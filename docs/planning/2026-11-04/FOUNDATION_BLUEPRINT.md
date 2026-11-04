# Nền dùng chung của nhóm SE100

[Hướng dẫn chạy từ bản clone mới](../../../README.md) · [Phiếu của sáu thành viên](./README.md)

## Bản khởi đầu

Một bộ Docker chạy web React, máy chủ NestJS và PostgreSQL do nhóm tự host. Dữ liệu học kỳ dùng ví dụ chương trình Piano tại trung tâm và Thanh nhạc online, có An và Bình thuộc các lớp khác nhau. Khi kiểm tra quyền, dùng đúng tài khoản học viên và đối chiếu những buổi người đó được ghi danh.

Bộ khởi động cung cấp một luồng mẫu để phát triển tiếp. Code, Figma và báo cáo dùng cùng tên và mối quan hệ giữa học viên, chương trình, lớp, buổi học và ghi danh.

## Luồng sản phẩm cần hoàn thiện

Khách xem chương trình và trao đổi với Giáo vụ. Giáo vụ tư vấn lớp, kiểm tra điều kiện và xác nhận ghi danh cùng học phí. Sau ghi danh, học viên xem lịch, giáo trình và link buổi online theo quyền. Giảng viên chốt buổi được giao và ghi nhận kỹ năng thực tế. Nếu vắng đủ điều kiện, Giáo vụ xác nhận buổi bù, người học thấy lịch mới.

- Hướng phụ trách phiên đăng nhập, quyền theo hồ sơ và buổi, tài khoản sau ghi danh, link riêng, quản trị và máy chủ chung.
- Khang phụ trách hồ sơ tư vấn và lịch lớp, số chỗ/thiết bị tốt, ghi danh trước khai giảng, thu đủ phí và tiền chờ. Chỗ được tính sau khi đã trừ ghi danh chính thức và lịch bù đã xác nhận. Thanh nhạc xét sức chứa người và điều kiện thiết bị âm thanh.
- Huy phụ trách giáo trình gắn với lớp, bài và mục tiêu từng buổi, điểm danh có mặt/vắng, đánh giá Chưa đánh giá / Đang luyện / Đạt, tiếp nhận báo nghỉ qua Giáo vụ và quyền học bù. Sửa sau chốt cần duyệt và giữ lịch sử.
- Nhánh học bù kiểm tra bộ môn và cấp độ, chủ đề tương đương, loại lớp và hình thức tại trung tâm/online, điều kiện chỗ, xung đột lịch, thời lượng và hạn. Huy kiểm tra lại các điều kiện khi lưu bằng cùng quy tắc giữ chỗ của Khang. Lớp 1:1 dùng buổi bù riêng.
- Mỗi lớp online có giảng viên trực tiếp qua Meet/Zoom. Link của buổi chỉ cấp cho người có phân công, ghi danh hoặc lịch bù hiệu lực. Người dùng bên ngoài xem thông tin công khai của chương trình.
- Hoàng, Quý và Đại làm song song dữ liệu mở rộng, phân tích, báo cáo và kiểm thử. Hướng, Huy và Khang tự cung cấp chức năng cùng dữ liệu cơ bản để hoàn thành các luồng chính.

Các sơ đồ và ví dụ trong báo cáo cần mô tả đúng phiên bản đã chạy. Phần thực tế đã nghiệm thu ghi bằng đường dẫn, dữ liệu thử, người kiểm tra và ngày kiểm tra.
