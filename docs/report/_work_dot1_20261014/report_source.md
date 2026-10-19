# BÁO CÁO TIẾN ĐỘ ĐỢT 1 — MÔN HỌC SE100
## PHẦN MỀM QUẢN LÝ TRUNG TÂM DẠY NĂNG KHIẾU

### DANH SÁCH THÀNH VIÊN NHÓM THỰC HIỆN

| STT | Họ và tên thành viên | MSSV | Vai trò |
| --- | --- | --- | --- |
| 1 | Trần Hữu Quốc Hướng | 24520644 | Trưởng nhóm |
| 2 | Nguyễn Tuấn Khang | 24520763 | Thành viên |
| 3 | Nguyễn Lê Đức Huy | 24520680 | Thành viên |
| 4 | Dương Nguyễn Phú Quý | 24521489 | Thành viên |
| 5 | Nguyễn Văn Hoàng | 23520355 | Thành viên |
| 6 | Đào Phúc Đại | 24520244 | Thành viên |

> **Tóm tắt phương án đề xuất:** Xây dựng ứng dụng web nội bộ phục vụ vận hành cho một chi nhánh trung tâm dạy năng khiếu với ba tác nhân trực tiếp: Quản lý, Giáo vụ, Giảng viên; quản lý lớp học theo khóa trọn gói có số buổi cố định. Luồng nghiệp vụ cốt lõi bao gồm: tư vấn xếp lớp, ghi danh, thu học phí trọn gói một lần, lập thời khóa biểu chống trùng phòng học và giảng viên, điểm danh kèm nhận xét chuyên môn và điều phối lịch học bù. Báo cáo này là kết quả khảo sát thực tế và phân tích sơ bộ đặc thù trung tâm năng khiếu; các quy tắc nghiệp vụ sẽ tiếp tục được tinh chỉnh chi tiết trong giai đoạn thiết kế.

<!-- page -->
# MỤC LỤC
[[TOC]]

<!-- page -->
# CHƯƠNG 1: TỔNG QUAN ĐỀ TÀI
## 1.1. Bối cảnh và hoạt động cốt lõi

Trung tâm dạy năng khiếu là mô hình đào tạo ngoài giờ chính khóa, chuyên giảng dạy các bộ môn nghệ thuật, thể chất và phát triển tư duy cho đối tượng chủ yếu là thiếu nhi, học sinh và thanh thiếu niên từ 4 đến 18 tuổi. Hoạt động đào tạo tại trung tâm được phân thành ba nhóm bộ môn chính:

* **Nghệ thuật âm nhạc:** Piano, Guitar, Violin, Organ, Thanh nhạc, Trống. Đặc thù đòi hỏi phòng học cách âm chuyên dụng và trang bị nhạc cụ cố định cho từng học viên.
* **Mỹ thuật và hội họa:** Vẽ màu nước, vẽ chì tĩnh vật, hội họa sáng tạo, điêu khắc đất sét. Đặc thù đòi hỏi phòng học có ánh sáng tiêu chuẩn, giá vẽ và khu vực vệ sinh dụng cụ chuyên dụng.
* **Kỹ năng và thể chất:** Cờ vua tư duy, múa Ballet hoặc hiện đại, võ thuật, kỹ năng dẫn chương trình. Đặc thù đòi hỏi không gian sàn tập rộng có gương, thảm đệm hoặc bàn cờ tiêu chuẩn.

Về quy mô và hình thức tổ chức, trung tâm triển khai giảng dạy theo ba mô hình lớp học đặc thù:

1. **Lớp cá nhân 1 kèm 1:** Sĩ số tối đa 01 học viên, thường áp dụng cho bộ môn Piano cổ điển hoặc luyện thi năng khiếu chuyên sâu, mức học phí cao và lịch học đòi hỏi theo dõi sát sao.
2. **Lớp nhóm nhỏ:** Sĩ số từ 03 đến 05 học viên, đảm bảo giảng viên kèm cặp trực tiếp từng học viên trong các môn Thanh nhạc, Guitar hoặc Hội họa.
3. **Lớp nhóm tiêu chuẩn:** Sĩ số từ 08 đến 12 học viên, áp dụng cho các môn Múa, Cờ vua hoặc Mỹ thuật cơ bản.

Qua khảo sát hiện trạng quản lý thủ công bằng sổ sách giấy kết hợp bảng tính Excel tại các cơ sở đào tạo năng khiếu, nhóm nhận thấy ba bất cập lớn thường xuyên xảy ra:

* **Xung đột tài nguyên phòng học và giảng viên:** Do số lượng lớp nhiều, sĩ số mỗi lớp nhỏ và khung giờ học tập trung cao điểm vào buổi tối hoặc cuối tuần, việc xếp lịch thủ công trên Excel rất dễ dẫn đến tình trạng hai lớp bị xếp trùng một phòng chuyên dụng hoặc một giảng viên bị phân công trùng ca dạy.
* **Quá tải trong quản lý nghỉ phép và xếp lịch học bù:** Học viên nhỏ tuổi thường xuyên nghỉ đột xuất vì lý do sức khỏe hoặc trùng lịch thi ở trường phổ thông. Việc tiếp nhận xin nghỉ qua tin nhắn rời rạc khiến giáo vụ khó kiểm soát số buổi vắng hợp lệ, dẫn đến xếp lịch học bù chồng chéo, gây vượt quá sức chứa phòng học như trường hợp phòng chỉ có 5 cây đàn Piano nhưng nhận tới 6 học viên và phát sinh tranh chấp về quyền lợi buổi học.
* **Rủi ro sai lệch tài chính và đối soát học phí:** Thu học phí trọn gói bằng tiền mặt hoặc chuyển khoản nhưng thiếu sự gắn kết chặt chẽ giữa trạng thái giữ chỗ ghi danh và phiếu thu dẫn đến nhầm lẫn giữa học viên đã đóng phí và học viên mới đăng ký chờ thanh toán, gây khó khăn khi đối chiếu doanh thu cuối kỳ.

## 1.2. Phạm vi và nhu cầu phần mềm

Nhóm đề xuất xây dựng phần mềm quản lý dưới dạng ứng dụng web nội bộ phục vụ cho một chi nhánh trung tâm dạy năng khiếu. Hệ thống tập trung giải quyết bài toán quản lý lớp học theo khóa trọn gói có số buổi cố định *N* buổi, thu học phí đủ một lần trước khi khai giảng, kiểm soát thời khóa biểu chống trùng lặp, điểm danh chuyên cần kèm nhận xét năng khiếu từng buổi và điều phối quyền học bù minh bạch.

**Bảng 1.1: Phân định ranh giới phạm vi của phần mềm trong phiên bản đầu**

| Trong phạm vi phiên bản đầu | Ngoài phạm vi phiên bản đầu |
| --- | --- |
| Quản lý hồ sơ học viên, thông tin phụ huynh bảo trợ; quản lý danh mục môn học, cấp độ, khung khóa học, phòng học chuyên dụng và giảng viên. | Quản lý mô hình chuỗi đa chi nhánh; cổng thông tin hoặc ứng dụng di động riêng cho phụ huynh và học viên tự đăng nhập. |
| Mở lớp học, lập thời khóa biểu chi tiết từng buổi; tự động kiểm tra và ngăn chặn xung đột phòng học, giảng viên và lịch học của học viên. | Thuật toán tự động sinh thời khóa biểu tối ưu bằng trí tuệ nhân tạo; quản lý chi tiết khấu hao và bảo trì từng nhạc cụ, thiết bị. |
| Tiếp nhận ghi danh; thu học phí trọn gói một lần bằng tiền mặt hoặc chuyển khoản; lập phiếu thu nội bộ và quản lý sổ theo dõi các khoản tiền chờ xử lý. | Thu học phí chia nhỏ nhiều đợt, thẻ học theo buổi tích điểm, mã khuyến mãi phức tạp, tích hợp cổng thanh toán trực tuyến hoặc hóa đơn điện tử. |
| Điểm danh từng buổi học, ghi nhận xét tiến bộ năng khiếu; tiếp nhận và duyệt đơn xin nghỉ phép, cấp quyền học bù và xếp lịch học bù đúng môn, đúng cấp độ. | Tính lương và hoa hồng tự động cho giảng viên; chính sách bảo lưu học phí dài hạn nhiều tháng; tự động hoàn trả tiền qua hệ thống ngân hàng. |
| Báo cáo thống kê sĩ số lớp, tỷ lệ chuyên cần của học viên, doanh thu học phí thực thu và danh sách các khoản tiền chờ xử lý. | Tích hợp gửi thông báo tự động qua tin nhắn SMS hoặc Zalo; phân tích dự báo năng lực học tập bằng trí tuệ nhân tạo. |

**Danh mục các biểu mẫu, chứng từ nghiệp vụ cần tin học hóa:**

