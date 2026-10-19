# SE100 - Phương pháp phát triển phần mềm hướng đối tượng (OOAD)

> **Tài liệu ngữ cảnh và chỉ dẫn dành cho AI Agents (Context & Agent Instructions)**  
> **Đồng bộ ngày 14/10/2026 (Asia/Saigon).** Trạng thái dưới đây dựa trên tài liệu lưu trong workspace; việc trình bày, nộp bài và duyệt cần có bằng chứng riêng.

---

## 1. Thông tin môn học & Nhân sự nhóm

- **Môn học**: Phương pháp phát triển phần mềm hướng đối tượng (Mã môn: **SE100**)
- **Đề tài đồ án**: **Phần mềm quản lý trung tâm dạy năng khiếu** (Âm nhạc, mỹ thuật, thể thao, kỹ năng...)
- **Tài liệu nền tảng đi kèm**:
  - [`SE100.md`](./SE100.md): Đề cương chi tiết môn học.
  - [`YC OOAD.md`](./YC%20OOAD.md): Bài toán Case Study mẫu môn học (*Hệ thống quản lý thư viện* - dùng làm chuẩn đối chiếu mẫu, không chọn làm đề tài).
  - [`Gợi ý nội dung báo cáo tiến độ.md`](./Gợi%20ý%20nội%20dung%20báo%20cáo%20tiến%20độ.md): Hướng dẫn chi tiết báo cáo tiến độ Lần 1, Lần 2 và khung cấu trúc chuẩn 5 chương cuốn báo cáo.
  - Khi xác định phạm vi hoặc chuẩn bị phân tích/thiết kế, đọc [`docs/DE_TAI.md`](./docs/DE_TAI.md): phạm vi đề xuất ngày 14/10 và định hướng ban đầu ngày 22/09 được giữ làm lịch sử.
  - Khi cập nhật báo cáo lần 1 hoặc truy vết FR/NFR/BR/UC, đọc [nguồn báo cáo ngày 14/10](./docs/report/_work_dot1_20261014/report_source.md) và [bản DOCX hiện có](./docs/report/SE100_BaoCaoTienDo_Dot1_Scope_SRS.docx). Đây là đầu ra phân tích cục bộ, chưa có bằng chứng đã nộp hoặc được duyệt.
  - Khi sửa sơ đồ lần 1, đối chiếu [`SE100_DOT1_DIAGRAMS.md`](./docs/diagrams/SE100_DOT1_DIAGRAMS.md) với cùng nguồn báo cáo.
- **Nhân sự theo báo cáo cục bộ ngày 14/10/2026**:

| Thành viên | MSSV | Vai trò |
| --- | --- | --- |
| Trần Hữu Quốc Hướng | 24520644 | Trưởng nhóm |
| Nguyễn Tuấn Khang | 24520763 | Thành viên |
| Nguyễn Lê Đức Huy | 24520680 | Thành viên |
| Dương Nguyễn Phú Quý | 24521489 | Thành viên |
| Nguyễn Văn Hoàng | 23520355 | Thành viên |
| Đào Phúc Đại | 24520244 | Thành viên |

Danh sách này thay cho mục “đang chờ cập nhật” của ngữ cảnh cũ; nguồn học phần hiện có không nêu trần số thành viên. Phân công trong báo cáo là kế hoạch đề xuất, chưa xác nhận công việc đã hoàn thành hoặc danh sách đã được giảng viên duyệt.

**Phạm vi đề xuất hiện hành:** ứng dụng web nội bộ cho một chi nhánh; ba vai trò Quản lý, Giáo vụ và Giảng viên; lớp theo khóa có số buổi cố định, thu đủ học phí một lần. Luồng lõi gồm mở lớp, xếp lịch, ghi danh, thu phí và sổ tiền chờ xử lý, điểm danh, nghỉ/học bù và báo cáo. Cổng phụ huynh, lương, khuyến mãi, bảo lưu dài hạn và hoàn phí tự động thuộc định hướng mở rộng. Chính sách nghiệp vụ cần được xác nhận khi khảo sát trung tâm.

---

## 2. Cấu trúc đánh giá môn học (Course Assessment)

Trọng số A1/A3/A4 theo đề cương ([SE100.md](./SE100.md)); điểm góp ý theo [hướng dẫn báo cáo tiến độ](./Gợi%20ý%20nội%20dung%20báo%20cáo%20tiến%20độ.md):

