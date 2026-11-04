/**
 * Subsystem 1 & 2: Room & Instrument Effective Capacity Domain Service
 * Implements the music-center capacity rules from Section 2.5b & 2.9.1 of SE100 Report v7.
 */

export interface RoomCapacityInput {
  classMaxCapacity: number; // Nhóm: 5 | Kèm 1:1: 1
  roomMaxHumanCapacity: number; // Sức chứa người của phòng (VD: P-101 = 5, P-301 Thanh nhạc = 5)
  requiresIndividualInstrument: boolean; // true: Piano, Trống | false: Thanh nhạc
  goodInstrumentCount: number; // Số đàn/trống sử dụng tốt (VD: 5 đàn Piano tốt)
  hasWorkingSharedAudioAndMics: boolean; // Điều kiện thiết bị âm thanh/micro cho Thanh nhạc
  activeRegularEnrollmentsCount: number; // Số học viên chính thức đang hiệu lực
  confirmedMakeupBookingsCount: number; // Số lịch bù đã xác nhận vào buổi này
  notifiedLeaveCount?: number; // Số học viên chính thức đã báo nghỉ (KHÔNG làm tăng chỗ trống)
}

export interface SessionSeatAvailability {
  effectiveCapacity: number;
  occupiedSeats: number;
  remainingSeats: number;
  isEquipmentQualified: boolean;
  explanation: string;
}

export class RoomCapacityService {
  /**
   * Tính sức chứa sử dụng được (Effective Capacity) và số chỗ còn lại của một buổi học.
   * - Nhạc cụ cá nhân (Piano, Trống): min(Trần lớp, Sức chứa phòng, Số nhạc cụ tốt).
   * - Thanh nhạc: min(Trần lớp, Sức chứa người của phòng) khi đủ điều kiện âm thanh/micro;
   *   tuyệt đối KHÔNG quy đổi 1 micro thành 1 học viên.
   * - Chỗ còn lại = Sức chứa hiệu dụng - (Học viên chính thức hiệu lực + Lịch bù đã xác nhận).
   *   Không lấy chỗ của học viên chính thức đã báo nghỉ vì họ vẫn có thể đến học.
   */
  public calculateSessionAvailability(input: RoomCapacityInput): SessionSeatAvailability {
    if (!input.requiresIndividualInstrument && !input.hasWorkingSharedAudioAndMics) {
      return {
        effectiveCapacity: 0,
        occupiedSeats: input.activeRegularEnrollmentsCount + input.confirmedMakeupBookingsCount,
        remainingSeats: 0,
        isEquipmentQualified: false,
        explanation: "Phòng Thanh nhạc thiếu thiết bị âm thanh/micro sử dụng tốt.",
      };
    }

    const effectiveCapacity = input.requiresIndividualInstrument
      ? Math.min(input.classMaxCapacity, input.roomMaxHumanCapacity, input.goodInstrumentCount)
      : Math.min(input.classMaxCapacity, input.roomMaxHumanCapacity);

    const occupiedSeats = input.activeRegularEnrollmentsCount + input.confirmedMakeupBookingsCount;
    const remainingSeats = Math.max(0, effectiveCapacity - occupiedSeats);

    return {
      effectiveCapacity,
      occupiedSeats,
      remainingSeats,
      isEquipmentQualified: effectiveCapacity > 0,
      explanation: input.requiresIndividualInstrument
        ? `Sức chứa hiệu dụng = min(Trần lớp ${input.classMaxCapacity}, Phòng ${input.roomMaxHumanCapacity}, Đàn tốt ${input.goodInstrumentCount}) = ${effectiveCapacity}. Đã xếp: ${input.activeRegularEnrollmentsCount} chính thức + ${input.confirmedMakeupBookingsCount} học bù.`
        : `Phòng Thanh nhạc tính theo sức chứa người (${effectiveCapacity}), đủ thiết bị âm thanh; còn ${remainingSeats} chỗ.`,
    };
  }
}
