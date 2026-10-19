# Sơ đồ báo cáo tiến độ lần 1 SE100

Nguồn Mermaid và ảnh biểu diễn cùng tập tác nhân, nghiệp vụ và quan hệ. Bội số là số bản ghi lịch sử; điều kiện hiệu lực do BR quy định.

## use_cases

```mermaid
flowchart LR
  M["Quản lý"]
  O["Giáo vụ"]
  T["Giảng viên"]
  subgraph SYS["Phần mềm quản lý trung tâm năng khiếu"]
    A(["Quản trị tài khoản và danh mục"])
    B(["Xử lý khoản chờ và sửa sai chứng từ"])
    C(["Hồ sơ, ghi danh và thu học phí"])
    D(["Quản lý lớp và xếp lịch"])
    E(["Duyệt nghỉ và bố trí học bù"])
    F(["Xem lịch, điểm danh và nhận xét"])
    G(["Tra cứu và báo cáo theo phạm vi quyền"])
  end
  M --- A
  M --- B
  M --- F
  O --- C
  O --- D
  O --- E
  O --- G
  T --- F
  T --- G
  M --|> O
```

## workflow

```mermaid
flowchart LR
  A["Mở lớp và xếp đủ lịch"] --> B["Lập ghi danh Chờ thanh toán"]
  B --> C{"Còn hợp lệ trước nhận tiền?"}
  C -->|"Hợp lệ"| D["Nhận tiền và xác nhận thu"]
  C -->|"Không hợp lệ"| X["Chọn lớp khác"]
  X --> B
  D --> E{"Lưu hợp lệ và thành công?"}
  E -->|"Có"| F["Phiếu thu và kích hoạt ghi danh cùng giao dịch"]
  E -->|"Không, đã nhận tiền"| P["Ghi sổ tiền chờ xử lý"]
  P --> Q["Quản lý xác nhận ghi nhận lại hoặc trả tiền thủ công"]
  Q -->|"Đã trả lại"| R["Đối chiếu báo cáo học phí và tiền chờ"]
  Q -->|"Ghi nhận lại đủ điều kiện"| F
  F --> G["Học theo lịch và chốt điểm danh"]
  G --> R
  G -->|"Vắng có phép đã duyệt"| H["Tạo quyền bù, bố trí và chốt lượt bù"]
  H --> R
```

## domain_finance

```mermaid
classDiagram
  direction LR
  Course "1" -- "0..*" ClassGroup
  ClassGroup "1" -- "0..*" Enrollment
  Student "1" -- "0..*" Enrollment
  Enrollment "1" -- "0..*" Receipt
  Enrollment "1" -- "0..*" PaymentIncident
  Receipt "0..1" -- "0..1" PaymentIncident : linked after resolution
```

## domain_learning

```mermaid
classDiagram
  direction LR
  ClassGroup "1" -- "0..*" Lesson
  Room "1" -- "0..*" Lesson
  Instructor "1" -- "0..*" Lesson
  Enrollment "1" -- "0..*" Attendance
  Lesson "1" -- "0..*" Attendance
  Attendance "1" -- "0..1" MakeupEntitlement
  MakeupEntitlement "1" -- "0..*" MakeupBooking
  Lesson "1" -- "0..*" MakeupBooking
  Enrollment "1" -- "0..*" LeaveRequest
  Lesson "1" -- "0..*" LeaveRequest
```