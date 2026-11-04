# Bộ khởi động của máy chủ

NestJS phục vụ dữ liệu tại `/api/v1`. PostgreSQL lưu tài khoản, phiên đăng nhập, chương trình, lớp, buổi và ghi danh. [Cách chạy bằng Docker](../../README.md).

| Yêu cầu | Kết quả |
| --- | --- |
| GET /health | Kiểm tra kết nối CSDL |
| GET /public/programs | Danh mục công khai |
| POST /auth/login | Kiểm tra email và mật khẩu rồi cấp cookie phiên |
| GET /auth/me, POST /auth/logout | Đọc người đang đăng nhập hoặc kết thúc phiên |
| GET /me/schedule | Lịch trong phạm vi quyền của người dùng |
| GET /me/sessions/:id | Đọc một buổi sau khi kiểm tra quyền trên máy chủ |

Các tệp nghiệp vụ có sẵn trong `src/modules` là bản phác thảo để Khang và Huy đối chiếu với yêu cầu. Luồng đang chạy được kiểm tra qua API ở bảng trên. Khi hiện thực học phí hoặc học bù, chủ luồng phải nối xử lý với PostgreSQL và kiểm tra lại điều kiện khi lưu.

Bản phát triển áp dụng migration rồi nạp dữ liệu mẫu một lần. Bản triển khai Linux dùng migration trên CSDL riêng. Hướng tạo quản lý đầu tiên theo [hướng dẫn tự host](../../deploy/README.md).
