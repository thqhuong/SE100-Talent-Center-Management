# BẢN NHẬN XÉT VÀ ĐÁNH GIÁ BÁO CÁO TIẾN ĐỘ ĐỢT 1 - SE100
**Môn học:** Phương pháp phát triển phần mềm hướng đối tượng (OOAD) - Mã môn: SE100  
**Học kỳ:** Học kỳ 1, Năm học 2026–2027 (HK5) - Trường ĐH Công nghệ Thông tin, ĐHQG-HCM  
**Người đánh giá:** Giảng viên hướng dẫn & chấm đồ án SE100 (Roleplay qua Subagent)  
**Nhóm sinh viên:** Nhóm 6 thành viên (Trưởng nhóm: Trần Hữu Quốc Hướng - 24520644)  
**Tài liệu thẩm định:** `docs/report/SE100_BaoCaoTienDo_Dot1_Scope_SRS.docx` (Nguồn: `report_source.md`)  
**Tài liệu đối chiếu:** `Gợi ý nội dung báo cáo tiến độ.md`, `SE100.md`, `YC OOAD.md`, `docs/DE_TAI.md`  
**Ngày đánh giá:** 15/10/2026

---

## I. TỔNG QUAN ĐÁNH GIÁ (EXECUTIVE SUMMARY)

- **Điểm đánh giá sơ bộ:** **8.5 / 10** (Xếp loại: **Tốt về tư duy logic và kỹ thuật phần mềm, nhưng cần điều chỉnh để khớp đúng trọng tâm môn học OOAD Đợt 1**).
- **Nhận xét tổng quan:**
  Nhóm có sự đầu tư cực kỳ nghiêm túc, văn phong gãy gọn, lập luận logic và xử lý các vấn đề toàn vẹn dữ liệu (concurrency, transaction, idempotency, edge cases) rất tốt — hiếm thấy ở mức độ sinh viên năm 3. Tuy nhiên, bản báo cáo hiện tại đang mang dáng dấp của một bản **Đặc tả yêu cầu phần mềm kỹ thuật (Technical SRS / Testing Specification)** nhiều hơn là một bản **Báo cáo tiến độ Lần 1 môn OOAD (Xác định yêu cầu đề tài + Tính khả thi)** theo định hướng của Giảng viên và chuẩn đào tạo khoa KHMT/KTPM UIT.

### 03 Ưu điểm nổi bật nhất:
1. **Xử lý ràng buộc và kịch bản ngoại lệ cực kỳ chặt chẽ:** Quy định về sĩ số (BR02), giao dịch tiền mặt/chờ xử lý (BR07), vắng và quyền học bù (BR10, BR11) giải quyết được bài toán khó mà nhiều nhóm thường bỏ qua (tranh chỗ cuối, không sinh quyền bù kép, tách biệt chuyên cần gốc và lượt bù).
2. **Tính trung thực học thuật cao:** Báo cáo liên tục làm rõ ranh giới giữa những gì đã phân tích sơ bộ và những gì cần khảo sát thực tế, không "nổ" hay báo cáo khống tiến độ.
3. **Phân công trách nhiệm minh bạch:** Bảng phân công 6 thành viên có cơ chế rà soát chéo (Peer Review) rất rõ ràng, thể hiện vai trò điều phối tốt của nhóm trưởng.

### 03 Tồn tại lớn nhất cần khắc phục ngay:
1. **Thiếu đặc thù thực tế của mô hình "Trung tâm năng khiếu":** Nội dung còn mang tính trừu tượng của một trung tâm quản lý lớp học chung chung. Thiếu hẳn các yếu tố cốt lõi của môn năng khiếu: phân loại môn (Âm nhạc, Mỹ thuật, Cờ vua, Múa), phân loại hình thức lớp (Lớp 1 kèm 1, Lớp nhóm nhỏ 3–5 học viên, Lớp tiêu chuẩn), yêu cầu phòng học đặc thù (phòng cách âm đàn piano, phòng vẽ có giá vẽ/ánh sáng, sân tập), và quy trình kiểm tra trình độ/buổi học thử (Placement Test / Trial Lesson).
2. **Thừa thãi và "nhảy cóc" sang Đợt 2 / Cuối kỳ:** Báo cáo nhồi nhét quá nhiều chi tiết thuộc về Đợt 2 và Đợt cuối: 18 FR, 8 NFR chi tiết tải/mã hóa, 12 Test Cases (TC01–TC12), kiến trúc phân tầng 3-tier, quy chuẩn băm mật khẩu, công thức CSV... Việc này làm loãng trọng tâm phân tích hướng đối tượng (OOA) ở Đợt 1.
3. **Sơ đồ UML chưa chuẩn hóa theo hướng đối tượng (OOAD):** Sơ đồ Use Case đặt tên theo phân hệ chức năng (danh từ) thay vì hành động nghiệp vụ (động từ + danh từ); Sơ đồ luồng (Workflow) chỉ mô tả một nhánh kỹ thuật thanh toán thay vì luồng nghiệp vụ xuyên suốt (End-to-End Business Process); Sơ đồ miền thiếu thuộc tính đặc trưng của các lớp.