1. **Phiếu đăng ký ghi danh:** Ghi nhận thông tin học viên, thông tin phụ huynh hoặc người giám hộ gồm họ tên, số điện thoại, ghi chú kết quả tư vấn và đánh giá đầu vào, môn học, cấp độ và lớp học đăng ký.
2. **Phiếu thu học phí nội bộ:** Chứng từ xác nhận số tiền thực thu, ngày giờ thu, phương thức thanh toán bằng Tiền mặt hoặc Chuyển khoản, mã giao dịch đối chiếu, nhân viên lập phiếu và lớp học được kích hoạt.
3. **Phiếu điểm danh và sổ theo dõi tiến độ:** Bảng ghi nhận trạng thái hiện diện gồm Có mặt, Vắng có phép, Vắng không phép kèm theo nhận xét chuyên môn của giảng viên cho từng học viên sau mỗi buổi học.
4. **Phiếu hẹn học bù:** Chứng từ xác nhận lịch học bù hợp lệ gồm môn học, cấp độ, lớp học đích, phòng học, giảng viên, ngày giờ được cấp từ một buổi vắng có phép còn trong thời hạn quy định.

## 1.3. Mục tiêu cần kiểm chứng

Phần mềm hướng tới giải quyết triệt để và có thể kiểm chứng được ba mục tiêu nghiệp vụ cốt lõi sau:

1. **Chống vượt sĩ số và loại trừ hoàn toàn xung đột thời khóa biểu:** Đảm bảo không xảy ra tình trạng trùng phòng học, trùng giảng viên, trùng lịch học của học viên hoặc vượt quá sức chứa vật lý của phòng học chuyên dụng tại bất kỳ khung giờ nào.
2. **Đảm bảo tính toàn vẹn và minh bạch tài chính:** Mỗi hồ sơ ghi danh chính thức có hiệu lực đều gắn liền với đúng một phiếu thu học phí hợp lệ; mọi khoản tiền thực tế đã nhận nhưng gặp sự cố khi lưu hệ thống đều phải được ghi nhận vào sổ theo dõi tiền chờ xử lý để Quản lý đối soát, không bị thất thoát hoặc tính trùng.
3. **Chuẩn hóa quy trình nghỉ phép và học bù:** Tách biệt rõ ràng giữa dữ liệu điểm danh tại lớp học gốc và kết quả tham dự buổi học bù; mỗi buổi vắng có phép hợp lệ chỉ sinh tối đa một quyền học bù và chỉ được sử dụng một lần duy nhất trong thời hạn cho phép.

<!-- page -->
# CHƯƠNG 2: PHÂN TÍCH YÊU CẦU VÀ NGHIỆP VỤ
## 2.1. Tác nhân và phân quyền sử dụng

Trong phạm vi phiên bản đầu, hệ thống có ba tác nhân trực tiếp đăng nhập và thao tác trên phần mềm: **Quản lý**, **Giáo vụ** và **Giảng viên**. Học viên và Phụ huynh đóng vai trò là đối tượng thụ hưởng dịch vụ và tham gia nghiệp vụ gián tiếp thông qua sự hỗ trợ của nhân viên Giáo vụ tại quầy tiếp đón.

[[diagram:use_cases.png|Hình 2.1: Sơ đồ Use Case tổng quát thể hiện các tác nhân và nhóm ca sử dụng của hệ thống]]

**Bảng 2.1: Mô tả vai trò, trách nhiệm và giới hạn quyền hạn của các tác nhân**

| Vai trò tác nhân | Trách nhiệm nghiệp vụ và giới hạn quyền sử dụng |
| --- | --- |
| **Quản lý** | Quản trị tài khoản người dùng; thiết lập danh mục môn học, cấp độ, khóa học mẫu, biểu phí và phòng học; phê duyệt xử lý các khoản tiền chờ và phát hành phiếu thu thay thế khi có sai sót hành chính; duyệt điều chỉnh điểm danh có lưu vết; xem toàn bộ báo cáo doanh thu và chuyên cần. |
| **Giáo vụ** | Tiếp nhận và quản lý hồ sơ học viên; mở lớp tuyển sinh và lập thời khóa biểu; thực hiện ghi danh và lập phiếu thu học phí; tiếp nhận đơn xin nghỉ phép và bố trí lịch học bù; tra cứu sĩ số và danh sách lớp. Không có quyền tự ý sửa hoặc xóa phiếu thu đã xác nhận. |
| **Giảng viên** | Tra cứu lịch giảng dạy cá nhân; thực hiện điểm danh và ghi nhận xét chuyên môn cho học viên trong các buổi học được phân công; theo dõi lịch sử chuyên cần của lớp mình phụ trách. Không có quyền truy cập dữ liệu học phí hoặc can thiệp vào lịch học của lớp khác. |

Xét theo tư duy hướng đối tượng, tác nhân **Quản lý** kế thừa toàn bộ quyền hạn nghiệp vụ của **Giáo vụ**, đồng thời sở hữu thêm các đặc quyền quản trị danh mục, kiểm soát tài chính và xử lý ngoại lệ theo quy tắc BR04.

## 2.2. Luồng nghiệp vụ tổng thể từ đầu đến cuối

Hoạt động vận hành tại trung tâm năng khiếu diễn ra theo một chu trình nghiệp vụ khép kín gồm 5 giai đoạn nối tiếp nhau:

1. **Tư vấn và Mở lớp:** Giáo vụ khởi tạo lớp học từ khung chương trình khóa học mẫu, lập lịch đủ *N* buổi học tương ứng với phòng học chuyên dụng và giảng viên có chuyên môn phù hợp. Khi phụ huynh đến liên hệ, Giáo vụ tư vấn bộ môn, kết hợp ghi chú kết quả kiểm tra năng khiếu đầu vào nếu có vào hồ sơ học viên và tạo bản ghi đăng ký ghi danh ở trạng thái Chờ thanh toán.
2. **Thu học phí và Kích hoạt ghi danh:** Giáo vụ kiểm tra điều kiện chỗ trống của lớp, nhận đủ 100% học phí trọn khóa bằng tiền mặt hoặc chuyển khoản và xác nhận thu phí trên hệ thống. Phần mềm thực hiện tạo phiếu thu nội bộ và chuyển trạng thái ghi danh sang Có hiệu lực trong cùng một giao dịch cơ sở dữ liệu nguyên tử.
3. **Tổ chức buổi học và Điểm danh chuyên môn:** Đến ngày học, Giảng viên phụ trách mở danh sách học viên của buổi học gồm học viên chính thức và học viên đăng ký học bù, ghi nhận trạng thái hiện diện và nhập nhận xét đánh giá sự tiến bộ năng khiếu cho từng em. Sau khi buổi học kết thúc, Giảng viên thực hiện chốt điểm danh chính thức.
4. **Xử lý nghỉ học và Điều phối học bù:** Khi học viên bận đột xuất, phụ huynh thông báo trước giờ học để Giáo vụ lập và duyệt đơn xin nghỉ. Khi Giảng viên chốt điểm danh với trạng thái Vắng có phép, hệ thống tự động cấp một Quyền học bù có thời hạn sử dụng. Giáo vụ tra cứu các buổi học tương đương cùng môn, cùng cấp độ, còn chỗ trống để xếp lịch học bù cho học viên trước khi hết hạn.
5. **Đối soát và Báo cáo định kỳ:** Cuối tuần hoặc cuối tháng, Quản lý và Giáo vụ trích xuất báo cáo sĩ số lớp, thống kê tỷ lệ chuyên cần và đối chiếu sổ thu học phí cùng danh sách các khoản tiền chờ xử lý để đánh giá hiệu quả hoạt động.

[[diagram:workflow.png|Hình 2.2: Sơ đồ luồng nghiệp vụ ghi danh, thu học phí, xử lý khoản tiền chờ và điều phối học bù]]

> **Quy trình xử lý ngoại lệ khi giao dịch thu tiền gặp sự cố:** Trong trường hợp nhân viên Giáo vụ đã nhận tiền thực tế từ phụ huynh nhưng thao tác lưu phiếu thu trên hệ thống thất bại do rớt mạng đột xuất hoặc vừa bị người khác chiếm chỗ trống cuối cùng của lớp, Giáo vụ lập tức ghi nhận thông tin vào sổ theo dõi khoản tiền chờ xử lý PaymentIncident kèm mã biên nhận tạm. Sau đó, Quản lý sẽ kiểm tra đối chứng để kích hoạt bổ sung ghi danh nếu lớp được mở rộng hoặc chuyển sang lớp tương đương, hoặc xác nhận hoàn trả tiền mặt thủ công có lưu vết minh bạch.

## 2.3. Ràng buộc nghiệp vụ và kịch bản ngoại lệ

**Bảng 2.2: Tổng hợp các ràng buộc nghiệp vụ trọng yếu và phương án xử lý ngoại lệ**

