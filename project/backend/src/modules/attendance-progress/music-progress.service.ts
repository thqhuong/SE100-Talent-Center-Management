/**
 * Subsystem 4: Music Progress Profile & Attendance Domain Service
 * Implements rules from Section 2.8 & supporting_analysis.md of SE100 Report v7:
 * - Three qualitative levels: NOT_ASSESSED ("Chưa đánh giá"), PRACTICING ("Đang luyện"), ACHIEVED ("Đạt").
 * - Absent students cannot receive skill assessments for that session.
 * - Current level per skill in an enrollment = latest locked effective assessment ordered by ACTUAL SESSION DATE (not edit timestamp).
 * - Course completion does NOT automatically upgrade skills to ACHIEVED or carry over to a new enrollment.
 */

export type SkillLevel = "NOT_ASSESSED" | "PRACTICING" | "ACHIEVED";

export interface SkillAssessmentRecord {
  assessmentId: string;
  enrollmentId: string;
  actualSessionId: string;
  actualSessionStartTime: Date;
  isSessionLocked: boolean;
  attendanceStatusAtSession: "PRESENT" | "ABSENT";
  skillReferenceId: string;
  skillName: string;
  practiceSegment: string;
  level: SkillLevel;
  comment?: string;
  assessedByTeacherId: string;
  isEffective: boolean;
}

export interface SkillProgressSummaryItem {
  skillReferenceId: string;
  skillName: string;
  currentLevel: SkillLevel;
  currentPracticeSegment: string;
  latestComment?: string;
  latestActualSessionDate?: Date;
  history: SkillAssessmentRecord[];
}

export class MusicProgressService {
  /**
   * Kiểm tra điều kiện trước khi cho phép Giảng viên lưu đánh giá kỹ năng trong buổi học.
   */
  public validateCanAssessStudent(params: {
    actorRole: "MANAGER" | "ACADEMIC_STAFF" | "TEACHER";
    actorTeacherId: string;
    assignedSessionTeacherId: string;
    attendanceStatus: "PRESENT" | "ABSENT";
  }): { allowed: boolean; reason?: string } {
    if (params.actorRole === "ACADEMIC_STAFF") {
      return {
        allowed: false,
        reason: "Giáo vụ chỉ có quyền xem và xuất tổng hợp học vụ, không được sửa đánh giá chuyên môn.",
      };
    }

    if (params.actorRole === "TEACHER" && params.actorTeacherId !== params.assignedSessionTeacherId) {
      return {
        allowed: false,
        reason: "Chỉ Giảng viên thực tế được phân công buổi học này mới có quyền cập nhật đánh giá.",
      };
    }

    if (params.attendanceStatus === "ABSENT") {
      return {
        allowed: false,
        reason: "Học viên Vắng mặt tại buổi học không phát sinh đánh giá tiến bộ âm nhạc.",
      };
    }

    return { allowed: true };
  }

  /**
   * Tổng hợp Hồ sơ tiến bộ âm nhạc cho 1 Ghi danh (1 khóa học độc lập):
   * Lấy đánh giá hợp lệ đã chốt có NGÀY BUỔI HỌC THỰC TẾ gần nhất cho từng kỹ năng tham chiếu.
   */
  public summarizeEnrollmentProgress(
    programSkills: Array<{ skillReferenceId: string; skillName: string }>,
    records: SkillAssessmentRecord[],
  ): SkillProgressSummaryItem[] {
    return programSkills.map((skill) => {
      const validHistory = records
        .filter(
          (r) =>
            r.skillReferenceId === skill.skillReferenceId &&
            r.isSessionLocked &&
            r.isEffective &&
            r.attendanceStatusAtSession === "PRESENT" &&
            r.level !== "NOT_ASSESSED",
        )
        .sort(
          (a, b) => b.actualSessionStartTime.getTime() - a.actualSessionStartTime.getTime(),
        );

      const latest = validHistory[0];

      return {
        skillReferenceId: skill.skillReferenceId,
        skillName: skill.skillName,
        currentLevel: latest ? latest.level : "NOT_ASSESSED",
        currentPracticeSegment: latest ? latest.practiceSegment : "Chưa thực hiện",
        latestComment: latest ? latest.comment : "Chưa có ghi nhận.",
        latestActualSessionDate: latest?.actualSessionStartTime,
        history: validHistory,
      };
    });
  }
}
