# Bắt đầu với Harmony

Harmony là đồ án SE100 về quản lý một trung tâm âm nhạc. Bản khởi động có danh mục chương trình, đăng nhập và lịch học cá nhân. Mỗi bạn chạy ứng dụng và cơ sở dữ liệu ngay trên máy mình.

## Lần đầu chạy trên Windows

1. Hướng mời bạn vào kho GitHub riêng. Mở lời mời và chấp nhận bằng đúng tài khoản GitHub của bạn.
2. Cài Git và Docker Desktop. Mở Docker Desktop, đợi Docker Engine báo đang chạy.
3. Mở PowerShell tại thư mục muốn lưu bài và chạy ba lệnh sau.

```powershell
git clone --branch develop https://github.com/thqhuong/SE100-Talent-Center-Management.git se100
cd se100
docker compose up --build -d --wait
```

4. Mở **[ứng dụng trên máy bạn](http://localhost:3000)**. Lần đầu Docker cần tải các gói phần mềm. Đợi các dịch vụ báo sẵn sàng rồi mới mở trình duyệt.

### Thử trong hai phút

Mở danh mục và tìm **Piano** và **Thanh nhạc**. Đăng nhập bằng An, xem lịch rồi đăng xuất. Làm lại bằng Bình. An có buổi tại trung tâm, Bình có buổi online. Hai người xem hai danh sách khác nhau dù dùng cùng một máy chủ.

Tất cả tài khoản dưới đây dùng mật khẩu `HarmonyDemo2026!` **trên bản phát triển ở máy cá nhân**.

| Người dùng thử | Email |
| --- | --- |
| Quản lý | `manager@harmony.test` |
| Giáo vụ | `staff@harmony.test` |
| Giảng viên | `teacher@harmony.test` |
| Học viên An | `an@harmony.test` |
| Học viên Bình | `binh@harmony.test` |

## Bắt đầu việc của mình

Mở [phiếu Word của sáu thành viên](./docs/planning/2026-11-04/README.md) và đọc phần **việc đầu tiên**. Hướng, Huy và Khang làm Figma cùng các luồng chính. Hoàng chuẩn bị dữ liệu mở rộng và sao lưu. Quý viết đặc tả và tình huống kiểm thử. Đại phụ trách hướng dẫn, kiểm thử người dùng và báo cáo cuối kỳ.

| Bạn muốn làm gì? | Mở ở đâu? |
| --- | --- |
| Sửa chữ hoặc cách hiển thị trên web | [Giao diện React](./project/frontend/src/) |
| Tìm đoạn máy chủ kiểm tra người đăng nhập và trả lịch | [Máy chủ NestJS](./project/backend/src/) |
| Xem các bảng, thay đổi CSDL và bộ dữ liệu ví dụ | [Dữ liệu PostgreSQL](./project/backend/prisma/) |
| Tạo nhánh, gửi phần mình làm để nhóm kiểm tra | [Cách làm việc nhóm](./CONTRIBUTING.md) |
| Đưa bản chung lên máy Linux của nhóm | [Hướng dẫn triển khai](./deploy/README.md) |

Từ thư mục `se100`, dừng ứng dụng bằng `docker compose stop`. Mở lại bằng `docker compose up -d --wait`. Dữ liệu nằm trong volume riêng của Docker và còn sau khi dừng dịch vụ. Khi nhóm thay đổi thư viện hoặc cấu trúc dữ liệu, cập nhật nhánh rồi chạy lại lệnh có `--build`. Khi sửa tệp trong hai thư mục `src`, bản phát triển sẽ tự tải lại.

### Nếu chưa mở được trang

- **GitHub báo không tìm thấy kho.** Mở lời mời của Hướng và kiểm tra tài khoản đang đăng nhập vào Git.
- **Docker báo không kết nối được engine.** Mở Docker Desktop, chọn Linux containers rồi thử `docker info`.
- **Cổng 3000 đang bận.** Trong PowerShell chạy `$env:WEB_PORT='3002'`, chạy lại lệnh khởi động và mở `http://localhost:3002`.
- **Một dịch vụ chưa sẵn sàng.** Chạy `docker compose ps -a` rồi `docker compose logs --tail=50 init api web`. Dịch vụ `init` kết thúc với mã 0 là bình thường vì việc của nó là tạo bảng và nạp dữ liệu mẫu.

## Các mốc chung

Figma bàn giao trước **22:00 ngày 12/11/2026**, sẵn sàng từ 13/11 cho buổi trình bày 27/11. Bộ đồ án bàn giao trước **22:00 ngày 11/12/2026**, sẵn sàng từ 12/12 cho hạn cuối kỳ **tạm tính** 26/12. [Lịch và đầu ra theo giai đoạn](./docs/planning/2026-11-04/MILESTONES.md).
