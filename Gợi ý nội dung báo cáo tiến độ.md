# Gợi ý nội dung báo cáo tiến độ - SE100 (OOAD)

## 1. Yêu cầu chung
- **Mã QR đóng góp**: Đầu trang/slide báo cáo phải chứa mã QR để thu thập đóng góp (feedback/góp ý, không phải khảo sát yêu cầu) từ các nhóm / sinh viên khác trong lớp.
- **Thông tin sinh viên tham gia**: Ghi nhận thông tin sinh viên có mặt tại lớp tham gia đóng góp (đóng góp cá nhân hoặc theo nhóm đều được).
- **Thứ tự câu hỏi**: Các câu hỏi thu thập đóng góp được sắp xếp theo thứ tự phù hợp với nội dung trình bày.
- **Chia sẻ cho Giảng viên**: Chia sẻ liên kết kết quả đóng góp cho giảng viên; với những đóng góp nhóm đánh giá là hữu ích thì cần đánh dấu nổi bật.
- **Cơ chế điểm cộng**: Sinh viên / nhóm có 1 đóng góp được công nhận là hữu ích sẽ được **cộng 5% số điểm** (tích lũy tối đa 3 lần = **15%**).

---

## 2. Gợi ý nội dung trình bày lúc báo cáo

### Lần 1: Xác định yêu cầu đề tài + Tính khả thi
*(Ví dụ tham khảo: Đề tài "Tiệm cầm đồ")*
1. **Khái niệm & Bối cảnh nghiệp vụ**:
   - Hoạt động nghiệp vụ cốt lõi là gì?
   - Mức độ phạm vi tổ chức (cá nhân, hộ gia đình, cửa hàng tư nhân 1 chi nhánh, chuỗi nhiều chi nhánh, doanh nghiệp...).
2. **Đối tượng tham gia (Actors & Objects)**:
   - Các đối tượng con người chính tham gia vào hoạt động (Chủ tiệm, khách hàng, nhân viên...)?
   - Đối tượng vật chất / tài sản phát sinh? Thuộc tính và dữ liệu cần thu thập là gì?
3. **Phạm vi & Nhu cầu phần mềm**:
   - Xác định phạm vi đề tài nhóm thực hiện $\rightarrow$ Mô tả hiện trạng tổ chức, quy trình hiện tại.
   - Lý do cần xây dựng phần mềm? Người dùng sử dụng nhằm mục đích gì?
4. **Luồng nghiệp vụ & Tương tác (Business Workflows)**:
   - Tương tác giữa các đối tượng (Tham khảo $\rightarrow$ Liên hệ $\rightarrow$ Thẩm định/Đánh giá $\rightarrow$ Thỏa thuận $\rightarrow$ Tạo giao dịch $\rightarrow$ Đóng lãi định kỳ $\rightarrow$ Chuộc đồ sớm/đúng/trễ hạn $\rightarrow$ Báo cáo thống kê).
5. **Ràng buộc, Biến động & Kịch bản ngoại lệ (Constraints & Edge Cases)**:
   - Trong quá trình tương tác có phụ thuộc đối tượng nào?
   - Ràng buộc thời gian, ràng buộc dữ liệu, phạm vi giá trị thuộc tính, tính pháp lý?
   - Các kịch bản ngoại lệ nếu không thực hiện đúng luồng lý tưởng (Happy Path vs. Exceptional Paths)?
   - Các thuộc tính đối tượng biến đổi theo thời gian ra sao?

---

### Lần 2: Thiết kế giao diện (Bản vẽ thô / Prototype / Frontend) & Khung báo cáo
*(Khung chuẩn cấu trúc các chương trong cuốn báo cáo)*

#### Chương 1. Tổng quan đề tài
- **1.1. Hiện trạng**: Khảo sát thực tế, khó khăn của quy trình thủ công.
- **1.2. Giới thiệu đề tài**: Mô tả chi tiết đề tài, giới hạn phạm vi, các biểu mẫu chứng từ và quy định nghiệp vụ.

#### Chương 2. Phân tích (Analysis)
- **Sơ đồ Use Case tổng quát**: Chỉ thể hiện các nghiệp vụ lớn.
- **2.1. Mô tả nghiệp vụ 1**:
  - Use Case chi tiết của nghiệp vụ 1.
  - Sơ đồ Activity / Sequence đặc tả chi tiết nghiệp vụ và thuyết minh đặc tả cho từng sơ đồ.
- **2.2. Mô tả nghiệp vụ 2**:
  - Tương tự nghiệp vụ 1.
  - *(Lưu ý: Chỉ chọn các chức năng cốt lõi chính để vẽ đặc tả chi tiết, không cần vẽ dàn trải toàn bộ).*

#### Chương 3. Thiết kế (Design)
- **3.1. Thiết kế cơ sở dữ liệu**: Sơ đồ ERD, mô hình quan hệ hoặc lược đồ NoSQL.
- **3.2. Thiết kế giao diện**:
  - Sơ đồ liên kết các màn hình / giao diện (Screen Flow / Navigation Map).
  - *3.2.1. Thiết kế giao diện nghiệp vụ chính 1*: Bản vẽ giao diện (Mockup/Wireframe/Figma) và đặc tả chi tiết thành phần.
  - *3.2.2. Thiết kế giao diện nghiệp vụ chính 2*: Tương ứng các nghiệp vụ chính đã phân tích ở Chương 2.
- **3.3. Thiết kế lớp / Thiết kế đối tượng (Class Design)**:
  - Sơ đồ Class Diagram chi tiết (thuộc tính, kiểu dữ liệu, phương thức, quan hệ).
  - Thuyết minh đặc tả từng lớp.
- **3.4. Thiết kế kiến trúc (Architecture Design)**:
  - Sơ đồ kiến trúc tổng thể (Layered Architecture, MVC/MVVM...) và thuyết minh.

#### Chương 4. Xây dựng và triển khai ứng dụng (Implementation)
- **4.1. Tổng quan công nghệ**: Giới thiệu ngắn gọn các công nghệ sử dụng (Ngôn ngữ, Framework, Database...).
- **4.2. Sơ đồ thành phần (Component Diagram)**.
- **4.3. Sơ đồ triển khai (Deployment Diagram)**.
- **4.4. Bảng phân công công việc**: Ma trận trách nhiệm (RACI / Work Breakdown) của từng thành viên trong nhóm.

#### Chương 5. Tổng kết
- **5.1. Kết quả đạt được**:
  - Mô tả chi tiết kết quả đã hoàn thành so với mục tiêu đề ra.
  - Link Source code (GitHub/GitLab mở quyền truy cập cho Giảng viên).
  - Link Video Demo sản phẩm (không giới hạn thời gian, mở public/unlisted cho GV truy cập).
  - Thông tin liên hệ sinh viên phụ trách quản lý mã nguồn và video (để Khoa/GV liên hệ khi cần).
- **5.2. Ưu khuyết điểm** (của phần mềm đã xây dựng).
- **5.3. Hướng phát triển** (tính năng mở rộng trong tương lai).

#### Tài liệu tham khảo & Phụ lục
- Danh mục tài liệu tham khảo theo chuẩn học thuật.
- **Phụ lục**: Diễn giải tập các ký hiệu và quy tắc dùng để vẽ các sơ đồ UML.
