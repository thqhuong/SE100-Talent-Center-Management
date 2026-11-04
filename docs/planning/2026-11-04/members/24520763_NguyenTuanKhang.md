# Nguyễn Tuấn Khang

**SE100 · 24520763 · Mở lớp, kiểm tra chỗ và thu học phí**

[Mở phiếu Word](../PhanCong_Word/03_NguyenTuanKhang.docx) · [Lịch chung](../MILESTONES.md)

Bạn làm hành trình của Giáo vụ từ lúc khách hỏi lớp đến khi ghi danh, thu phí và phát phiếu thu. Bạn trực tiếp viết phần quản lý phòng, lịch, sức chứa và xử lý tiền để đi hết luồng.

## Mở bản mẫu

Bộ khởi động có chương trình Piano, Thanh nhạc, lớp tại trung tâm, lớp online và mẫu ghi danh. Bạn dùng dữ liệu cơ bản này để viết quy tắc mở lớp và nhận học viên.

Sau khi clone nhánh develop, mở Docker Desktop và chạy docker compose up --build -d --wait trong thư mục se100. Mở http://localhost:3000. [Hướng dẫn bắt đầu](../../../../README.md).

## Việc đầu tiên

Lấy lớp Piano mẫu và giả sử phòng chỉ còn một đàn tốt chưa dùng. Viết xuống kết quả khi có hai người muốn ghi danh cùng lúc. Gửi Huy quy tắc tính chỗ chung cho ghi danh và học bù.

## Hai người cùng muốn lấy chỗ cuối

Một phòng có năm chỗ Piano. Đã có bốn học viên chính thức. Hai Giáo vụ cùng xác nhận chỗ còn lại. Một người đã thực nhận tiền từ khách.

**Biết đã xong khi** Chỉ một ghi danh được tạo. Nếu đã nhận tiền nhưng khách chưa có chỗ, Giáo vụ tra được tiền chờ. Gửi lại cùng yêu cầu thì mở đúng chứng từ cũ.

## Phối hợp với nhóm

Bạn cùng Hướng và Huy làm Figma. Bạn dẫn từ khách xem chương trình qua tư vấn, chọn lớp đến phiếu thu. Bạn sở hữu cả cách kiểm tra chỗ lẫn giao dịch thay đổi tiền.

## Sáu mốc bàn giao

Chốt lúc **22:00 giờ Việt Nam**. Khi người nhận đã thử lại kết quả, đánh dấu và dán đường dẫn.

| Hạn | Việc cần giao | Dấu hiệu đã xong | Người nhận | Link kết quả |
| --- | --- | --- | --- | --- |
| 08/11 | Chốt dữ liệu cần khi mở lớp và ghi danh. Vẽ luồng của quầy Giáo vụ. | Một ví dụ có số chỗ lớp, chỗ phòng và nhạc cụ tốt. Huy dùng được quy tắc trừ chỗ của buổi bù. | Huy và Hướng | … |
| 12/11 | Hoàn thành phần tiếp nhận và học phí trong Figma. | Bấm được từ hỏi lớp tới phiếu thu, rồi thử nhánh lớp đầy và tra lại phiếu. Ghép được vào luồng chung. | Hướng và Huy | … |
| 22/11 | Mở lớp, kiểm tra lịch và thu đủ học phí trên cơ sở dữ liệu thật. | Đủ điều kiện mới ghi danh và phát phiếu. Hướng nhận được mã ghi danh, Huy đọc được số chỗ còn lại. | Hướng và Huy | … |
| 29/11 | Hoàn thiện đổi lịch, dạy thay, tiền chờ và xử lý sau duyệt. | Buổi thay thế không bị đếm hai lần. Phân bổ tiền chờ không tăng thu lần nữa. Trình bày phần quầy 27/11. | Hướng | … |
| 06/12 | Thử tranh chỗ cuối và gửi lặp sau mất mạng. | Hai yêu cầu đồng thời chỉ một lượt lấy chỗ. Số tiền trên phiếu, khoản chờ và báo cáo khớp nhau. | Đại | … |
| 11/12 | Bàn giao luồng lớp, lịch, học phí và phần viết cho báo cáo. | Tự mở lớp và nhận học viên trên server nhóm. Gửi ví dụ, ảnh, phiếu đối chiếu và kết quả thử. | Hướng và Đại | … |

Figma sẵn sàng từ 13/11 cho buổi trình bày 27/11. Bộ nộp sẵn sàng từ 12/12 cho hạn cuối kỳ tạm tính 26/12/2026.
