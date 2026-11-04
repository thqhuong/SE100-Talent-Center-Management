# Đưa Harmony lên máy Linux của nhóm

Hướng phụ trách máy chủ, tên miền và quyền truy cập. Cấu hình này dựng web, API NestJS, PostgreSQL và Caddy trên máy Linux có Docker Engine và Compose. PostgreSQL chỉ lắng nghe trong mạng Docker. Caddy nhận lưu lượng HTTPS và chuyển tới web. Hoàng và Đại có thể dùng một bản CSDL thử tách biệt để tập phục hồi.

## Khởi động lần đầu

1. Trỏ bản ghi DNS của tên miền về máy chủ và cho phép lưu lượng đến cổng 80, 443. Clone nhánh `develop` rồi chọn đúng commit mà nhóm đã kiểm tra.
2. Trong thư mục repo, tạo tệp môi trường riêng trên máy chủ. Đặt biến APP_DOMAIN bằng tên miền thật của nhóm.

```sh
umask 077
printf 'APP_DOMAIN=%s\nDB_PASSWORD=%s\n' 'harmony.example.org' "$(openssl rand -hex 32)" > .env.production
docker compose --env-file .env.production -f compose.production.yaml up --build -d --wait
```

Lệnh tạo tệp trên chỉ thực hiện lần đầu. Khi đã có dữ liệu, giữ lại mật khẩu CSDL hiện tại. Bản triển khai này dùng volume riêng, tạo bảng bằng migration và bắt đầu với CSDL trống. Tài khoản và mật khẩu mẫu trong README dành riêng cho bản phát triển.

3. Tạo tài khoản quản lý đầu tiên từ terminal của người quản trị. Ví dụ dưới đây dùng Bash. Tên đăng nhập và mật khẩu do nhóm đặt. Mật khẩu nhập ẩn và không ghi vào lịch sử lệnh.

```bash
read -r -p 'Email quản lý: ' ADMIN_EMAIL
read -r -s -p 'Mật khẩu (tối thiểu 12 ký tự): ' ADMIN_PASSWORD
printf '\n'
export ADMIN_EMAIL ADMIN_PASSWORD
docker compose --env-file .env.production -f compose.production.yaml exec -T -e ADMIN_EMAIL -e ADMIN_PASSWORD api npm run admin:create
unset ADMIN_EMAIL ADMIN_PASSWORD
```

4. Mở tên miền bằng HTTPS, đăng nhập bằng tài khoản vừa tạo và kiểm tra `/api/v1/health`. Chuẩn bị dữ liệu nghiệp vụ cho bản chạy chung theo phần việc của nhóm. Khi cần thay version, sao lưu CSDL, ghi commit đang chạy, cập nhật sang commit đã kiểm tra và chạy lại lệnh Compose.

## Bản sao dữ liệu đầu tiên

Chạy trên máy Linux. Chọn đường dẫn lưu bản sao chỉ người quản trị đọc được.

```bash
umask 077
docker compose --env-file .env.production -f compose.production.yaml exec -T db pg_dump -U harmony -d harmony -Fc > harmony-backup.dump
```

Để thử phục hồi, tạo CSDL thử với tên mới trên máy thử và dùng `pg_restore` vào CSDL đó. Lưu bằng chứng đăng nhập được sau khi khởi động lại. Hoàng sẽ bổ sung kịch bản sao lưu định kỳ và đối chiếu dữ liệu nghiệp vụ khi các chức năng tương ứng đã hoàn thành.