| Ràng buộc nghiệp vụ | Kịch bản ngoại lệ và giải pháp xử lý trên phần mềm |
| --- | --- |
| **Kiểm soát sĩ số và tranh chấp chỗ cuối** | Sĩ số thực tế của một buổi học bằng tổng số học viên chính thức của lớp cộng với số lượt học bù được xếp vào buổi đó. Con số này không được vượt quá sĩ số tối đa của lớp và sức chứa vật lý của phòng học. Khi hai nhân viên cùng bấm xác nhận thu phí cho một chỗ trống cuối cùng, hệ thống dùng khóa giao dịch chỉ cho phép một giao dịch thành công; giao dịch còn lại được chuyển sang quy trình ghi nhận khoản tiền chờ xử lý để đổi lớp hoặc hoàn tiền. |
| **Loại trừ xung đột thời khóa biểu** | Hai khung giờ học [BắtĐầu_A, KếtThúc_A] và [BắtĐầu_B, KếtThúc_B] trong cùng một ngày được xác định là xung đột khi BắtĐầu_A < KếtThúc_B và BắtĐầu_B < KếtThúc_A. Hệ thống kiểm tra nghiêm ngặt điều kiện này tại thời điểm lưu đối với cả ba đối tượng: Phòng học, Giảng viên và Học viên. Hai ca học nối tiếp liền kề nhau như ca 1 kết thúc lúc 18:30 và ca 2 bắt đầu lúc 18:30 được coi là hợp lệ. |
| **Hủy hoặc dời lịch buổi học** | Lịch học của một buổi chỉ được phép thay đổi hoặc hủy bỏ trước thời điểm bắt đầu buổi học đó. Đối với lớp học đang trong quá trình giảng dạy, việc hủy một buổi học do sự cố bắt buộc phải đi kèm thao tác tạo một buổi học bù thay thế tương ứng cho cả lớp để đảm bảo tổng số buổi cam kết *N* buổi không bị thiếu hụt. |
| **Nghỉ phép và cấp quyền học bù** | Điểm danh lớp gốc có 3 trạng thái: Có mặt, Vắng có phép, Vắng không phép. Trạng thái Vắng có phép chỉ hợp lệ khi đã có đơn xin nghỉ được Giáo vụ phê duyệt trước khi chốt điểm danh. Mỗi buổi vắng có phép chỉ sinh ra tối đa 01 quyền học bù có hạn sử dụng trong vòng 30 ngày. Nếu học viên tiếp tục vắng mặt tại buổi đi học bù, quyền bù đó được tính là hết lượt và tuyệt đối không sinh thêm quyền bù mới. |
| **Tính bất biến của chứng từ và nhật ký sửa đổi** | Phiếu thu học phí sau khi phát hành không được phép sửa số tiền hoặc xóa bỏ khỏi cơ sở dữ liệu nhằm phòng chống gian lận. Nếu ghi nhận sai hình thức thanh toán do nhầm giữa Tiền mặt và Chuyển khoản, Quản lý thực hiện nghiệp vụ phát hành phiếu thu thay thế có liên kết tham chiếu đến phiếu cũ. Kết quả điểm danh đã chốt chỉ được sửa khi nhập lý do giải trình và được hệ thống lưu vết lịch sử đầy đủ. |

## 2.4. Vòng đời và sự biến đổi trạng thái của đối tượng

**Bảng 2.3: Chu kỳ vòng đời và quy tắc chuyển đổi trạng thái của các thực thể cốt lõi**

| Thực thể đối tượng | Chu kỳ vòng đời và điều kiện chuyển trạng thái |
| --- | --- |
| **Lớp học** | **Dự kiến** → **Mở tuyển sinh** khi đã xếp đủ *N* buổi học hợp lệ → **Đang học** khi đến giờ bắt đầu của buổi học đầu tiên → **Hoàn thành** khi toàn bộ *N* buổi học đã kết thúc và hoàn tất chốt điểm danh. |
| **Ghi danh** | **Chờ thanh toán** là hồ sơ đăng ký tạm, không giữ chỗ cứng, tự hủy nếu quá giờ khai giảng → **Có hiệu lực** ngay khi lập phiếu thu học phí thành công → **Hoàn thành** khi lớp học kết thúc khóa. |
| **Buổi học** | **Đã lên lịch** → **Hoàn thành** sau khi giờ học kết thúc và giảng viên chốt điểm danh, hoặc **Đã hủy** nếu giáo vụ thực hiện hủy buổi học trước giờ bắt đầu và tạo buổi học thay thế. |
| **Quyền học bù** | **Chờ bố trí** sinh ra khi chốt vắng có phép → **Đã bố trí** khi xếp thành công vào một buổi học đích → **Đã sử dụng** khi hoàn tất điểm danh buổi học bù, hoặc **Hết hạn** sau 30 ngày kể từ ngày kết thúc lớp gốc mà chưa sử dụng. |
| **Phiếu thu** | **Hiệu lực** ngay khi phát hành → **Được thay thế** khi Quản lý lập phiếu thu điều chỉnh thông tin hành chính, giữ nguyên số tiền và ngày thu gốc. |

<!-- page -->
# CHƯƠNG 3: MÔ HÌNH MIỀN VÀ ĐỊNH HƯỚNG THIẾT KẾ
## 3.1. Các lớp đối tượng khái niệm và dữ liệu cần thu thập

Mô hình miền của hệ thống được thiết kế theo phương pháp hướng đối tượng, phản ánh đầy đủ các thực thể vật lý, giao dịch tài chính và hồ sơ học vụ tại trung tâm năng khiếu:

**Bảng 3.1: Danh mục các lớp thực thể miền và thuộc tính khái niệm cốt lõi**

| Lớp đối tượng | Các thuộc tính khái niệm cốt lõi | Ý nghĩa nghiệp vụ trong hệ thống |
| --- | --- | --- |
| **Account** | accountId, username, passwordHash, role: Manager, Staff, Instructor, isActive | Quản lý thông tin định danh đăng nhập, trạng thái hoạt động và phân quyền truy cập hệ thống. |
| **Student** | studentId, fullName, dateOfBirth, gender, parentName, parentPhone, parentEmail, address, note | Lưu trữ thông tin học viên, thông tin phụ huynh giám hộ và ghi chú tư vấn, năng khiếu đầu vào. |
| **Course** | courseId, courseName, category: Music, Art, Skill, level, defaultLessons, standardTuition | Khung chương trình đào tạo chuẩn theo từng bộ môn, cấp độ năng khiếu, số buổi và học phí chuẩn. |
| **ClassGroup** | classId, className, courseId, maxCapacity, currentCapacity, fixedTuition, status | Lớp học cụ thể được mở tuyển sinh từ một khóa học với sĩ số tối đa và mức học phí chốt trọn gói. |
| **Lesson** | lessonId, classId, lessonNumber, date, startTime, endTime, roomId, instructorId, status | Một buổi học cụ thể thuộc lớp học với ngày giờ, phòng học chuyên dụng và giảng viên xác định. |
| **Room** | roomId, roomName, capacity, roomType: Piano, Art, Dance, Chess, isAvailable | Phòng học chuyên dụng với sức chứa vật lý tối đa và loại trang thiết bị phục vụ bộ môn tương ứng. |
| **Instructor** | instructorId, accountId, fullName, phone, specialization, isActive | Hồ sơ giảng viên hoặc huấn luyện viên phụ trách giảng dạy theo danh mục bộ môn chuyên môn. |
| **Enrollment** | enrollmentId, studentId, classId, registrationDate, agreedTuition, status | Hồ sơ đăng ký ghi danh của một học viên vào một lớp học cụ thể kèm mức học phí cam kết. |
| **Receipt** | receiptId, receiptNumber, enrollmentId, amount, paymentDate, paymentMethod, cashierId, replacedByReceiptId, status | Phiếu thu học phí nội bộ ghi nhận khoản tiền thực tế đã thu và liên kết thay thế chứng từ nếu có. |
| **PaymentIncident** | incidentId, enrollmentId, amountReceived, receivedDate, evidenceRef, resolutionNote, status | Bản ghi sổ theo dõi khoản tiền đã nhận thực tế nhưng gặp sự cố chưa kích hoạt được ghi danh. |
| **LeaveRequest** | requestId, enrollmentId, lessonId, requestDate, reason, approvedBy, status: Pending, Approved, Rejected | Đơn xin nghỉ phép của học viên trước giờ học, làm căn cứ hợp lệ để ghi nhận vắng có phép. |
| **Attendance** | attendanceId, enrollmentId, lessonId, status: Present, Excused, Unexcused, teacherFeedback | Bản ghi kết quả điểm danh chuyên cần và nhận xét chuyên môn của giảng viên tại lớp học gốc. |
| **MakeupEntitlement** | entitlementId, attendanceId, issueDate, expiryDate, status: Pending, Booked, Used, Expired | Quyền học bù phát sinh tự động từ một bản ghi điểm danh vắng có phép hợp lệ. |
| **MakeupBooking** | bookingId, entitlementId, targetLessonId, attendanceStatus: Present, Absent, note | Lượt đăng ký học bù xếp học viên vào một buổi học đích còn chỗ trống của lớp tương đương. |

[[diagram:domain_finance.png|Hình 3.1: Sơ đồ mô hình miền phân hệ Quản lý ghi danh và Thu học phí]]

## 3.2. Mô hình lịch học, điểm danh và điều phối học bù

[[diagram:domain_learning.png|Hình 3.2: Sơ đồ mô hình miền phân hệ Quản lý lịch học, Điểm danh, Nghỉ phép và Học bù]]

Trong mô hình thiết kế của nhóm, mỗi lớp học ClassGroup bao gồm một danh sách cố định *N* buổi học Lesson đang hoạt động. Mỗi buổi học được tổ chức tại một phòng học chuyên dụng Room và do một giảng viên Instructor trực tiếp đứng lớp. Khi phụ huynh xin nghỉ trước giờ học, Giáo vụ ghi nhận thông qua thực thể LeaveRequest.

