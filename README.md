# SE100 — Phần mềm quản lý trung tâm dạy năng khiếu

[![Course](https://img.shields.io/badge/Course-SE100%20OOAD-blue.svg)](./SE100.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![UML Standard](https://img.shields.io/badge/Modeling-UML%202.5-orange.svg)](https://www.uml.org/)

Đồ án môn học: **Phương pháp phát triển phần mềm hướng đối tượng (OOAD) — SE100**  
Khoa Kỹ thuật Phần mềm — Trường ĐH Công nghệ Thông tin (UIT - VNUHCM).

---

## 👥 Danh sách Thành viên Thực hiện (Nhóm Đồ án)

| STT | MSSV | Họ và tên | Vai trò | Trách nhiệm chính |
| :---: | :---: | :--- | :---: | :--- |
| 1 | `24520644` | **Trần Hữu Quốc Hướng** | 👑 **Trưởng nhóm** | Quản lý tiến độ, kiến trúc hệ thống, Use Case lõi, tổng hợp báo cáo |
| 2 | `24520763` | **Nguyễn Tuấn Khang** | Thành viên | Phân tích nghiệp vụ, Sequence Diagrams, giao diện |
| 3 | `24520680` | **Nguyễn Lê Đức Huy** | Thành viên | Thiết kế CSDL (ERD/Relational), Class Diagram |
| 4 | `24521489` | **Dương Nguyễn Phú Quý** | Thành viên | Phân tích yêu cầu FR/NFR, Activity Diagrams |
| 5 | `23520355` | **Nguyễn Văn Hoàng** | Thành viên | Thiết kế giao diện (Wireframes/Mockup), Component Diagram |
| 6 | `24520244` | **Đào Phúc Đại** | Thành viên | Phân tích kịch bản ngoại lệ, Deployment Diagram, kiểm thử |

---

## 🎯 Giới thiệu Đề tài & Phạm vi Nghiệp vụ

Phần mềm hỗ trợ quản lý vận hành trung tâm đào tạo các môn năng khiếu (âm nhạc, mỹ thuật, thể thao, kỹ năng sống) tại một chi nhánh:
- **3 vai trò người dùng**: Quản lý trung tâm, Giáo vụ, Giảng viên.
- **Quản lý khóa học & lớp học**: Thiết lập lớp theo khóa với số buổi cố định, quản lý phòng học và lịch dạy.
- **Ghi danh & Học phí**: Thu học phí trọn gói theo khóa, xuất phiếu thu và quản lý sổ tiền chờ duyệt.
- **Điểm danh & Học bù**: Theo dõi buổi học, xử lý học viên vắng có phép và sắp xếp lớp học bù.
- **Báo cáo thống kê**: Thống kê doanh thu, sĩ số lớp học và hiệu suất giảng dạy.

---

## 🏛️ Khung Báo cáo 5 Chương Chuẩn OOAD

1. **Chương 1. Tổng quan đề tài**: Hiện trạng thực tế, mục tiêu đề tài, giới hạn phạm vi, biểu mẫu chứng từ và quy định nghiệp vụ.
2. **Chương 2. Phân tích (Analysis)**: Sơ đồ Use Case tổng quát, đặc tả Use Case chi tiết, sơ đồ Activity Diagram và Sequence Diagram.
3. **Chương 3. Thiết kế (Design)**: Thiết kế CSDL quan hệ (ERD), thiết kế Screen Flow & Wireframes, thiết kế chi tiết các lớp (Class Diagram), kiến trúc phân tầng (Layered/MVC).
4. **Chương 4. Xây dựng và Triển khai (Implementation)**: Tổng quan công nghệ, Component Diagram, Deployment Diagram, ma trận phân công công việc.
5. **Chương 5. Tổng kết**: Đánh giá kết quả, ưu khuyết điểm, hướng phát triển và liên kết video demo.

---

## 📂 Cấu trúc Thư mục

```
SE100-Talent-Center-Management/
├── docs/                     # Tài liệu đặc tả yêu cầu, thiết kế UML, báo cáo tiến độ
│   ├── diagrams/             # Sơ đồ Mermaid, ảnh export StarUML
│   └── report/               # Báo cáo Đợt 1, Đợt 2 và bản cuối kỳ
├── project/                  # Mã nguồn ứng dụng (Frontend, Backend, Database)
├── presentations/            # Slide thuyết trình Đợt 1, Đợt 2 và Vấn đáp cuối kỳ
├── labs/                     # Bài tập thực hành 6 buổi môn học
├── CONTRIBUTING.md           # Hướng dẫn đóng góp và quy ước Git
├── CHANGELOG.md              # Nhật ký các đợt nộp báo cáo và sprint
└── README.md                 # Tài liệu này
```
