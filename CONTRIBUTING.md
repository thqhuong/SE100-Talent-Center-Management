# Gửi thay đổi cho nhóm SE100

Bắt đầu từ thư mục repo và bảo đảm đã lưu các việc đang làm trên nhánh riêng. Trước khi nhận việc mới:

```powershell
git switch develop
git pull --ff-only
git switch -c feat/student-schedule
```

Đổi `feat/student-schedule` thành tên ngắn mô tả việc bạn nhận. Ví dụ `feat/makeup-options`, `test/late-leave-entry` hoặc `docs/class-diagram`.

## Làm theo một ví dụ có sẵn

Mở màn lịch bằng tài khoản An và xem yêu cầu `GET /api/v1/me/schedule` trong thẻ Network của trình duyệt. Mở phần gọi API trong `project/frontend/src`, tìm đường dẫn tương ứng trong `project/backend/src`, rồi đối chiếu bản ghi lớp và buổi trong `project/backend/prisma`. Khi thêm chức năng, chốt một ví dụ đầu vào, kết quả người dùng nhìn thấy và cách thử khi đăng nhập sai vai trò.

Phần giao diện gọi API theo đường dẫn tương đối `/api/v1`. Máy chủ lấy người đang đăng nhập từ cookie phiên để lọc dữ liệu. Đổi vai trò trong giao diện không cấp quyền mới. Khi thay đổi định dạng dữ liệu trả về, cập nhật cả phần sử dụng trên web và báo người phụ trách luồng đó.

Hướng phụ trách nền tảng, tài khoản và bản tích hợp. Khang chịu trách nhiệm lịch, chỗ học, ghi danh và thu phí. Huy chịu trách nhiệm giáo trình, buổi học, chuyên cần, tiến bộ và học bù. Công việc của Hoàng, Quý, Đại dùng dữ liệu hoặc giao diện đã thống nhất để có thể thực hiện song song.

## Trước khi gửi

1. Chạy thử việc của mình trên Docker bằng dữ liệu chung. Ghi lại tài khoản, thao tác và kết quả để người khác thử lại.
2. Kiểm tra danh sách tệp bằng `git status --short`. Chỉ chọn những tệp thuộc công việc. Ví dụ dưới đây dùng cho một thay đổi giao diện.

```powershell
git add project/frontend/src
git commit -m "feat: show student schedule"
git push -u origin HEAD
```

3. Trên GitHub tạo pull request vào **develop**. Ghi thay đổi có ích gì, cách thử và link minh chứng. Nhờ một người liên quan xem lại. Luồng kiểm tra tự động khởi động ứng dụng với PostgreSQL và thử quyền của hai học viên.
4. Dán link pull request vào phiếu của bạn. Khi kiểm tra đạt và nhóm đã xem, tích hợp vào `develop`. Nhánh `main` dành cho bản ổn định của nhóm.

Khi có thay đổi cấu trúc bảng, thêm migration vào kho cùng code. Dùng một cơ sở dữ liệu phát triển riêng để tạo migration. Quy trình clone mặc định chỉ áp dụng migration đã có và nạp dữ liệu mẫu theo mã cố định.