Điểm nhấn quan trọng trong kiến trúc dữ liệu này là sự **tách biệt hoàn toàn giữa điểm danh lớp gốc Attendance và lượt tham dự học bù MakeupBooking**:

* Attendance chỉ gắn với Enrollment và Lesson của lớp học gốc mà học viên đăng ký.
* Khi Attendance có trạng thái Vắng có phép, hệ thống sinh ra một MakeupEntitlement. Từ quyền bù này, Giáo vụ tạo MakeupBooking trỏ tới một buổi học đích thuộc lớp học khác cùng môn và cùng cấp độ.
* Thiết kế này giúp bảo toàn dữ liệu lịch sử của cả hai lớp: báo cáo chuyên cần của lớp gốc không bị sửa đè khi học viên đi học bù, đồng thời sĩ số thực tế tại buổi học của lớp nhận học bù vẫn được kiểm soát chặt chẽ để không vượt quá số lượng nhạc cụ hoặc chỗ ngồi của phòng học.

## 3.3. Định hướng thiết kế chi tiết cho Đợt 2

Dựa trên nền tảng yêu cầu và mô hình miền khái niệm đã thống nhất ở Đợt 1, nhóm xác lập kế hoạch triển khai kỹ thuật cho báo cáo Đợt 2 bao gồm ba hạng mục chính:

1. **Thiết kế giao diện người dùng:** Xây dựng bản mẫu giao diện trực quan và sơ đồ luồng màn hình cho 04 không gian làm việc trọng tâm: Quầy tiếp đón ghi danh và thu học phí; Bảng lập thời khóa biểu kiểm tra xung đột trực quan; Màn hình điểm danh và nhận xét năng khiếu dành cho giảng viên; Màn hình tra cứu và điều phối học bù.
2. **Thiết kế hành vi hướng đối tượng:** Đặc tả chi tiết Sơ đồ hoạt động và Sơ đồ tuần tự cho các ca sử dụng cốt lõi, làm rõ cơ chế khóa giao dịch chống trùng chỗ cuối và tự động cấp quyền học bù.
3. **Thiết kế lớp chi tiết và cơ sở dữ liệu:** Chuyển đổi mô hình miền khái niệm sang Lược đồ lớp thiết kế đầy đủ kiểu dữ liệu, phạm vi truy cập và phương thức xử lý; đồng thời thiết kế Lược đồ cơ sở dữ liệu quan hệ và kiến trúc phân tầng phục vụ giai đoạn lập trình.

<!-- page -->
# CHƯƠNG 4: ĐÁNH GIÁ TÍNH KHẢ THI VÀ KẾ HOẠCH THỰC HIỆN
## 4.1. Đánh giá tính khả thi của dự án

**Bảng 4.1: Phân tích tính khả thi của đề tài theo bốn khía cạnh**

| Khía cạnh đánh giá | Phân tích tính khả thi | Điều kiện đảm bảo thực hiện thành công |
| --- | --- | --- |
| **Nghiệp vụ** | Đề tài bám sát bài toán thực tế tại các trung tâm đào tạo nghệ thuật, năng khiếu, giải quyết trực diện vấn đề trùng phòng học chuyên dụng và rối loạn quản lý học bù. Việc giới hạn phạm vi trong 01 chi nhánh và thu phí trọn gói giúp quy trình nghiệp vụ cô đọng, rõ ràng và chặt chẽ. | Tham khảo biểu mẫu phiếu thu, sổ điểm danh và nội quy học bù thực tế tại các trung tâm năng khiếu để chuẩn hóa dữ liệu đầu vào. |
| **Kỹ thuật** | Sử dụng kiến trúc ứng dụng web phân tầng kết hợp hệ quản trị cơ sở dữ liệu quan hệ hỗ trợ giao dịch tin cậy. Thuật toán kiểm tra giao thoa khoảng thời gian và cơ chế khóa bản ghi kèm mã chống gửi lặp hoàn toàn khả thi với các công nghệ phổ biến hiện nay. | Xây dựng bộ kịch bản kiểm thử tự động và kiểm thử đồng thời cho hai luồng nhạy cảm: Thu học phí chỗ cuối và Xếp lịch phòng học. |
| **Nhân lực** | Nhóm gồm 06 thành viên có nền tảng lập trình hướng đối tượng và cơ sở dữ liệu, được phân chia phụ trách chuyên sâu theo từng phân hệ và áp dụng quy trình rà soát chéo nghiêm túc. | Duy trì họp nhóm định kỳ hàng tuần để đồng bộ mô hình thiết kế và giải quyết sớm các điểm nghẽn kỹ thuật. |
| **Thời gian và chi phí** | Quy mô 18 yêu cầu chức năng và 05 nhóm Use Case trọng tâm hoàn toàn phù hợp với thời lượng một học kỳ môn SE100. Dự án sử dụng các công cụ và thư viện mã nguồn mở nên không phát sinh chi phí bản quyền hay hạ tầng. | Bám sát tiến độ 03 cột mốc của môn học: Đợt 1 về Phạm vi và yêu cầu → Đợt 2 về Bản mẫu giao diện và thiết kế UML → Cuối kỳ về Cài đặt, kiểm thử và vấn đáp. |

## 4.2. Kế hoạch phân công công việc và rà soát chéo

**Bảng 4.2: Ma trận phân công nhiệm vụ và kiểm soát chất lượng chéo giữa các thành viên**

| Thành viên phụ trách | Phân hệ và đầu ra công việc chịu trách nhiệm chính | Thành viên rà soát chéo |
| --- | --- | --- |
| **Trần Hữu Quốc Hướng - Trưởng nhóm** | Quản lý phạm vi tổng thể, kiến trúc hệ thống, chuẩn hóa văn bản báo cáo và điều phối thuyết trình. | Nguyễn Tuấn Khang |
| **Nguyễn Tuấn Khang** | Phân hệ Lớp học và Thời khóa biểu: Đặc tả tác nhân, phân quyền hệ thống, sơ đồ Use Case tổng quát và quy tắc kiểm soát xung đột lịch học từ BR01 đến BR04. | Dương Nguyễn Phú Quý |
| **Nguyễn Lê Đức Huy** | Phân hệ Ghi danh và Thu học phí: Đặc tả luồng nghiệp vụ ghi danh, lập phiếu thu, xử lý khoản tiền chờ từ BR05 đến BR08 và thiết kế biểu mẫu chứng từ tài chính. | Nguyễn Văn Hoàng |
| **Dương Nguyễn Phú Quý** | Phân hệ Điểm danh và Học bù: Đặc tả quy trình duyệt nghỉ phép, chốt điểm danh, nhận xét chuyên môn và điều phối quyền học bù từ BR09 đến BR11. | Nguyễn Lê Đức Huy |
| **Nguyễn Văn Hoàng** | Phân hệ Mô hình dữ liệu và Báo cáo: Xây dựng sơ đồ mô hình miền, từ điển thuộc tính thực thể và đặc tả các báo cáo đối soát theo quy tắc BR12. | Đào Phúc Đại |
| **Đào Phúc Đại** | Phân hệ Đảm bảo chất lượng và Truy vết: Xây dựng ràng buộc chất lượng hệ thống, ma trận truy vết nghiệp vụ và các kịch bản xử lý ngoại lệ. | Trần Hữu Quốc Hướng |

<!-- page -->
# CHƯƠNG 5: KẾT QUẢ ĐẠT ĐƯỢC VÀ ĐỊNH HƯỚNG TIẾP THEO
## 5.1. Kết quả đạt được trong Đợt 1

1. **Xác lập ranh giới phạm vi rõ ràng:** Phân định cụ thể các chức năng thực hiện trong phiên bản đầu và các tính năng tạm lược bỏ cho mô hình trung tâm năng khiếu một chi nhánh, giúp dự án tập trung vào chiều sâu nghiệp vụ thay vì dàn trải.
2. **Chuẩn hóa bộ quy tắc nghiệp vụ chặt chẽ:** Xây dựng hoàn chỉnh 12 quy tắc nghiệp vụ cốt lõi từ BR01 đến BR12, giải quyết thấu đáo các bài toán thực tế như: chống trùng lịch phòng học và giảng viên, xử lý tranh chấp chỗ trống cuối cùng, quản lý sổ tiền chờ xử lý và tách bạch điểm danh lớp gốc với học bù.
3. **Hoàn thiện mô hình miền hướng đối tượng:** Xây dựng bộ 04 sơ đồ phân tích trực quan gồm Sơ đồ Use Case tổng quát, Sơ đồ luồng nghiệp vụ, Mô hình miền Ghi danh và Tài chính, Mô hình miền Lịch học, Điểm danh và Học bù cùng từ điển 14 lớp thực thể đồng bộ.
4. **Chuẩn bị sẵn sàng bộ câu hỏi phản biện:** Tổng hợp 05 câu hỏi trọng tâm tại Phụ lục F nhằm tiếp nhận ý kiến đóng góp từ Giảng viên và sinh viên để hoàn thiện báo cáo Đợt 2.

## 5.2. Nhận diện rủi ro và biện pháp xử lý

**Bảng 5.1: Các rủi ro tiềm ẩn và phương án phòng ngừa, giảm thiểu**