---

## II. ĐỐI CHIẾU CHI TIẾT VỚI 5 NỘI DUNG CỐT LÕI CỦA LẦN 1
*(Căn cứ theo mục 2 - Lần 1 trong tài liệu `Gợi ý nội dung báo cáo tiến độ.md`)*

### 1. Khái niệm & Bối cảnh nghiệp vụ
- **Mức độ đạt:** `7.0 / 10` (Khá).
- **Điểm đạt:** Xác định rõ mô hình 1 chi nhánh tư nhân, khóa học trọn gói, số buổi cố định, thu học phí một lần.
- **Hạn chế:**
  - Nhóm lặp lại quá nhiều lần cụm từ "chưa có biên bản khảo sát trung tâm". Thay vì chỉ nói "chưa có", nhóm cần đưa vào kết quả khảo sát thực tế từ 1–2 trung tâm năng khiếu điển hình (hoặc bảng đối chiếu quy trình thực tế) để chứng minh bài toán có thật.
  - Cần làm rõ sự khác biệt của việc dạy năng khiếu so với dạy văn hóa: năng khiếu đòi hỏi trang thiết bị chuyên biệt (đàn piano, organ, trống, giá vẽ, màu, thảm tập), sĩ số thường rất nhỏ (1–5 học viên), học viên nghỉ học rất thường xuyên dẫn đến nhu cầu học bù rất cao.

### 2. Đối tượng tham gia (Actors & Objects)
- **Mức độ đạt:** `7.5 / 10` (Khá).
- **Điểm đạt:** Đã xác định được 3 tác nhân trực tiếp: Quản lý, Giáo vụ, Giảng viên.
- **Hạn chế:**
  - **Đối tượng con người (Actors):** Việc gạt Phụ huynh/Học viên ra ngoài phần mềm trong phiên bản đầu là chấp nhận được để kiểm soát khối lượng (MVP), nhưng cần bổ sung phân tích nghiệp vụ về *sự tương tác giữa Phụ huynh và Giáo vụ* (tiếp nhận nhu cầu, độ tuổi của học viên từ 4–15 tuổi cần có người giám hộ).
  - **Đối tượng vật chất / tài sản phát sinh (Objects):** Báo cáo chỉ mới nêu chung chung "phòng và thiết bị cố định". Cần chỉ rõ đối tượng: Nhạc cụ, Giá vẽ/Họa cụ, Phòng tập chuyên dụng, Phiếu thu, Biên nhận, Thẻ học viên, Sổ điểm danh.
  - **Thuộc tính cần thu thập:** Cần liệt kê thuộc tính trực quan cho các đối tượng trong chương trình học (Độ tuổi phù hợp, Trình độ đầu vào, Sĩ số tối đa/tối thiểu của từng môn).

### 3. Phạm vi & Nhu cầu phần mềm
- **Mức độ đạt:** `8.5 / 10` (Tốt).
- **Điểm đạt:** Bảng phân định Trong phạm vi (In-Scope) và Ngoài phạm vi (Out-of-Scope) rất rõ ràng, dứt khoát. Giới hạn 1 chi nhánh, không làm cổng thanh toán online, không làm đa chi nhánh là quyết định sáng suốt cho đồ án học kỳ.
- **Hạn chế:** Cần bổ sung lý do tại sao phần mềm thủ công (Excel, sổ sách) thất bại: Việc xếp lịch học bù và kiểm tra trùng phòng chuyên dụng trên Excel khi có hàng chục lớp nhóm nhỏ là "cơn ác mộng" đối với giáo vụ. Đây là điểm thuyết phục nhất để xây dựng phần mềm.