| Thành phần | Trọng số | Nội dung thực hiện |
| :--- | :---: | :--- |
| **A1. Quá trình** | **30%** | Kiểm tra trên lớp, bài tập nhóm, thảo luận |
| **A2. Giữa kỳ** | Đề cương để trống; AGENTS cũ ghi **0%** | AGENTS cũ ghi “Không thi lý thuyết giữa kỳ”; đề cương hiện có chưa xác nhận hình thức giữa kỳ. Giữ thông tin này để đối chiếu khi có thông báo lớp. |
| **A3. Thực hành** | **20%** | 6 buổi thực hành (StarUML, Use Case, Sequence, Class, CSDL, Cài đặt) |
| **A4. Cuối kỳ** | **50%** | **Vấn đáp đồ án OOAD** (Xây dựng phần mềm thực tế hoàn chỉnh) |
| **Cơ chế điểm thưởng (Bonus)** | **+5% -> +15%** | Sinh viên/nhóm có một đóng góp được công nhận hữu ích được cộng 5% số điểm; tích lũy tối đa 3 lần = 15%. QR phục vụ thu góp ý, chưa tự xác nhận điểm cộng. |

Quy định cần giữ từ đề cương: nộp bài tập/báo cáo trễ hạn coi như không nộp; xin phép nghỉ trước ít nhất 1 ngày, trừ bất khả kháng; vắng lý thuyết không phép từ 03 buổi sẽ không được thi cuối kỳ. Lịch 6 buổi thực hành theo đề cương không phải bằng chứng nhóm đã hoàn thành các buổi.

---

## 3. Quy cách đồ án & Khung báo cáo 5 chương bắt buộc

Mọi tài liệu báo cáo của môn học (lưu tại [`docs/`](./docs/)) và slide trình bày (lưu tại [`presentations/`](./presentations/)) phải tuân thủ nghiêm ngặt cấu trúc sau:

### Lần 1: Khảo sát, Yêu cầu & Tính khả thi
- Trình bày hoạt động nghiệp vụ cốt lõi, phạm vi tổ chức.
- Liệt kê các đối tượng con người (Actors) và đối tượng vật chất/thông tin.
- Luồng nghiệp vụ từ đầu đến cuối (Happy path).
- Ràng buộc nghiệp vụ, biến đổi thuộc tính theo thời gian và các kịch bản ngoại lệ (Edge cases).

### Lần 2: Thiết kế giao diện (Prototype / Frontend) & Khung báo cáo
Báo cáo hoàn chỉnh phải có cấu trúc 5 chương chuẩn:
* **Chương 1. Tổng quan đề tài**:
  - *1.1. Hiện trạng*: Khó khăn, bất cập của quy trình thực tế.
  - *1.2. Giới thiệu đề tài*: Mô tả chi tiết, giới hạn phạm vi, biểu mẫu chứng từ, quy định nghiệp vụ.
* **Chương 2. Phân tích (Analysis)**:
  - Sơ đồ Use Case tổng quát (chỉ thể hiện các nghiệp vụ lớn).
  - Đặc tả chi tiết các Use Case chính + Sơ đồ Activity Diagram & Sequence Diagram kèm thuyết minh.
* **Chương 3. Thiết kế (Design)**:
  - *3.1. Thiết kế cơ sở dữ liệu*: Mô hình ERD / Quan hệ.
  - *3.2. Thiết kế giao diện*: Sơ đồ liên kết màn hình (Screen Flow) + Wireframe/Mockup các chức năng chính.
  - *3.3. Thiết kế lớp (Class Diagram)*: Lược đồ quan hệ các lớp chi tiết (thuộc tính, kiểu dữ liệu, phương thức) + thuyết minh đặc tả từng lớp.
  - *3.4. Thiết kế kiến trúc (Architecture)*: Kiến trúc phân tầng (Layered, MVC...).
* **Chương 4. Xây dựng và triển khai ứng dụng (Implementation)**:
  - *4.1. Tổng quan công nghệ*: Ngôn ngữ, framework, DBMS.
  - *4.2. Sơ đồ thành phần (Component Diagram)*.
  - *4.3. Sơ đồ triển khai (Deployment Diagram)*.
  - *4.4. Bảng phân công công việc*: Ma trận phân công nhiệm vụ từng thành viên.
* **Chương 5. Tổng kết**:
  - *5.1. Kết quả đạt được*: Báo cáo kết quả, Link GitHub mã nguồn, Link Video Demo (công khai/unlisted cho GV), Thông tin liên hệ sinh viên phụ trách mã nguồn & video.
  - *5.2. Ưu khuyết điểm* của phần mềm.
  - *5.3. Hướng phát triển* trong tương lai.
* **Tài liệu tham khảo & Phụ lục**: Bảng quy ước và diễn giải ký hiệu các sơ đồ UML.

---

## 4. Cấu trúc thư mục chi tiết (Directory Layout)

