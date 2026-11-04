# Dương Nguyễn Phú Quý

**SE100 · 24521489 · Đặc tả nghiệp vụ, sơ đồ và ca kiểm thử**

[Mở phiếu Word](../PhanCong_Word/05_DuongNguyenPhuQuy.docx) · [Lịch chung](../MILESTONES.md)

Bạn viết Chương 2 để người đọc hiểu trung tâm làm việc như thế nào. Mỗi nghiệp vụ cần có người thực hiện, các bước, kết quả đúng và ví dụ để nhóm thử lại.

## Mở bản mẫu

Bộ khởi động có dữ liệu về An, Bình, lớp và lịch. Bạn có thể viết kết quả mong đợi bằng giấy, bảng hoặc Markdown ngay cả khi chức năng đang được xây dựng.

Sau khi clone nhánh develop, mở Docker Desktop và chạy docker compose up --build -d --wait trong thư mục se100. Mở http://localhost:3000. [Hướng dẫn bắt đầu](../../../../README.md).

## Việc đầu tiên

Chọn nghiệp vụ báo nghỉ. Viết ba tình huống gồm báo đúng ngưỡng, báo muộn và vắng tại buổi bù. Mỗi tình huống ghi thời gian, người nhập, hành động và kết quả cần thấy.

## An báo đúng giờ nhưng Giáo vụ nhập muộn

An có buổi Piano lúc 18:00 thứ Ba. An báo nghỉ lúc 18:00 thứ Hai. Giáo vụ nhập lại thông tin lúc 09:00 thứ Ba. Giảng viên chốt An vắng sau buổi học.

**Biết đã xong khi** Bảng tình huống phải tách giờ An thực báo khỏi giờ Giáo vụ nhập. Với ngưỡng 24 giờ và đủ căn cứ, kết quả mong đợi là một quyền bù cho buổi gốc.

## Phối hợp với nhóm

Đưa ví dụ cho Huy để tham khảo. Khi chức năng có thể chạy, bạn thực hiện lại các bước và điền thêm kết quả thực tế. Các sơ đồ và bài kiểm tra có thể phát triển trên nhánh riêng.

## Sáu mốc bàn giao

Chốt lúc **22:00 giờ Việt Nam**. Khi người nhận đã thử lại kết quả, đánh dấu và dán đường dẫn.

| Hạn | Việc cần giao | Dấu hiệu đã xong | Người nhận | Link kết quả |
| --- | --- | --- | --- | --- |
| 08/11 | Mô tả ba tình huống báo nghỉ và kết quả mong đợi. | Mỗi ví dụ có người thao tác, giờ thực báo, giờ nhập và kết quả khi chốt điểm danh. | Huy | … |
| 12/11 | Giao đặc tả bốn luồng chính, sơ đồ tổng quát và bộ ca thử đầu tiên. | Bao phủ mở lớp, ghi danh, theo dõi buổi học và nghỉ bù. Mỗi luồng có một đường thành công và một ngoại lệ. | Hướng và Đại | … |
| 22/11 | Vẽ sơ đồ các bước và thứ tự trao đổi giữa người dùng với hệ thống. | Dùng cùng tên lớp, buổi, phiếu và quyền bù như trong bộ mẫu. Đối chiếu ít nhất một ca với ứng dụng. | Huy và Khang | … |
| 29/11 | Ghép Chương 2 từ đặc tả các luồng và ví dụ hiện hành. | Mỗi sơ đồ có thuyết minh dễ đọc. Ghi nhận góp ý ngày 27/11 để điều chỉnh phần liên quan. | Đại | … |
| 06/12 | Chạy bộ ca thử và bổ sung bằng chứng. | Ghi cả mong đợi và thực tế. Nếu sai, đưa tên tài khoản, mã buổi, các bước và cách lặp lại lỗi. | Chủ chức năng | … |
| 11/12 | Giao Chương 2 và bảng ca thử cuối. | Người khác có thể lặp lại ba ca báo nghỉ và đối chiếu đúng kết quả. Các sơ đồ khớp bản chạy. | Đại và Hướng | … |

Figma sẵn sàng từ 13/11 cho buổi trình bày 27/11. Bộ nộp sẵn sàng từ 12/12 cho hạn cuối kỳ tạm tính 26/12/2026.