| Rủi ro nhận diện | Biện pháp phòng ngừa và hướng xử lý |
| --- | --- |
| **Chính sách học bù ngoài thực tế có nhiều biến tướng phức tạp** | Giữ vững nguyên tắc chuẩn hóa trong phạm vi đồ án: chỉ cấp quyền học bù khi có đơn xin nghỉ được duyệt trước giờ học và chỉ xếp vào buổi học tương đương còn chỗ trống trong hạn 30 ngày. Trường hợp không bố trí được lịch phù hợp, hệ thống giữ trạng thái chờ để Quản lý xử lý ngoại lệ, không tự động tính toán hoàn tiền lẻ. |
| **Xung đột dữ liệu khi nhiều giáo vụ thao tác đồng thời tại quầy** | Thực thi kiểm tra toàn bộ điều kiện ràng buộc tại tầng máy chủ và áp dụng giao dịch cơ sở dữ liệu nguyên tử kèm khóa bản ghi khi xác nhận thu học phí hoặc xếp lịch học bù vào chỗ trống cuối cùng. |
| **Áp lực khối lượng thiết kế UML và bản mẫu ở Đợt 2** | Ưu tiên hoàn thiện dứt điểm bản vẽ giao diện và Sơ đồ tuần tự cho hai luồng nghiệp vụ xương sống: Ghi danh, Thu học phí và Điểm danh, Xếp lịch học bù trước khi mở rộng sang các màn hình danh mục và báo cáo. |

<!-- page -->
# TÀI LIỆU THAM KHẢO

1. Khoa Công nghệ Phần mềm, Trường Đại học Công nghệ Thông tin – ĐHQG-HCM (2026). *Đề cương chi tiết môn học Phương pháp phát triển phần mềm hướng đối tượng SE100*.
2. Giảng viên phụ trách môn học SE100 (2026). *Tài liệu hướng dẫn nội dung báo cáo tiến độ và khung tiêu chuẩn đánh giá đồ án môn học*.
3. Bộ môn Kỹ thuật Phần mềm, Trường Đại học Công nghệ Thông tin – ĐHQG-HCM (2026). *Tài liệu nghiên cứu tình huống mẫu: Phân tích và thiết kế hướng đối tượng hệ thống quản lý thư viện*.
4. Nhóm thực hiện đề tài SE100 (2026). *Báo cáo khảo sát sơ bộ quy trình nghiệp vụ và biểu mẫu quản lý tại các trung tâm đào tạo năng khiếu nghệ thuật*.

<!-- page -->
# PHỤ LỤC A: DANH MỤC QUY TẮC NGHIỆP VỤ
## A.1. Nhóm quy tắc quản lý lớp học, thời khóa biểu và ghi danh

Hệ thống 12 quy tắc nghiệp vụ từ BR01 đến BR12 đóng vai trò là nền tảng logic chi phối toàn bộ quá trình phân tích và thiết kế phần mềm:

* **BR01 — Đơn vị vận hành và chuẩn thời khóa biểu:** Hệ thống vận hành cho một chi nhánh duy nhất, sử dụng múi giờ chuẩn Việt Nam `Asia/Ho_Chi_Minh` và đơn vị tiền tệ Đồng Việt Nam `VND`. Mỗi lớp học ClassGroup lưu cố định mức học phí trọn khóa và tổng số buổi học *N* buổi tại thời điểm khởi tạo, không bị biến động tự động khi thay đổi biểu giá danh mục sau đó. Để chuyển sang trạng thái Mở tuyển sinh, lớp học bắt buộc phải được xếp đủ *N* buổi học hợp lệ. Khi hủy một buổi học lẻ của lớp đang diễn ra, Giáo vụ bắt buộc phải tạo kèm một buổi học thay thế tương ứng trong cùng một giao dịch. Khi xếp lịch, hệ thống bắt buộc kiểm tra phòng học và giảng viên phải đúng chuyên môn bộ môn của lớp.
* **BR02 — Kiểm soát sĩ số lớp và sức chứa phòng học:** Chỉ những hồ sơ ghi danh ở trạng thái Có hiệu lực mới chính thức chiếm một suất trong sĩ số lớp; hồ sơ Chờ thanh toán không giữ chỗ cứng. Sĩ số thực tế tại một buổi học cụ thể được tính bằng tổng số học viên chính thức của lớp, bao gồm cả học viên xin nghỉ phép buổi đó, cộng với số lượng học viên học bù được xếp vào buổi học này. Tổng số này tuyệt đối không được vượt quá sĩ số tối đa của lớp học `maxCapacity` và sức chứa vật lý tối đa của phòng học chuyên dụng `capacity`.
* **BR03 — Loại trừ xung đột thời khóa biểu:** Hai buổi học diễn ra trong cùng một ngày được coi là xung đột thời gian khi thời điểm bắt đầu của buổi thứ nhất sớm hơn thời điểm kết thúc của buổi thứ hai và thời điểm bắt đầu của buổi thứ hai sớm hơn thời điểm kết thúc của buổi thứ nhất (`BắtĐầu_A < KếtThúc_B` và `BắtĐầu_B < KếtThúc_A`). Hệ thống tự động kiểm tra và chặn xung đột lịch tại thời điểm lưu dữ liệu đối với cả ba thực thể: Phòng học, Giảng viên và Học viên. Các buổi học ở trạng thái Đã hủy không chiếm giữ tài nguyên thời gian.
* **BR04 — Nguyên tắc kiểm soát phân quyền theo vai trò:** Mọi yêu cầu nghiệp vụ đều phải được kiểm tra quyền hạn tại tầng máy chủ. Giảng viên chỉ được phép xem lịch dạy và thực hiện điểm danh, nhận xét cho đúng các buổi học mình được phân công phụ trách. Giáo vụ thực hiện quản lý hồ sơ, lập lịch, ghi danh, thu phí và xếp lịch học bù nhưng không có quyền sửa đổi phiếu thu đã phát hành. Quản lý kế thừa toàn bộ quyền của Giáo vụ, đồng thời nắm quyền quản trị danh mục, xử lý sổ tiền chờ và phê duyệt điều chỉnh chứng từ, điểm danh có lưu vết.
* **BR05 — Quy định tiếp nhận ghi danh và kích hoạt:** Học viên chỉ được phép đăng ký vào lớp học đang ở trạng thái Mở tuyển sinh và trước giờ bắt đầu của buổi học đầu tiên. Mỗi học viên chỉ có tối đa một hồ sơ ghi danh đang hoạt động tại một lớp học. Sau khi nhận đủ học phí, hệ thống kiểm tra lại điều kiện chỗ trống của lớp rồi mới chuyển trạng thái ghi danh sang Có hiệu lực. Khi lớp học đã bắt đầu buổi học đầu tiên, chuyển sang trạng thái Đang học, hệ thống tự động khóa chức năng tiếp nhận ghi danh mới vào lớp đó.
* **BR06 — Chính sách chốt và thu học phí trọn gói:** Mức học phí cần thu được chốt cố định theo mức học phí của lớp học tại thời điểm tạo hồ sơ ghi danh. Trong phạm vi phiên bản đầu, hệ thống yêu cầu thu đủ 100% học phí trọn khóa trong một lần thanh toán duy nhất; không hỗ trợ thu trả góp nhiều đợt, ghi nợ học phí hoặc áp dụng chồng chéo nhiều mã giảm giá tự động.

## A.2. Nhóm quy tắc thu học phí, điểm danh và điều phối học bù