```
d:\Hoc\HK5\SE100 - Phương pháp phát triển phần mềm hướng đối tượng/
├── AGENTS.md                                   <-- File này (AI Context Hub)
├── SE100.md                                    <-- Đề cương chi tiết môn học
├── YC OOAD.md                                  <-- Đề bài Case Study mẫu (Quản lý thư viện)
├── Gợi ý nội dung báo cáo tiến độ.md           <-- Quy chuẩn nội dung báo cáo tiến độ & 5 chương
├── project/                                    <-- Mã nguồn sản phẩm phần mềm
├── docs/                                       <-- Báo cáo đặc tả, thiết kế UML, SRS
│   ├── diagrams/                               <-- File ảnh/Mermaid sơ đồ UML
│   └── report/                                 <-- Báo cáo lần 1 và nguồn làm việc theo ngày
├── presentations/                              <-- Slide báo cáo (Lần 1, Lần 2, Cuối kỳ)
│   ├── lan-1/
│   ├── lan-2/
│   └── final/
└── labs/                                       <-- 6 Bài tập thực hành StarUML trên lớp
    ├── lab-01/
    └── ...
```

---

## 5. Bảng theo dõi tiến độ (Milestone Tracker)

Đối chiếu ngày 14/10/2026: đã có bản DOCX lần 1, QR góp ý, bốn sơ đồ tổng quan/mô hình miền và đặc tả 18 FR, 8 NFR, 12 BR, 5 Use Case. TC01–TC12 là kịch bản dự kiến. Chưa có bằng chứng trình bày hoặc nộp báo cáo; chưa có biên bản khảo sát, xác nhận chính sách hoặc kết quả chạy ứng dụng trong hồ sơ báo cáo.

| Cột mốc / Giai đoạn | Nội dung cần hoàn thành | Trạng thái | Deadline |
| :--- | :--- | :---: | :---: |
| **Chọn đề tài** | Đã chốt đề tài: **Phần mềm quản lý trung tâm dạy năng khiếu** | `Đã hoàn thành` | 22/09/2026 |
| **Báo cáo Lần 1** | Bản phân tích, phạm vi, Actor, Use Case, luồng nghiệp vụ và QR đã có; tiếp tục khảo sát/xác nhận chính sách và chuẩn bị trình bày | `Có bản báo cáo cục bộ; chưa xác nhận đã trình bày/nộp` | Chưa có hạn chính thức trong tài liệu |
| **Báo cáo Lần 2** | Hoàn thiện Prototype/Giao diện, Sơ đồ liên kết màn hình & Khung báo cáo | `Chưa có minh chứng đầu ra cục bộ` | Chưa có hạn chính thức trong tài liệu |
| **Labs thực hành** | Hoàn thành 6 bài thực hành StarUML theo lịch trên lớp | `Chưa có minh chứng hoàn thành cục bộ` | Theo lịch trên lớp; chưa có ngày cụ thể trong tài liệu |
| **Hoàn thiện đồ án** | Code ứng dụng, quay Video Demo, kiểm thử, đóng gói báo cáo 5 chương | `Chưa có minh chứng hoàn thành cục bộ` | Cuối kỳ |

Bảng cũ ghi “Chưa bắt đầu” cho báo cáo, labs và đồ án. Bảng này cập nhật theo hiện vật lưu tại đây; công việc làm ở nơi khác cần đối chiếu với nhóm. Khi cập nhật, ghi nguồn và ngày của trạng thái/hạn mới; giữ các mốc cũ có giá trị lịch sử.

---

## 6. Chỉ thị & Quy tắc dành cho AI Agents

1. **Ngôn ngữ chuẩn mực**:
   - Viết tài liệu báo cáo, giải thích nghiệp vụ, thuyết minh sơ đồ: **Tiếng Việt**.
   - Thiết kế Class diagram, thuộc tính, phương thức, mã nguồn code, commit git: **Tiếng Anh**.
2. **Quy tắc vẽ biểu đồ UML**:
   - **Bắt buộc dùng định dạng Mermaid.js** trong tài liệu Markdown để người dùng và AI đều xem/sửa đổi dễ dàng:
     - Use Case Diagram (`quadrantChart` hoặc `flowchart`)
     - Activity Diagram (`flowchart TD`)
     - Sequence Diagram (`sequenceDiagram`)
     - Class Diagram (`classDiagram`)
     - Component/Deployment Diagram (`flowchart`)
3. **Nhắc nhở tương tác lớp**:
   - Khi soạn báo cáo/slide lần 1 hoặc lần 2, đặt **mã QR góp ý** ở trang đầu theo hướng dẫn môn. Dùng [biểu mẫu có trong báo cáo ngày 14/10](https://docs.google.com/forms/d/e/1FAIpQLSenTD2JN9DCcaVJOOXoAiWOsRG7jEftdgfszZExJ_lw_65Rvg/viewform?usp=header); ghi nhận người góp ý có mặt tại lớp, chia sẻ kết quả cho giảng viên và đánh dấu ý kiến hữu ích. Ghi điểm cộng theo kết quả công nhận thực tế.
4. **Tuân thủ đúng Case Study**:
   - Nhớ rằng nội dung trong [`YC OOAD.md`](./YC%20OOAD.md) là bài toán mẫu của giảng viên để tham khảo kỹ thuật mô tả, **không được dùng bài quản lý thư viện làm đề tài đồ án**.