### 4. Luồng nghiệp vụ & Tương tác (Business Workflows)
- **Mức độ đạt:** `6.5 / 10` (Trung bình khá).
- **Điểm đạt:** Xử lý luồng thu tiền và ghi sổ khoản chờ rất tỉ mỉ, chặt chẽ.
- **Hạn chế lớn:**
  - Báo cáo đang bị "lệch trọng tâm": dành quá nhiều dung lượng cho việc tranh chấp tiền mặt và lỗi giao dịch CSDL, trong khi **luồng nghiệp vụ sư phạm tổng thể** lại bị bỏ quên.
  - Một trung tâm năng khiếu có quy trình tương tác chuẩn gồm 6 giai đoạn:
    1. *Tư vấn & Đăng ký đánh giá năng khiếu/học thử (Placement Test / Trial).*
    2. *Xếp lớp phù hợp với độ tuổi & trình độ.*
    3. *Ghi danh & Đóng học phí trọn gói (Xuất phiếu thu).*
    4. *Vận hành buổi học: Điểm danh, ghi nhận xét tiến bộ năng khiếu từng buổi.*
    5. *Xử lý biến động: Xin nghỉ có phép $\rightarrow$ Xếp lịch học bù cùng môn/cấp độ.*
    6. *Tổng kết khóa: Báo cáo chuyên cần, đánh giá kết quả rèn luyện.*
  - Cần vẽ lại hoặc mở rộng sơ đồ Luồng nghiệp vụ (Workflow) để thể hiện trọn vẹn luồng này, thay vì chỉ vẽ mỗi thao tác kiểm tra chỗ và ghi sổ tiền chờ.

### 5. Ràng buộc, Biến động & Kịch bản ngoại lệ (Constraints & Edge Cases)
- **Mức độ đạt:** `9.0 / 10` (Rất tốt).
- **Điểm đạt:** Bảng ràng buộc sĩ số, kiểm tra giao thoa thời gian ($Start_A < End_B \land Start_B < End_A$), vòng đời lớp học, quyền học bù 30 ngày được đặc tả xuất sắc.
- **Cần hoàn thiện:** Cần bổ sung kịch bản: Lớp không đủ sĩ số tối thiểu thì xử lý ra sao (hủy lớp hoàn tiền hay dời ngày khai giảng)? Giảng viên bận đột xuất cần đổi giảng viên dạy thay thì kiểm tra chuyên môn thế nào?

---

## III. BẢNG PHÂN LOẠI CHI TIẾT: THỪA - THIẾU - CẦN ĐIỀU CHỈNH