* **BR07 — Tính nguyên tử của giao dịch thu phí và xử lý sự cố:** Thao tác tạo phiếu thu học phí Receipt và cập nhật trạng thái ghi danh Enrollment sang Có hiệu lực bắt buộc phải thực thi trong cùng một giao dịch cơ sở dữ liệu nguyên tử, cùng thành công hoặc cùng hủy bỏ hoàn toàn. Mỗi yêu cầu xác nhận thu tiền đều đính kèm mã định danh chống gửi lặp. Trường hợp nhân viên đã nhận tiền thực tế từ phụ huynh nhưng giao dịch hệ thống bị từ chối do hết chỗ đồng thời hoặc lỗi kết nối, nhân viên phải lập tức ghi nhận vào sổ theo dõi khoản tiền chờ xử lý PaymentIncident kèm thông tin biên nhận tạm. Chỉ Quản lý mới có thẩm quyền phê duyệt xử lý khoản tiền chờ này: hoặc kích hoạt vào lớp phù hợp, hoặc xác nhận đã hoàn trả tiền thủ công cho phụ huynh.
* **BR08 — Nguyên tắc bất biến của chứng từ tài chính:** Phiếu thu học phí sau khi đã phát hành trên hệ thống tuyệt đối không được chỉnh sửa số tiền hoặc xóa vật lý khỏi cơ sở dữ liệu. Nếu phát sinh sai sót về thông tin hành chính như chọn nhầm phương thức thanh toán giữa Tiền mặt và Chuyển khoản hoặc sai ghi chú, Quản lý được phép lập một Phiếu thu thay thế tham chiếu trực tiếp tới mã phiếu thu cũ, chuyển phiếu cũ sang trạng thái Được thay thế, nhưng bắt buộc phải giữ nguyên mã hồ sơ ghi danh, số tiền thực thu và ngày thu gốc.
* **BR09 — Quy định quản lý buổi học và thời điểm chốt điểm danh:** Giảng viên chỉ được phép bấm chốt điểm danh chính thức sau khi thời gian của buổi học đã kết thúc theo lịch. Mỗi học viên chính thức trong lớp chỉ có duy nhất một bản ghi kết quả điểm danh cho mỗi buổi học. Việc dời lịch hoặc hủy buổi học chỉ hợp lệ khi thực hiện trước giờ bắt đầu buổi học. Các buổi học ở trạng thái Đã hủy không phát sinh dữ liệu điểm danh và không tính vào mẫu số thống kê chuyên cần.
* **BR10 — Phân loại trạng thái chuyên cần và điều kiện sinh quyền học bù:** Điểm danh tại lớp học gốc gồm ba trạng thái: Có mặt, Vắng có phép và Vắng không phép. Học viên vắng mặt chỉ được ghi nhận là Vắng có phép khi có đơn xin nghỉ LeaveRequest được Giáo vụ phê duyệt trước thời điểm chốt điểm danh buổi học đó. Mỗi bản ghi điểm danh Vắng có phép chỉ tự động sinh ra tối đa 01 Quyền học bù MakeupEntitlement. Đối với học viên đi học bù, kết quả tham dự MakeupBooking chỉ ghi nhận hai trạng thái là Có mặt hoặc Vắng; trường hợp học viên vắng mặt tại buổi học bù thì quyền học bù đó xem như đã sử dụng hết và không được cấp lại quyền bù mới.
* **BR11 — Tiêu chí và thời hạn bố trí lịch học bù:** Buổi học đích được chọn để xếp học bù phải thỏa mãn đồng thời 05 điều kiện: cùng bộ môn năng khiếu; cùng cấp độ đào tạo; còn chỗ trống khả dụng theo quy tắc BR02; không gây trùng lịch học hiện tại của học viên theo quy tắc BR03; diễn ra trước ngày hết hạn của quyền học bù. Thời hạn hiệu lực của quyền học bù là 30 ngày kể từ ngày kết thúc dự kiến của lớp học gốc. Trường hợp lớp học gốc có sự thay đổi dẫn đến lùi ngày kết thúc khóa học, ngày hết hạn của các quyền học bù chưa sử dụng thuộc lớp đó sẽ được hệ thống tự động gia hạn tương ứng.
* **BR12 — Lưu vết lịch sử và bảo toàn dữ liệu tham chiếu:** Các bản ghi danh mục và hồ sơ đã phát sinh giao dịch nghiệp vụ liên quan như học viên đã từng ghi danh, phòng học hoặc giảng viên đã từng được xếp lịch dạy tuyệt đối không được xóa vật lý mà chỉ được chuyển sang trạng thái ngưng hoạt động. Mọi thao tác nhạy cảm bao gồm: điều chỉnh điểm danh đã chốt, phát hành phiếu thu thay thế, xử lý khoản tiền chờ và hủy hoặc dời lịch học đều bắt buộc người thực hiện phải nhập lý do giải trình và được hệ thống tự động lưu vết gồm người thao tác, thời gian, giá trị cũ, giá trị mới vào nhật ký kiểm toán.

<!-- page -->
# PHỤ LỤC B: DANH MỤC YÊU CẦU CHỨC NĂNG
## B.1. Phân hệ Quản trị hệ thống, Danh mục và Tuyển sinh

* **FR01 — Đăng nhập và kiểm soát phiên làm việc:** Cho phép người dùng đăng nhập bằng tài khoản được cấp, tự động xác thực và phân quyền giao diện cũng như API máy chủ theo đúng 03 vai trò: Quản lý, Giáo vụ và Giảng viên.
* **FR02 — Quản lý hồ sơ học viên và phụ huynh:** Cho phép Giáo vụ thêm mới, tra cứu, cập nhật thông tin cá nhân học viên, thông tin phụ huynh bảo trợ và ghi chú tư vấn, năng khiếu; kiểm tra định dạng hợp lệ của ngày sinh và số điện thoại liên hệ.
* **FR03 — Quản lý danh mục đào tạo và tài nguyên:** Cho phép Quản lý thiết lập và cập nhật danh mục bộ môn năng khiếu, cấp độ, khung chương trình khóa học mẫu, danh sách phòng học chuyên dụng kèm sức chứa và hồ sơ giảng viên kèm bộ môn chuyên môn.
* **FR04 — Khởi tạo lớp học và quản lý trạng thái tuyển sinh:** Cho phép Giáo vụ mở lớp học mới kế thừa thông số từ khóa học mẫu, cấu hình sĩ số tối đa, gán giảng viên phụ trách chính và kích hoạt trạng thái Mở tuyển sinh sau khi đã lập đủ lịch học.
* **FR05 — Lập thời khóa biểu và kiểm tra xung đột tự động:** Hỗ trợ Giáo vụ thiết lập lịch học chi tiết gồm ngày học, ca giờ bắt đầu và kết thúc, phòng học, giảng viên cho đủ *N* buổi của lớp học; hệ thống tự động kiểm tra chuyên môn và ngăn chặn xung đột lịch theo quy tắc BR03.
* **FR06 — Tiếp nhận đăng ký ghi danh:** Cho phép Giáo vụ chọn học viên và lớp học đang mở tuyển sinh để tạo hồ sơ ghi danh ở trạng thái Chờ thanh toán, kiểm tra trùng lịch học của học viên và hiển thị mức học phí trọn khóa cần thu.

## B.2. Phân hệ Thu học phí và Điểm danh chuyên môn

* **FR07 — Thu học phí và kích hoạt ghi danh nguyên tử:** Cho phép Giáo vụ xác nhận đã nhận đủ học phí bằng tiền mặt hoặc chuyển khoản, hệ thống tự động kiểm tra chỗ trống lần cuối, phát hành phiếu thu nội bộ và chuyển trạng thái ghi danh sang Có hiệu lực trong cùng một giao dịch.
* **FR08 — Ghi nhận và xử lý sổ khoản tiền chờ:** Cho phép Giáo vụ ghi nhận ngay thông tin khoản tiền đã nhận thực tế nhưng gặp sự cố kích hoạt vào sổ khoản tiền chờ xử lý; hỗ trợ Quản lý phê duyệt kích hoạt bổ sung hoặc xác nhận hoàn tiền thủ công có lưu vết.
* **FR09 — Phát hành phiếu thu thay thế:** Cho phép Quản lý lập phiếu thu thay thế nhằm điều chỉnh sai sót về phương thức thanh toán hoặc ghi chú hành chính của phiếu thu cũ mà không làm thay đổi số tiền và ngày thu thực tế.
* **FR10 — Điểm danh buổi học và nhận xét năng khiếu:** Cung cấp giao diện cho Giảng viên phụ trách xem danh sách học viên của buổi học gồm học viên chính thức và học viên học bù, tích chọn trạng thái hiện diện, nhập nhận xét đánh giá chuyên môn từng học viên và chốt điểm danh sau giờ học.
* **FR11 — Điều chỉnh kết quả điểm danh có lưu vết:** Cho phép Giảng viên phụ trách hoặc Quản lý cập nhật lại trạng thái điểm danh của buổi học đã chốt khi có sai sót, bắt buộc nhập lý do giải trình và tự động ghi nhận lịch sử thay đổi.
* **FR12 — Tiếp nhận và phê duyệt đơn xin nghỉ phép:** Cho phép Giáo vụ ghi nhận yêu cầu xin nghỉ học của phụ huynh trước giờ học và phê duyệt đơn nghỉ hợp lệ làm cơ sở dữ liệu cho trạng thái Vắng có phép khi điểm danh.

## B.3. Phân hệ Điều phối học bù, Báo cáo và Nhật ký kiểm toán

* **FR13 — Tìm kiếm lớp và bố trí lịch học bù:** Tự động sinh quyền học bù khi chốt vắng có phép; hỗ trợ Giáo vụ tra cứu danh sách các buổi học tương đương cùng môn, cùng cấp độ, còn chỗ trống, không trùng lịch học viên trong hạn 30 ngày để xếp lịch học bù và in phiếu hẹn.
* **FR14 — Đổi lịch hoặc hủy buổi học kèm tạo buổi thay thế:** Cho phép Giáo vụ dời ngày giờ, đổi phòng hoặc giảng viên, hoặc hủy một buổi học trước giờ bắt đầu do sự cố đột xuất, đồng thời bắt buộc khởi tạo buổi học bù thay thế cho cả lớp theo quy tắc BR01.
* **FR15 — Báo cáo thống kê sĩ số và tỷ lệ chuyên cần:** Tổng hợp số lượng học viên theo từng lớp học, thống kê chi tiết số buổi có mặt, vắng có phép, vắng không phép tại lớp gốc và theo dõi độc lập kết quả các lượt đi học bù.
* **FR16 — Báo cáo doanh thu học phí và đối soát tài chính:** Cung cấp cho Quản lý bảng tổng hợp doanh thu thực thu theo kỳ thời gian, bộ môn, hình thức thanh toán bằng Tiền mặt hoặc Chuyển khoản và báo cáo chi tiết trạng thái xử lý các khoản tiền chờ.
* **FR17 — Tra cứu đa tiêu chí và xuất dữ liệu bảng tính:** Hỗ trợ tìm kiếm nhanh hồ sơ học viên, lớp học, phiếu thu theo nhiều bộ lọc và cho phép trích xuất các bảng báo cáo thống kê ra tệp định dạng bảng tính CSV hoặc Excel phục vụ lưu trữ.
* **FR18 — Quản lý nhật ký hệ thống:** Tự động ghi nhận và cho phép Quản lý tra cứu lịch sử thực hiện các thao tác trọng yếu gồm thu học phí, phát hành phiếu thay thế, xử lý tiền chờ, sửa điểm danh, hủy hoặc đổi lịch học.

