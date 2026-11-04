/**
 * Subsystem 5: Makeup Assistant Domain Service (Trợ lý học bù — Lọc 6 tiêu chí có giải thích)
 * Synchronized with Section 2.9 & Table 2.6 of SE100 Report v7.
 */

export interface MakeupRightContext {
  makeupRightId: string;
  enrollmentId: string;
  studentId: string;
  subjectCode: string; // VD: "PIANO"
  levelName: string; // VD: "Cấp độ 1"
  originalTopicCode: string; // VD: "PN-CB1-T05" (Bài đọc nốt số 1)
  originalClassId: string;
  originalClassType: "GROUP" | "ONE_ON_ONE";
  originalTeacherId: string;
  requiredDurationMinutes: number; // VD: 60 phút
  expiresAt: Date; // Hạn sử dụng quyền bù (30 ngày từ cuối buổi gốc)
  studentExistingIntervals: Array<{ startTime: Date; endTime: Date; label: string }>;
}

export interface CandidateMakeupSession {
  sessionId: string;
  classId: string;
  classCode: string; // VD: "PN-CB1-K14"
  subjectCode: string;
  levelName: string;
  topicCode: string;
  isTopicEquivalenceVerified: boolean;
  classType: "GROUP" | "ONE_ON_ONE";
  teacherId: string;
  startTime: Date;
  endTime: Date;
  remainingSeats: number; // Đã trừ học viên chính thức + lịch bù hiệu lực (không lấy chỗ người mới báo nghỉ)
  isRoomAndEquipmentQualified: boolean;
}

export interface MakeupCandidateEvaluation {
  sessionId: string;
  classCode: string;
  isEligible: boolean;
  criteriaResults: {
    c1_subjectAndLevel: boolean;
    c2_equivalentTopic: boolean;
    c3_matchingClassType: boolean;
    c4_roomAndSeatCapacity: boolean;
    c5_noStudentScheduleConflict: boolean;
    c6_durationAndWithinExpiry: boolean;
  };
  explanationReason: string; // Lý do Đề xuất hoặc Loại hiển thị trên màn hình SC-19
  priorityRank?: number;
}

export class MakeupAssistantService {
  /**
   * Đối chiếu danh sách buổi học tương lai qua 6 tiêu chí (Mục 2.9b Báo cáo v7)
   * và sắp xếp thứ tự ưu tiên: Ngày gần nhất -> Cùng Giảng viên lớp gốc -> Giờ bắt đầu -> Mã buổi.
   */
  public evaluateCandidates(
    right: MakeupRightContext,
    candidates: CandidateMakeupSession[],
  ): MakeupCandidateEvaluation[] {
    const evaluations: Array<MakeupCandidateEvaluation & { _candidate: CandidateMakeupSession }> =
      candidates.map((session) => {
        // Tiêu chí 1: Đúng bộ môn và cấp độ
        const c1 =
          session.subjectCode === right.subjectCode && session.levelName === right.levelName;

        // Tiêu chí 2: Chủ đề tương đương đã được xác minh
        const c2 =
          session.topicCode === right.originalTopicCode && session.isTopicEquivalenceVerified;

        // Tiêu chí 3: Đúng hình thức lớp (Nhóm ghép vào nhóm; 1:1 dùng buổi bù riêng)
        const c3 =
          right.originalClassType === "GROUP" &&
          session.classType === "GROUP" &&
          session.classId !== right.originalClassId;

        // Tiêu chí 4: Còn chỗ trống và đủ điều kiện phòng/thiết bị
        const c4 = session.isRoomAndEquipmentQualified && session.remainingSeats > 0;

        // Tiêu chí 5: Không trùng lịch cá nhân của học viên (lớp khác hoặc lịch bù khác)
        const conflictingSlot = right.studentExistingIntervals.find(
          (slot) => session.startTime < slot.endTime && session.endTime > slot.startTime,
        );
        const c5 = !conflictingSlot;

        // Tiêu chí 6: Đủ thời lượng chuẩn và kết thúc không muộn hơn hạn quyền bù
        const durationMinutes =
          (session.endTime.getTime() - session.startTime.getTime()) / (1000 * 60);
        const c6 =
          durationMinutes >= right.requiredDurationMinutes && session.endTime <= right.expiresAt;

        const isEligible = c1 && c2 && c3 && c4 && c5 && c6;

        const reasons: string[] = [];
        if (!c1) reasons.push("Khác bộ môn hoặc cấp độ");
        if (!c2) reasons.push("Chủ đề bài học chưa tương đương hoặc chờ xác minh");
        if (!c3)
          reasons.push(
            right.originalClassType === "ONE_ON_ONE"
              ? "Lớp kèm 1:1 phải xếp buổi bù riêng (SC-20), không ghép nhóm"
              : "Không đúng hình thức lớp nhóm hoặc trùng lớp gốc",
          );
        if (!c4) reasons.push("Không còn chỗ học hoặc phòng thiếu nhạc cụ tốt");
        if (!c5) reasons.push(`Trùng lịch cá nhân (${conflictingSlot?.label})`);
        if (!c6) reasons.push("Không đủ thời lượng hoặc kết thúc sau hạn sử dụng quyền bù");

        const explanationReason = isEligible
          ? `Đề xuất: Đạt đủ 6 tiêu chí${
              session.teacherId === right.originalTeacherId ? "; cùng Giảng viên lớp gốc" : ""
            }; còn ${session.remainingSeats} chỗ.`
          : `Loại: ${reasons.join("; ")}.`;

        return {
          sessionId: session.sessionId,
          classCode: session.classCode,
          isEligible,
          criteriaResults: {
            c1_subjectAndLevel: c1,
            c2_equivalentTopic: c2,
            c3_matchingClassType: c3,
            c4_roomAndSeatCapacity: c4,
            c5_noStudentScheduleConflict: c5,
            c6_durationAndWithinExpiry: c6,
          },
          explanationReason,
          _candidate: session,
        };
      });

    // Sắp xếp các buổi đạt điều kiện theo ngày gần nhất -> cùng Giảng viên lớp gốc -> mã buổi
    const eligible = evaluations
      .filter((e) => e.isEligible)
      .sort((a, b) => {
        const dayA = new Date(a._candidate.startTime).setHours(0, 0, 0, 0);
        const dayB = new Date(b._candidate.startTime).setHours(0, 0, 0, 0);
        if (dayA !== dayB) return dayA - dayB;
        const sameTeacherA = a._candidate.teacherId === right.originalTeacherId ? 0 : 1;
        const sameTeacherB = b._candidate.teacherId === right.originalTeacherId ? 0 : 1;
        if (sameTeacherA !== sameTeacherB) return sameTeacherA - sameTeacherB;
        return a._candidate.startTime.getTime() - b._candidate.startTime.getTime();
      });

    eligible.forEach((item, idx) => {
      item.priorityRank = idx + 1;
    });

    return evaluations.map(({ _candidate, ...rest }) => rest);
  }
}