| Vị trí trong báo cáo | Nội dung hiện tại | Đánh giá | Hướng dẫn chỉnh sửa cụ thể |
| :--- | :--- | :---: | :--- |
| **Trang bìa & Đầu tài liệu** | Mã QR dẫn đến form Google khảo sát | **CẦN SỬA** | Cần ghi rõ: *"Mã QR thu thập góp ý phản biện tại lớp – Điểm cộng 5% đến 15% cho đóng góp hữu ích theo quy chế môn học"*. Phải phân biệt rõ đây là form góp ý trên lớp, không phải form khảo sát yêu cầu khách hàng. |
| **Mục 1.1 (Chương 1)** | Bối cảnh trung tâm năng khiếu chung chung | **THIẾU** | Bổ sung phân loại môn năng khiếu (Âm nhạc, Hội họa, Kỹ năng/Múa/Cờ vua), phân loại hình thức lớp (1 kèm 1, nhóm nhỏ 3–5, nhóm 8–12), yêu cầu phòng học đặc thù và các biểu mẫu chứng từ giấy hiện tại (Phiếu ghi danh, Biên nhận thu tiền, Sổ điểm danh). |
| **Mục 2.1 - Hình 1** | Sơ đồ Use Case: Các node tên là danh từ (`Quản trị tài khoản`, `Báo cáo và tra cứu`...) | **CẦN SỬA** | Chuẩn hóa tên Use Case theo chuẩn OOAD: **Động từ + Danh từ** (ví dụ: `Quản lý hồ sơ học viên`, `Xếp lịch và mở lớp`, `Đăng ký ghi danh & Thu học phí`, `Điểm danh và nhận xét`, `Tiếp nhận nghỉ & Bố trí học bù`, `Xem báo cáo thống kê`). |
| **Mục 2.2 - Hình 2** | Sơ đồ Workflow chỉ tập trung vào giao dịch thanh toán và sổ chờ | **CẦN SỬA** | Nâng cấp sơ đồ thành Luồng nghiệp vụ tổng thể (End-to-End Business Process) của trung tâm năng khiếu. Phần chi tiết giao dịch thu tiền giữ lại làm luồng con (Sub-process). |
| **Mục 3.1 & 3.2 (Chương 3)** | Sơ đồ miền Hình 3 & Hình 4 chia thành 2 nửa, không có thuộc tính | **CẦN SỬA** | Thêm các thuộc tính cốt lõi của từng lớp (ví dụ: `Student`: studentId, fullName, dob; `ClassGroup`: classId, capacity, fixedFee, status; `Lesson`: date, startTime, endTime; `Receipt`: receiptNo, amount, paymentMethod...). Chuẩn hóa quan hệ theo đúng Conceptual Class Diagram. |
| **Mục 3.3 (Chương 3)** | Kiến trúc 3-tier, chi tiết kỹ thuật CSDL, thuật toán băm mật khẩu | **THỪA** | **Cắt giảm bớt.** Chỉ nêu ngắn gọn định hướng ứng dụng Web nội bộ. Các chi tiết sâu về kiến trúc phân tầng, cài đặt kỹ thuật, database schema để dành cho Đợt 2 (Chương 3 & Chương 4). |
| **Phụ lục B (FR01–FR18)** | 18 FR viết kèm Tiêu chí chấp nhận rất nặng nề theo kiểu kiểm thử | **THỪA / CẦN SỬA** | Tinh gọn lại. Giữ lại mô tả yêu cầu chức năng nghiệp vụ cốt lõi, loại bỏ các chi tiết kiểm thử sâu (chuyển sang phụ lục tóm tắt). |
| **Phụ lục D (NFR01–NFR08)** | NFR viết rất sâu về đo tải 1.000 học viên, UTF-8, băm mật khẩu | **THỪA** | Rút gọn NFR về mức định hướng chất lượng chung của hệ thống phần mềm (tính bảo mật, tính khả dụng, tính toàn vẹn dữ liệu). Bỏ các chỉ số kiểm thử hiệu năng giả định chưa thể đo ở Đợt 1. |
| **Phụ lục E (TC01–TC12)** | Ma trận 12 Test Cases giả định | **THỪA** | Trong Báo cáo Lần 1 (Xác định yêu cầu + Khả thi), Ma trận kiểm thử (Test Cases) là quá sớm. Cần chuyển trọng tâm ma trận này thành **Ma trận truy vết Nghiệp vụ (Business Rule $\leftrightarrow$ Use Case $\leftrightarrow$ Actor)** để giảng viên thấy được tính nhất quán của thiết kế hướng đối tượng. |
| **Chương 5 (Mục 5.3)** | 5 câu hỏi xin góp ý | **CẦN SỬA** | Căn chỉnh 5 câu hỏi khớp chính xác với 5 chương trình bày, kèm hướng dẫn sinh viên trong lớp quét mã QR trên slide/tài liệu để nhập nhận xét. |

---

## IV. ĐÁNH GIÁ CHUYÊN SÂU VỀ PHƯƠNG PHÁP HƯỚNG ĐỐI TƯỢNG (OOAD & UML)

### 1. Về Sơ đồ Use Case (Hình 1):
- Trong OOAD, một **Use Case** đại diện cho một chuỗi hành động mà hệ thống thực hiện mang lại một kết quả có giá trị quan sát được đối với một **Actor**.
- Việc đặt tên `Quản trị tài khoản và danh mục` hay `Báo cáo và tra cứu` là tư duy lập trình cấu trúc/phân chia module chức năng, **không phải tư duy Use Case**.
- **Yêu cầu chỉnh sửa:** Đổi toàn bộ các bong bóng Use Case thành động từ:
  - Thay vì `Quản lý hồ sơ và ghi danh` $\rightarrow$ Tách thành `Đăng ký hồ sơ học viên` và `Ghi danh khóa học`.
  - Thay vì `Thu học phí và chứng từ` $\rightarrow$ `Lập phiếu thu học phí`.
  - Thay vì `Quản lý lớp và lịch` $\rightarrow$ `Xếp thời khóa biểu & Mở lớp`.
  - Thay vì `Duyệt nghỉ và bố trí học bù` $\rightarrow$ `Duyệt đơn nghỉ` và `Bố trí lịch học bù`.