<!-- page -->
# PHỤ LỤC C: ĐẶC TẢ CÁC CA SỬ DỤNG TRỌNG TÂM
## C.1. Phân hệ Ghi danh và Xếp lịch học

### UC01 — Tiếp nhận ghi danh và thu học phí trọn gói

* **Tác nhân chính:** Giáo vụ hoặc Quản lý.
* **Các yêu cầu liên quan:** FR06, FR07, FR08; BR02, BR05, BR06, BR07.
* **Tiền điều kiện:** Học viên đã được tạo hồ sơ trên hệ thống; lớp học dự kiến đăng ký đang ở trạng thái Mở tuyển sinh và chưa bắt đầu buổi học đầu tiên.
* **Luồng sự kiện chính:**
  1. Giáo vụ tra cứu hồ sơ học viên và chọn lớp học cần đăng ký; hệ thống hiển thị chi tiết thời khóa biểu *N* buổi, số chỗ trống hiện tại và mức học phí trọn khóa cố định.
  2. Hệ thống tự động kiểm tra lịch học của lớp mới không bị xung đột với các buổi học hiện có của học viên và khởi tạo bản ghi ghi danh ở trạng thái Chờ thanh toán.
  3. Giáo vụ thu đủ 100% số tiền học phí từ phụ huynh, chọn phương thức thanh toán bằng Tiền mặt hoặc Chuyển khoản, nhập mã tham chiếu giao dịch và bấm xác nhận thu phí.
  4. Hệ thống kiểm tra khóa giao dịch và xác nhận lớp vẫn còn chỗ trống hợp lệ; tiếp theo thực hiện lưu phiếu thu nội bộ Receipt và cập nhật trạng thái ghi danh Enrollment sang Có hiệu lực, đồng thời tăng sĩ số hiện tại của lớp lên 01 trong cùng một giao dịch nguyên tử.
  5. Hệ thống hiển thị thông tin phiếu thu hoàn chỉnh để Giáo vụ in biên lai xác nhận giao cho phụ huynh.
* **Luồng ngoại lệ:**
  * Tại bước 4, nếu lớp học vừa bị giao dịch khác chiếm chỗ cuối cùng hoặc xảy ra sự cố cơ sở dữ liệu trong khi Giáo vụ đã cầm tiền thực tế, hệ thống hủy giao dịch kích hoạt và chuyển ngay sang màn hình lập bản ghi sổ theo dõi khoản tiền chờ xử lý PaymentIncident theo quy tắc BR07 để Quản lý đối soát chuyển lớp hoặc hoàn tiền.

### UC02 — Lập và điều chỉnh thời khóa biểu lớp học

* **Tác nhân chính:** Giáo vụ hoặc Quản lý.
* **Các yêu cầu liên quan:** FR04, FR05, FR14; BR01, BR02, BR03, BR09.
* **Tiền điều kiện:** Lớp học đã được khởi tạo từ khóa học mẫu; danh mục phòng học chuyên dụng và giảng viên đang ở trạng thái hoạt động.
* **Luồng sự kiện chính:**
  1. Giáo vụ chọn lớp học và tiến hành cấu hình lịch học cho đủ *N* buổi học gồm ngày, giờ bắt đầu, giờ kết thúc, phòng học chuyên dụng và giảng viên đứng lớp.
  2. Hệ thống kiểm tra phòng học và giảng viên được chọn có đáp ứng đúng bộ môn năng khiếu của lớp hay không, đồng thời kiểm tra không có sự giao thoa thời gian với bất kỳ buổi học hợp lệ nào khác trên hệ thống.
  3. Khi toàn bộ *N* buổi học đều hợp lệ và không có xung đột, hệ thống lưu thời khóa biểu và chuyển trạng thái lớp học từ Dự kiến sang Mở tuyển sinh.
* **Luồng ngoại lệ:**
  * Tại bước 2, nếu phát hiện xung đột khung giờ, hệ thống tô đỏ buổi học bị trùng, hiển thị rõ thông tin lớp, phòng hoặc giảng viên đang chiếm lịch và từ chối lưu cho đến khi Giáo vụ điều chỉnh sang khung giờ hoặc phòng trống khác.

<!-- page -->
## C.2. Phân hệ Điểm danh chuyên môn và Điều phối học bù

### UC03 — Điểm danh và ghi nhận xét chuyên môn buổi học

* **Tác nhân chính:** Giảng viên phụ trách buổi học.
* **Các yêu cầu liên quan:** FR10, FR11; BR04, BR09, BR10.
* **Tiền điều kiện:** Giảng viên đăng nhập hợp lệ và được phân công dạy buổi học đó; buổi học đang ở trạng thái Đã lên lịch.
* **Luồng sự kiện chính:**
  1. Giảng viên mở màn hình điểm danh của buổi học; hệ thống hiển thị danh sách học viên chính thức của lớp, tự động đánh dấu sẵn gợi ý Vắng có phép cho những học viên đã có đơn xin nghỉ được Giáo vụ duyệt, và danh sách học viên đăng ký học bù vào buổi học này.
  2. Trong hoặc ngay sau buổi học, Giảng viên tích chọn trạng thái hiện diện thực tế và nhập nhận xét đánh giá kỹ năng, tiến bộ năng khiếu cho từng học viên.
  3. Sau khi thời gian buổi học kết thúc, Giảng viên bấm nút Chốt điểm danh.
  4. Hệ thống chuyển trạng thái buổi học sang Hoàn thành, khóa chỉnh sửa thông thường, cập nhật trạng thái các lượt học bù MakeupBooking và tự động khởi tạo bản ghi Quyền học bù MakeupEntitlement ở trạng thái Chờ bố trí cho các học viên chính thức có kết quả Vắng có phép.
* **Luồng ngoại lệ:**
  * Tại bước 3, nếu thời gian hệ thống chưa vượt qua giờ kết thúc buổi học, hệ thống chỉ cho phép Lưu nháp thông tin nhận xét và thông báo chưa được phép chốt điểm danh chính thức theo quy tắc BR09.

### UC04 — Tiếp nhận xin nghỉ và bố trí lịch học bù

* **Tác nhân chính:** Giáo vụ.
* **Các yêu cầu liên quan:** FR12, FR13; BR02, BR03, BR10, BR11.
* **Tiền điều kiện:** Học viên có bản ghi Quyền học bù MakeupEntitlement đang ở trạng thái Chờ bố trí và còn trong thời hạn hiệu lực 30 ngày.
* **Luồng sự kiện chính:**
  1. Giáo vụ mở hồ sơ học viên và chọn quyền học bù cần được sắp xếp lịch.
  2. Hệ thống tự động truy vấn và liệt kê danh sách các buổi học đích khả dụng đáp ứng đủ 05 tiêu chí của quy tắc BR11 gồm cùng môn, cùng cấp độ, còn chỗ trống phòng học hoặc lớp học, không trùng lịch học viên và nằm trong hạn 30 ngày.
  3. Giáo vụ trao đổi với phụ huynh và chọn một buổi học đích phù hợp nhất trên danh sách.
  4. Hệ thống kiểm tra lại sức chứa tại thời điểm lưu, tạo bản ghi đăng ký học bù MakeupBooking, cập nhật trạng thái quyền học bù sang Đã bố trí và xuất Phiếu hẹn học bù.
* **Luồng ngoại lệ:**
  * Tại bước 2, nếu hiện tại không có lớp tương đương nào còn chỗ trống trong khung giờ phụ huynh mong muốn, hệ thống giữ nguyên trạng thái Chờ bố trí của quyền bù để Giáo vụ tiếp tục theo dõi xếp lịch vào tuần kế tiếp.

<!-- page -->
## C.3. Phân hệ Báo cáo và Đối soát vận hành

### UC05 — Đối chiếu thống kê chuyên cần và báo cáo doanh thu học phí

* **Tác nhân chính:** Quản lý xem toàn bộ báo cáo, hoặc Giáo vụ chỉ xem báo cáo học vụ và chuyên cần.
* **Các yêu cầu liên quan:** FR15, FR16, FR17; BR04, BR07, BR08, BR12.
* **Tiền điều kiện:** Người dùng đã đăng nhập và có quyền truy cập phân hệ báo cáo tương ứng.
* **Luồng sự kiện chính:**
  1. Người dùng chọn loại báo cáo cần kết xuất gồm Báo cáo sĩ số và chuyên cần lớp học, hoặc Báo cáo doanh thu và khoản tiền chờ xử lý cùng các bộ lọc thời gian, bộ môn, lớp học.
  2. Hệ thống truy vấn dữ liệu từ các bảng giao dịch, tách biệt rõ số liệu điểm danh chính khóa với số lượt học bù, đồng thời tách biệt tổng tiền từ các phiếu thu Hiệu lực với các khoản tiền nằm trong sổ khoản tiền chờ xử lý.
  3. Hệ thống hiển thị bảng dữ liệu tổng hợp trực quan trên màn hình và cho phép người dùng xuất tệp báo cáo định dạng bảng tính để lưu trữ hoặc trình ký.
