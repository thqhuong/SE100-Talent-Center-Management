/**
 * Subsystem 3: Enrollment & One-Touch Full Tuition Billing Domain Service
 * Implements rules from Section 2.7 & supporting_analysis.md of SE100 Report v7:
 * - Pre-course enrollment only; full course tuition collected in one transaction.
 * - Atomic confirmation: Enrollment + Receipt + Seat reservation across all 24 sessions.
 * - Last-seat contention protection & PendingFund fallback when money is already received.
 * - Idempotency key & Unique bankReference to prevent duplicate receipts on network retry.
 */

export interface ConfirmEnrollmentCommand {
  idempotencyKey: string;
  studentId: string;
  classId: string;
  payerName: string;
  receivedAmount: number;
  paymentMethod: "CASH" | "BANK_TRANSFER";
  bankReference?: string; // VD: "VCB-20261102-998877"
  staffId: string;
}

export interface EnrollmentValidationContext {
  classStatus: "PREPARING" | "ENROLLING" | "ONGOING" | "COMPLETED" | "CANCELLED";
  committedTuitionFee: number; // VD: 2.400.000 VND
  minRemainingSeatsAcrossAll24Sessions: number;
  hasScheduleConflictForStudent: boolean;
  existingReceiptByIdempotencyKey?: { receiptCode: string; enrollmentCode?: string };
  existingReceiptByBankReference?: { receiptCode: string };
}

export type EnrollmentOutcome =
  | {
      outcomeType: "IDEMPOTENT_REPLAY";
      receiptCode: string;
      enrollmentCode?: string;
      message: string;
    }
  | {
      outcomeType: "DUPLICATE_BANK_REFERENCE_REJECTED";
      existingReceiptCode: string;
      targetScreen: "SC-26";
      message: string;
    }
  | {
      outcomeType: "ENROLLED_AND_RECEIPT_ISSUED";
      targetScreen: "SC-13";
      appliedMinLeaveNoticeHours: number;
      appliedMakeupExpiryDays: number;
      message: string;
    }
  | {
      outcomeType: "MOVED_TO_PENDING_FUND";
      targetScreen: "SC-25" | "SC-14";
      pendingFundReason: string;
      message: string;
    };

export class EnrollmentBillingService {
  /**
   * Đánh giá điều kiện xác nhận Ghi danh – Thu phí trong giao dịch nguyên tử.
   * Nếu tiền đã thực nhận nhưng lớp vừa hết chỗ ở tích tắc cuối (Quầy khác vừa nhận chỗ thứ 5/5),
   * hệ thống giữ khoản tiền vào Hồ sơ Tiền chờ xử lý (PendingFund - SC-25 / SC-14), chưa xác nhận quyền học.
   */
  public evaluateEnrollmentConfirmation(
    cmd: ConfirmEnrollmentCommand,
    ctx: EnrollmentValidationContext,
  ): EnrollmentOutcome {
    // 1. Chống gửi lặp khi mất phản hồi mạng (Idempotency Key)
    if (ctx.existingReceiptByIdempotencyKey) {
      return {
        outcomeType: "IDEMPOTENT_REPLAY",
        receiptCode: ctx.existingReceiptByIdempotencyKey.receiptCode,
        enrollmentCode: ctx.existingReceiptByIdempotencyKey.enrollmentCode,
        message: "Thao tác lặp cùng Idempotency Key: Trả lại chứng từ gốc đã lưu, không thu trùng.",
      };
    }

    // 2. Chống nhập lại cùng một mã giao dịch ngân hàng (Unique Bank Reference - SC-26)
    if (cmd.paymentMethod === "BANK_TRANSFER" && ctx.existingReceiptByBankReference) {
      return {
        outcomeType: "DUPLICATE_BANK_REFERENCE_REJECTED",
        existingReceiptCode: ctx.existingReceiptByBankReference.receiptCode,
        targetScreen: "SC-26",
        message: `Mã giao dịch ngân hàng ${cmd.bankReference} đã được ghi nhận tại phiếu ${ctx.existingReceiptByBankReference.receiptCode}.`,
      };
    }

    // 3. Kiểm tra tranh chấp chỗ đàn cuối (Last-seat contention - SC-25)
    if (ctx.minRemainingSeatsAcrossAll24Sessions <= 0) {
      return {
        outcomeType: "MOVED_TO_PENDING_FUND",
        targetScreen: "SC-25",
        pendingFundReason: "Lớp vừa hết chỗ trống (5/5 đàn Piano) ngay khi xác nhận.",
        message:
          "Chỗ học cuối cùng vừa được quầy khác xác nhận. Khoản tiền đã nhận được lưu vào Tiền chờ xử lý (SC-14) để đổi lớp hoặc hoàn trả.",
      };
    }

    // 4. Kiểm tra số tiền thực nhận phải khớp học phí trọn khóa (không thu thiếu/trả góp)
    if (cmd.receivedAmount !== ctx.committedTuitionFee || ctx.classStatus !== "ENROLLING") {
      return {
        outcomeType: "MOVED_TO_PENDING_FUND",
        targetScreen: "SC-14",
        pendingFundReason:
          cmd.receivedAmount !== ctx.committedTuitionFee
            ? `Số tiền nhận (${cmd.receivedAmount}) lệch học phí trọn khóa (${ctx.committedTuitionFee}).`
            : "Lớp không còn ở trạng thái Đang tuyển sinh.",
        message: "Chưa đủ điều kiện xác nhận quyền học; ghi nhận vào Tiền chờ xử lý để đối soát.",
      };
    }

    // 5. Hợp lệ toàn diện -> Lưu nguyên tử Ghi danh hiệu lực + Phiếu thu
    return {
      outcomeType: "ENROLLED_AND_RECEIPT_ISSUED",
      targetScreen: "SC-13",
      appliedMinLeaveNoticeHours: 24,
      appliedMakeupExpiryDays: 30,
      message: "Đã lưu Ghi danh hiệu lực và phát hành Phiếu thu trong cùng một giao dịch nguyên tử.",
    };
  }
}