### 2. Về Sơ đồ Miền (Domain Model - Hình 3 & 4):
- Sơ đồ miền ở giai đoạn này chính là **Lược đồ lớp mức khái niệm (Conceptual Class Diagram)**.
- Hai hình hiện tại chỉ có tên hộp và đường nối với các ký hiệu $0..1, 0..*$. Giảng viên không thấy được các thực thể này lưu giữ thông tin gì.
- **Yêu cầu chỉnh sửa:** Đưa thêm 3–5 thuộc tính tiêu biểu vào mỗi thực thể:
  - `Course` (mã khóa, tên môn, cấp độ, số buổi, học phí chuẩn).
  - `ClassGroup` (mã lớp, tên lớp, sĩ số tối đa, trạng thái).
  - `Lesson` (mã buổi, số thứ tự buổi, ngày học, ca học, phòng học, giảng viên).
  - `Enrollment` (mã ghi danh, ngày đăng ký, trạng thái thanh toán).
  - `Receipt` (số phiếu thu, số tiền, ngày thu, hình thức thanh toán).
  - `Attendance` (trạng thái: Có mặt / Vắng phép / Vắng không phép, nhận xét).
  - `MakeupEntitlement` (mã quyền, ngày cấp, hạn sử dụng, trạng thái).

---

## V. ĐÁNH GIÁ MÃ QR & QUY CHẾ TƯƠNG TÁC LỚP HỌC

- **Điểm cộng:** Nhóm đã chủ động tạo link Google Form và chèn thẻ `[[qr:...]]` ngay trang đầu.
- **Cần hoàn thiện:**
  - Cần làm nổi bật cơ chế khuyến khích: Sinh viên/nhóm khác trong lớp có 1 đóng góp được công nhận là hữu ích sẽ được **cộng 5% điểm quá trình (tích lũy tối đa 15%)**.
  - Form thu thập ý kiến phải có trường nhập: Họ tên, MSSV, Nhóm của người góp ý (để giảng viên xác nhận điểm danh và cộng điểm).
  - 5 câu hỏi xin ý kiến ở Chương 5 phải được đánh số và cấu trúc tương ứng đúng 5 phần thuyết trình để người nghe dễ bám sát và phản biện.

---

## VI. BẢN KẾ HOẠCH HÀNH ĐỘNG CỤ THỂ DÀNH CHO MAIN AGENT (ACTION PLAN)

Để đưa báo cáo đạt điểm tối đa (9.5 – 10.0), Main Agent cần thực hiện ngay các chỉnh sửa sau vào file nguồn `report_source.md` và biên dịch lại `.docx`:

1. **Ưu tiên 1 (Nâng cấp nội dung nghiệp vụ & bổ sung đặc thù năng khiếu):**
   - Bổ sung vào Chương 1: Bối cảnh đặc thù của trung tâm năng khiếu (phòng cách âm, đàn piano, giá vẽ, sĩ số nhỏ 1-1 và 3-5), bảng khảo sát hiện trạng thực tế và các biểu mẫu chứng từ giấy mẫu (Phiếu đăng ký, Phiếu thu, Sổ điểm danh).
   - Mở rộng luồng nghiệp vụ tổng thể từ tiếp nhận tư vấn/kiểm tra đầu vào $\rightarrow$ xếp lớp $\rightarrow$ thu phí $\rightarrow$ điểm danh $\rightarrow$ học bù $\rightarrow$ tổng kết.
2. **Ưu tiên 2 (Chuẩn hóa OOAD & UML):**
   - Đổi tên các Use Case trong Hình 1 và Phụ lục C theo quy ước **Động từ + Danh từ**.
   - Bổ sung danh sách thuộc tính khái niệm cho các lớp trong Mô hình miền (Hình 3 & Hình 4).
3. **Ưu tiên 3 (Lược bớt các phần kỹ thuật "nhảy cóc" / thừa thãi):**
   - Rút gọn mục 3.3 (kiến trúc và công nghệ), chuyển định hướng chi tiết sang Đợt 2.
   - Chuyển Phụ lục D (NFR) thành các nguyên tắc chất lượng phần mềm ngắn gọn, loại bỏ các chỉ số đo tải giả định.
   - Thay thế Phụ lục E (12 Test Cases giả định) thành **Ma trận truy vết Nghiệp vụ (Business Traceability Matrix)** liên kết giữa Quy tắc nghiệp vụ (BR) $\leftrightarrow$ Use Case (UC) $\leftrightarrow$ Lớp dữ liệu (Domain Class).
4. **Ưu tiên 4 (Đồng bộ và biên dịch):**
   - Cập nhật script `build_report.py` để cập nhật hình vẽ Mermaid tương ứng nếu cần.
   - Biên dịch lại file Word `SE100_BaoCaoTienDo_Dot1_Scope_SRS.docx`.