* **Luồng ngoại lệ:**
  * Nếu người dùng có vai trò Giảng viên hoặc Giáo vụ cố tình truy cập đường dẫn báo cáo doanh thu tổng hợp của Quản lý, tầng máy chủ sẽ từ chối yêu cầu theo quy tắc BR04 và NFR01.

<!-- page -->
# PHỤ LỤC D: RÀNG BUỘC CHẤT LƯỢNG HỆ THỐNG

Nhằm đảm bảo chất lượng phần mềm phù hợp với đặc thù quản lý học vụ và tài chính nội bộ, hệ thống đặt ra 06 ràng buộc chất lượng cốt lõi làm tiêu chuẩn cho giai đoạn thiết kế và lập trình:

**Bảng D.1: Danh mục các yêu cầu phi chức năng và cơ chế kiểm soát kỹ thuật**

| Mã NFR | Tên ràng buộc chất lượng | Nội dung yêu cầu và phương thức đảm bảo kỹ thuật |
| --- | --- | --- |
| **NFR01** | **Bảo mật và kiểm soát phân quyền tại máy chủ** | Toàn bộ các API và truy vấn dữ liệu nghiệp vụ bắt buộc phải xác thực phiên đăng nhập và kiểm tra quyền theo vai trò tại tầng máy chủ. Đảm bảo Giảng viên không thể xem dữ liệu thu phí hoặc điểm danh thay cho lớp không được phân công. |
| **NFR02** | **Tính toàn vẹn nguyên tử của giao dịch tài chính** | Thao tác phát hành phiếu thu và kích hoạt trạng thái ghi danh phải tuân thủ nghiêm ngặt tính chất nguyên tử và nhất quán của cơ sở dữ liệu. Tuyệt đối không để xảy ra tình trạng có phiếu thu nhưng ghi danh chưa kích hoạt, hoặc ghi danh đã kích hoạt nhưng thiếu phiếu thu hợp lệ. |
| **NFR03** | **Kiểm soát tương tranh và chống gửi lặp giao dịch** | Áp dụng cơ chế khóa bản ghi cơ sở dữ liệu và mã chống gửi lặp khi xử lý xác nhận thu phí và đặt lịch học bù, loại trừ hoàn toàn lỗi vượt sĩ số phòng học khi có nhiều nhân viên thao tác cùng lúc. |
| **NFR04** | **Tính chính xác và minh bạch trong thống kê** | Cấu trúc dữ liệu phải phân tách độc lập giữa chuyên cần lớp gốc Attendance và lượt học bù MakeupBooking, cũng như giữa phiếu thu chính thức Receipt và khoản tiền chờ PaymentIncident, đảm bảo các báo cáo đối soát luôn khớp số liệu 100%. |
| **NFR05** | **Tính khả dụng và chuẩn mực giao diện tiếng Việt** | Toàn bộ giao diện, nhãn điều khiển và thông báo lỗi nghiệp vụ được trình bày bằng tiếng Việt chuẩn mực, rõ ràng; thiết kế tối ưu hóa thao tác nhập liệu nhanh tại quầy tiếp đón của Giáo vụ và thao tác điểm danh trên máy tính hoặc máy tính bảng của Giảng viên. |
| **NFR06** | **Khả năng đóng gói, sao lưu và triển khai kiểm thử** | Hệ thống hỗ trợ kịch bản khởi tạo dữ liệu mẫu đa dạng và cơ chế sao lưu, phục hồi cơ sở dữ liệu nhanh chóng, đảm bảo chạy ổn định trên môi trường cục bộ phục vụ quá trình chấm đồ án và vấn đáp cuối kỳ. |

<!-- page -->
# PHỤ LỤC E: MA TRẬN TRUY VẾT NGHIỆP VỤ

Ma trận truy vết dưới đây chứng minh tính nhất quán và độ bao phủ toàn diện trong thiết kế hướng đối tượng của nhóm, kết nối liền mạch từ Phân hệ nghiệp vụ → Tác nhân chính → Quy tắc nghiệp vụ BR → Yêu cầu chức năng FR và Ca sử dụng UC → Các lớp thực thể miền liên quan:

**Bảng E.1: Ma trận truy vết ngang giữa Yêu cầu nghiệp vụ, Chức năng và Mô hình lớp thực thể**

| Phân hệ nghiệp vụ | Tác nhân chính | Quy tắc nghiệp vụ BR | Yêu cầu chức năng FR và Ca sử dụng | Các lớp thực thể miền liên quan |
| --- | --- | --- | --- | --- |
| **1. Quản trị và danh mục đào tạo** | Quản lý | BR01, BR04, BR12 | FR01, FR03, FR18 | Account, Course, Room, Instructor |
| **2. Quản lý hồ sơ học viên** | Giáo vụ | BR01, BR04, BR12 | FR02 | Student |
| **3. Mở lớp và lập thời khóa biểu** | Giáo vụ | BR01, BR02, BR03, BR09 | FR04, FR05, FR14, UC02 | ClassGroup, Lesson, Room, Instructor, Course |
| **4. Tiếp nhận ghi danh** | Giáo vụ | BR02, BR03, BR05, BR06 | FR06, UC01 | Enrollment, ClassGroup, Student, Lesson |
| **5. Thu học phí và quản lý chứng từ** | Giáo vụ, Quản lý | BR06, BR07, BR08, BR12 | FR07, FR08, FR09, UC01 | Receipt, PaymentIncident, Enrollment, Account |
| **6. Điểm danh và nhận xét chuyên môn** | Giảng viên, Quản lý | BR04, BR09, BR10, BR12 | FR10, FR11, UC03 | Attendance, Lesson, Enrollment, MakeupEntitlement |
| **7. Duyệt nghỉ phép và điều phối học bù** | Giáo vụ | BR02, BR03, BR10, BR11 | FR12, FR13, UC04 | LeaveRequest, MakeupEntitlement, MakeupBooking, Lesson |
| **8. Báo cáo thống kê và đối soát** | Quản lý, Giáo vụ | BR04, BR07, BR08, BR12 | FR15, FR16, FR17, FR18, UC05 | Receipt, PaymentIncident, Attendance, MakeupBooking, ClassGroup |

Ma trận truy vết trên là căn cứ kỹ thuật để nhóm kiểm soát chặt chẽ phạm vi dự án, đảm bảo không bỏ sót bất kỳ quy tắc hay thực thể dữ liệu nào khi chuyển sang giai đoạn Thiết kế chi tiết ở Đợt 2 và Cài đặt phần mềm ở Cuối kỳ.

<!-- page -->
# PHỤ LỤC F: CÂU HỎI THẢO LUẬN VÀ XIN Ý KIẾN PHẢN BIỆN

Nhằm hoàn thiện hệ thống yêu cầu trước khi bước sang giai đoạn thiết kế chi tiết ở Đợt 2, nhóm kính mong nhận được ý kiến đóng góp từ Giảng viên và các bạn sinh viên xoay quanh 05 vấn đề trọng tâm sau:

1. **Về phạm vi và mô hình lớp học (Chương 1):** Việc chuẩn hóa ba loại hình lớp học gồm Cá nhân 1 kèm 1, Nhóm nhỏ 3 đến 5 học viên, Nhóm tiêu chuẩn 8 đến 12 học viên theo hình thức khóa học cố định số buổi đã phản ánh đủ đặc thù của trung tâm dạy năng khiếu chưa?
2. **Về tác nhân sử dụng hệ thống (Chương 2):** Trong phạm vi đồ án môn học, quyết định tập trung vào 03 tác nhân nội bộ gồm Quản lý, Giáo vụ, Giảng viên và thực hiện các giao dịch của Phụ huynh thông qua Giáo vụ tại quầy tiếp đón có hợp lý để đảm bảo độ sâu nghiệp vụ không?
3. **Về quy trình xử lý sự cố thu phí (Chương 2 và Phụ lục A):** Cơ chế sử dụng sổ theo dõi khoản tiền chờ xử lý PaymentIncident khi nhân viên đã nhận tiền mặt nhưng giao dịch hệ thống gặp lỗi có điểm nào cần cải tiến thêm để tăng tính minh bạch tài chính không?
4. **Về mô hình điểm danh và điều phối học bù (Chương 2 và Chương 3):** Quy tắc giới hạn thời hạn học bù trong 30 ngày và thiết kế tách rời bảng Attendance của lớp gốc với MakeupBooking của lượt học bù có còn trường hợp biên nào chưa được dự phòng không?
5. **Về thứ tự ưu tiên thiết kế ở Đợt 2 (Chương 3 và Chương 4):** Giữa phân hệ lập thời khóa biểu chống trùng trực quan và phân hệ điều phối lịch học bù, nhóm nên ưu tiên đầu tư thiết kế giao diện tương tác chi tiết cho phân hệ nào trước?
