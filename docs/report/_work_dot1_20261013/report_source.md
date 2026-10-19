# BÁO CÁO TIẾN ĐỘ ĐỢT 1
## Phần mềm quản lý trung tâm dạy năng khiếu

**Môn học:** SE100 — Phương pháp phát triển phần mềm hướng đối tượng
**Trường:** Trường Đại học Công nghệ Thông tin, ĐHQG TP Hồ Chí Minh
**Trọng tâm:** Xác định phạm vi và đặc tả yêu cầu phần mềm
**Ngày lập:** 13/10/2026
**Phiên bản:** 0.1 — Dự thảo phân tích để báo cáo và lấy góp ý

| Thành viên | MSSV | Vai trò |
| --- | --- | --- |
| Trần Hữu Quốc Hướng | 24520644 | Trưởng nhóm |
| Nguyễn Tuấn Khang | 24520763 | Thành viên |
| Nguyễn Lê Đức Huy | 24520680 | Thành viên |
| Dương Nguyễn Phú Quý | 24521489 | Thành viên |
| Nguyễn Văn Hoàng | 23520355 | Thành viên |
| Đào Phúc Đại | ________ | Thành viên |

**Kết luận chính.** Phiên bản đầu tập trung vào một chi nhánh, quản lý lớp theo khóa có số buổi cố định và luồng mở lớp, ghi danh, thu học phí, xếp lịch, điểm danh, học bù, báo cáo. SRS trong tài liệu xác định 18 yêu cầu chức năng, 8 yêu cầu phi chức năng và 12 quy tắc nghiệp vụ để làm cơ sở phân tích OOAD.

**Trạng thái tài liệu.** Phạm vi và quy tắc dưới đây là phương án nhóm đề xuất từ tài liệu định hướng. Chưa có biên bản khảo sát trung tâm hoặc chính sách nghiệp vụ được xác nhận trong hồ sơ hiện có. Đây là đầu ra phân tích, chưa phải kết quả triển khai hay nghiệm thu.

**Góp ý trong lớp.** Chưa có liên kết biểu mẫu góp ý nên chưa tạo mã QR. Khi có biểu mẫu, chèn QR tại đầu báo cáo và chia sẻ kết quả cho giảng viên. Các câu hỏi đề xuất được đặt ở cuối tài liệu.

<!-- page -->
# Nội dung báo cáo

Tài liệu giữ cấu trúc 5 chương theo hướng dẫn SE100. Chương 1 và Chương 2 là nội dung chính của đợt 1; các chương còn lại trình bày định hướng, tính khả thi và kế hoạch tiếp theo.

| Phần | Nội dung chính |
| --- | --- |
| Chương 1 Tổng quan đề tài | Bối cảnh, mục tiêu, phạm vi trong và ngoài hệ thống; tác nhân và luồng nghiệp vụ. |
| Chương 2 Phân tích | SRS, đối tượng dữ liệu, quy tắc, FR/NFR, đặc tả Use Case và truy vết nghiệm thu. |
| Chương 3 Thiết kế | Mô hình miền và kiến trúc sơ bộ; danh sách màn hình dự kiến cho đợt 2. |
| Chương 4 Xây dựng và triển khai ứng dụng | Đánh giá tính khả thi, kế hoạch triển khai và phân công 6 thành viên. |
| Chương 5 Tổng kết | Kết quả của bản tài liệu, giới hạn, tiêu chí chốt đợt 1 và công việc tiếp theo. |
| Tài liệu tham khảo và phụ lục | Nguồn nội bộ, câu hỏi khảo sát và câu hỏi góp ý trong lớp. |

## Cách đọc và quản lý thay đổi

SRS là tài liệu đặc tả yêu cầu phần mềm. Mỗi yêu cầu chức năng có mã FR, mỗi yêu cầu chất lượng có mã NFR, mỗi quy tắc nghiệp vụ có mã BR và mỗi Use Case chính có mã UC. Các mã giữ ổn định qua các lần chỉnh sửa để đối chiếu với thiết kế và kiểm thử.

Tài liệu hiện là bản 0.1. Sau khi nhóm rà soát và thu thập ý kiến nghiệp vụ, trưởng nhóm tổng hợp thay đổi để tạo bản 1.0. Mỗi thay đổi phạm vi cần nêu lý do, yêu cầu bị ảnh hưởng và phần việc bổ sung; không đưa chức năng mới vào kế hoạch chỉ vì có trong tài liệu định hướng ban đầu.

| Phiên bản | Ngày | Nội dung | Trạng thái |
| --- | --- | --- | --- |
| 0.1 | 13/10/2026 | Thu hẹp scope; lập SRS và kế hoạch OOAD đợt 1. | Chờ nhóm rà soát và xác nhận nghiệp vụ. |

**Thông tin chưa có.** MSSV của Đào Phúc Đại, tên giảng viên phụ trách lớp, hạn báo cáo và URL biểu mẫu góp ý chưa được cung cấp. Báo cáo không tự suy đoán các thông tin này.

<!-- page -->
# Chương 1 Tổng quan đề tài
## Bối cảnh và vấn đề cần giải quyết

Trung tâm dạy năng khiếu tổ chức các lớp âm nhạc, mỹ thuật, thể thao hoặc kỹ năng theo môn và cấp độ. Hoạt động hằng ngày gồm tiếp nhận học viên, mở lớp, phân công giảng viên, bố trí phòng, thu học phí và theo dõi việc tham gia từng buổi học.

Tài liệu định hướng nêu mô hình quản lý bằng sổ hoặc bảng tính rời rạc. Với mô hình này, nhân viên phải đối chiếu nhiều danh sách để biết lớp còn chỗ, học viên đã đóng tiền hay giảng viên có trùng lịch. Đây là bối cảnh giả định dùng để phân tích; chưa phải kết luận từ một cuộc khảo sát thực tế.

## Mục tiêu và ranh giới tổ chức

Nhóm đề xuất ứng dụng web nội bộ cho một trung tâm, một chi nhánh. Phần mềm lưu thống nhất hồ sơ, lớp, lịch, ghi danh, phiếu thu và điểm danh. Người sử dụng trực tiếp là Quản lý, Giáo vụ và Giảng viên; học viên và phụ huynh làm việc thông qua Giáo vụ.

| Mục tiêu | Kết quả cần kiểm chứng khi nghiệm thu |
| --- | --- |
| Ghi danh chính xác | Không trùng ghi danh có hiệu lực và không vượt sĩ số, kể cả thao tác đồng thời. |
| Lịch học nhất quán | Không xung đột phòng, giảng viên hoặc lịch học viên khi xác nhận ghi danh và học bù. |
| Theo dõi học phí | Phiếu thu gắn với một ghi danh, có số tiền chốt và đối chiếu được với báo cáo tiền thực thu. |
| Theo dõi học tập | Điểm danh và nhận xét theo từng buổi; học bù liên kết với lần vắng gốc. |
| Hỗ trợ OOAD | Yêu cầu truy vết được sang Use Case, đối tượng miền, thiết kế và kịch bản kiểm thử. |

## Cơ sở xác định yêu cầu

Nguồn hiện có gồm đề cương môn, hướng dẫn báo cáo và bản định hướng đề tài ngày 22/09/2026. Bản SRS này sử dụng các nguồn đó để xây dựng phương án có thể triển khai. Những quy định về thu phí, giữ chỗ, sửa chứng từ và học bù phải được xác nhận với người đại diện trung tâm trước khi chốt bản 1.0.

<!-- page -->
## Phạm vi phiên bản đầu

Phạm vi được thu hẹp từ bản định hướng để có thể hoàn thành một luồng nghiệp vụ đầy đủ trong học phần. Lớp một kèm một sử dụng cùng mô hình lớp với sĩ số tối đa bằng 1; không xây một phân hệ riêng.

| Nhóm chức năng | Trong phạm vi |
| --- | --- |
| Hồ sơ và danh mục | Học viên, người liên hệ, giảng viên, môn, cấp độ, khóa, phòng; trạng thái hoạt động. |
| Khóa và lớp | Khóa có số buổi, học phí trọn khóa; lớp cụ thể có giảng viên, lịch từng buổi và giới hạn sĩ số. |
| Ghi danh và học phí | Ghi danh trước buổi đầu; thu đủ một lần bằng tiền mặt hoặc chuyển khoản đã được Giáo vụ xác nhận thủ công. |
| Lịch và điểm danh | Kiểm tra xung đột; đổi hoặc hủy buổi chưa hoàn thành; điểm danh và nhận xét lớp được phân công. |
| Nghỉ và học bù | Duyệt vắng có phép; một quyền bù cho mỗi lần vắng của từng học viên; bố trí cùng môn và cấp độ, còn chỗ, không trùng lịch. |
| Quản trị và báo cáo | Phân quyền, lịch sử thao tác quan trọng, sĩ số, chuyên cần, tiền thực thu; lọc và xuất CSV. |

## Ngoài phạm vi

- Nhiều chi nhánh, cổng học viên hoặc phụ huynh, ứng dụng di động và học trực tuyến.
- Lớp đóng phí theo tháng, thẻ buổi linh hoạt, ghi danh giữa khóa, thu nhiều đợt và khuyến mãi nhiều chính sách.
- Tính lương, chấm công để trả lương, kế toán tổng hợp, hóa đơn điện tử, quản lý kho hoặc bảo trì thiết bị.
- Cổng thanh toán, đối soát ngân hàng tự động, tự động gửi SMS hoặc Zalo, tối ưu thời khóa biểu bằng thuật toán.
- Hoàn tiền, bảo lưu dài hạn, chuyển lớp có điều chỉnh học phí và cấp chứng chỉ tự động.
- AI, chatbot và phân tích nâng cao.

## Quyết định về phạm vi và lý do

Thu đủ học phí một lần giúp giảm số trạng thái tài chính phải xử lý. Ghi danh chờ thanh toán không giữ chỗ; hệ thống kiểm tra lại chỗ khi xác nhận thu và kích hoạt ghi danh. Phương án này cần được trung tâm đồng ý trước khi áp dụng thực tế.

Hệ thống báo cáo tiền thực thu từ chứng từ và chuyên cần từ điểm danh. Báo cáo không diễn giải tiền thu là lợi nhuận; không sử dụng điểm danh để tự động tính lương hoặc hoàn phí.

<!-- page -->
## Tác nhân và đối tượng nghiệp vụ

| Đối tượng | Nhu cầu và quyền chính |
| --- | --- |
| Quản lý | Quản trị tài khoản, danh mục và học phí; xử lý sửa sai chứng từ; xem toàn bộ báo cáo. |
| Giáo vụ | Quản lý hồ sơ, lớp, lịch; lập ghi danh, ghi nhận thu phí; duyệt nghỉ và bố trí học bù. |
| Giảng viên | Xem lịch và học viên thuộc lớp được giao; ghi, chốt và sửa điểm danh có lưu lịch sử. Không xem báo cáo học phí. |
| Học viên và phụ huynh | Cung cấp hồ sơ, chọn lớp, nộp tiền và đề nghị nghỉ hoặc học bù qua Giáo vụ. Không đăng nhập ở phiên bản đầu. |

Hồ sơ người liên hệ có thể liên kết nhiều học viên. Số điện thoại không được dùng làm định danh duy nhất của học viên vì anh chị em có thể dùng chung số của phụ huynh.

[[diagram:use_cases.png|Hình 1 Tác nhân và các nhóm nghiệp vụ chính]]

Sơ đồ dùng Mermaid dạng flowchart để biểu diễn ranh giới hệ thống và quan hệ tác nhân với nhóm nghiệp vụ. Đây là sơ đồ Use Case ở mức tổng quan, không biểu diễn thứ tự thực hiện hay quan hệ include và extend.

<!-- page -->
## Luồng nghiệp vụ từ đầu đến cuối

Trước tuyển sinh, Giáo vụ tạo lớp và bố trí đủ các buổi theo khóa. Khi học viên chọn lớp, Giáo vụ lập ghi danh chờ thanh toán. Sau khi nhận đủ học phí, hệ thống kiểm tra lại điều kiện, lập phiếu thu và kích hoạt ghi danh trong một giao dịch. Giảng viên sau đó điểm danh từng buổi; Giáo vụ bố trí học bù cho trường hợp đủ điều kiện và đối chiếu báo cáo.

[[diagram:workflow.png|Hình 2 Luồng ghi danh và theo dõi việc học]]

| Ngoại lệ | Cách xử lý trong phạm vi |
| --- | --- |
| Lớp hết chỗ lúc xác nhận thu | Từ chối kích hoạt và không sinh phiếu thu trong hệ thống; Giáo vụ giải quyết khoản tiền đã nhận ngoài hệ thống. |
| Trùng phòng, giảng viên hoặc học viên | Hiển thị buổi xung đột để chọn lịch hoặc lớp khác; không lưu thay đổi gây trùng. |
| Học viên vắng có phép | Giáo vụ duyệt; tạo một quyền bù gắn với buổi gốc, không tự hoàn phí. |
| Buổi học bị hủy | Không cho điểm danh hoặc dùng làm buổi bù; giữ lịch sử và bố trí buổi thay thế. |
| Thu không đủ, thu thừa hoặc tiền chưa được xác nhận | Không kích hoạt ghi danh; giải thích điều kiện thu trọn khóa. |

<!-- page -->
# Chương 2 Phân tích
## Cấu trúc SRS và thuật ngữ

SRS gồm phạm vi, tác nhân, đối tượng dữ liệu, quy tắc nghiệp vụ, yêu cầu chức năng, yêu cầu phi chức năng và tiêu chí chấp nhận. Bản 0.1 là cơ sở để nhóm xây dựng Use Case, Activity, Sequence, mô hình lớp và cơ sở dữ liệu ở các bước sau.

| Thuật ngữ | Nghĩa sử dụng trong tài liệu |
| --- | --- |
| Khóa học | Mẫu chương trình của một môn và cấp độ, có số buổi và học phí chuẩn. |
| Lớp học | Đợt tổ chức cụ thể của một khóa, có giảng viên, sĩ số và lịch. |
| Buổi học | Một khoảng thời gian cụ thể của lớp, sử dụng một phòng và một giảng viên. |
| Ghi danh | Quan hệ học viên với lớp; lưu học phí phải thu đã chốt. |
| Phiếu thu | Chứng từ nội bộ ghi nhận tiền đã nhận và được nhân viên xác nhận. |
| Điểm danh | Kết quả của một học viên tại một buổi, tách khỏi nhận xét học tập. |
| Quyền học bù | Quyền phát sinh từ một lần vắng có phép đã duyệt; không phải thẻ học trả trước. |

## Đối tượng và dữ liệu tối thiểu

| Đối tượng miền | Thuộc tính chính cần thu thập |
| --- | --- |
| Học viên và người liên hệ | Mã học viên, họ tên, ngày sinh, trạng thái; họ tên, quan hệ, điện thoại người liên hệ; email tùy chọn. |
| Giảng viên và phòng | Mã, tên, chuyên môn, trạng thái; phòng có mã, sức chứa và loại phòng. |
| Môn và khóa học | Mã, tên, cấp độ, số buổi nguyên dương, học phí VND nguyên dương. |
| Lớp và buổi học | Khóa, sĩ số tối đa, trạng thái; ngày giờ bắt đầu và kết thúc, phòng, giảng viên. |
| Ghi danh và phiếu thu | Học viên, lớp, học phí chốt, trạng thái; mã phiếu, số tiền, ngày thu, phương thức, người thu. |
| Điểm danh và học bù | Học viên, buổi, kết quả, nhận xét; lần vắng gốc, hạn bù, buổi bù và trạng thái. |
| Tài khoản và lịch sử | Tên đăng nhập, mật khẩu băm, vai trò, trạng thái; người thao tác, thời điểm, đối tượng, hành động và lý do. |

<!-- page -->
## Quy tắc nghiệp vụ về lớp và ghi danh

Các quy tắc BR01–BR12 là chính sách đề xuất cho nguyên mẫu. Chúng cần được rà soát khi khảo sát thực tế; không coi các con số hoặc cách xử lý là quy định đã ban hành của một trung tâm.

**BR01 — Đơn vị vận hành.** Một chi nhánh dùng múi giờ Asia/Ho_Chi_Minh và tiền VND. Lớp lưu số buổi và học phí của khóa khi tạo; không tự đổi khi danh mục khóa được sửa. Trước mở tuyển sinh, lớp phải có đúng N buổi chưa hủy theo số buổi đã chốt. Điều kiện tuổi và trình độ chỉ áp dụng nếu được khai báo, không tự suy diễn từ ngày sinh.

**BR02 — Sĩ số.** Ghi danh Có hiệu lực mới chiếm chỗ chính thức. Hồ sơ Chờ thanh toán không giữ chỗ. Số học viên chính thức cộng các lượt bù đã bố trí tại một buổi không vượt giới hạn lớp và sức chứa phòng. Lớp một kèm một có giới hạn 1.

**BR03 — Xung đột lịch.** Hai khoảng thời gian giao nhau khi bắt đầu A nhỏ hơn kết thúc B và bắt đầu B nhỏ hơn kết thúc A. Các buổi liền nhau được phép. Kiểm tra phòng, giảng viên, học viên và các lịch bù tại lúc lưu, kể cả thao tác đồng thời; buổi hủy không chiếm tài nguyên.

**BR04 — Phân quyền.** Quyền được kiểm tra ở máy chủ. Giảng viên chỉ truy cập lớp và buổi được phân công; Giáo vụ không quản lý tài khoản hoặc tự thay chứng từ đã xác nhận. Quản lý có các quyền nghiệp vụ của Giáo vụ, được quản trị tài khoản, danh mục, xem báo cáo và duyệt sửa sai có lưu vết.

**BR05 — Kích hoạt ghi danh.** Chỉ ghi danh vào lớp Mở tuyển sinh trước thời điểm bắt đầu buổi đầu tiên. Một học viên chỉ có một ghi danh chưa hủy trong cùng lớp. Khi thu đủ, hệ thống kiểm tra lại chỗ, lịch và trạng thái rồi kích hoạt. Hủy chỉ áp dụng cho ghi danh chưa thu; hủy ghi danh đã thu và hoàn tiền nằm ngoài phạm vi.

**BR06 — Học phí đã chốt.** Khi tạo ghi danh, hệ thống lưu học phí của lớp tại thời điểm đó. Đổi biểu phí không sửa số tiền đã chốt. Phiên bản đầu nhận đúng toàn bộ khoản phải thu một lần; không thu một phần, thu thừa hoặc áp dụng giảm giá.

**Lưu ý về giữ chỗ.** Vì ghi danh chờ thanh toán không giữ chỗ, Giáo vụ phải kiểm tra lớp ngay trước khi nhận tiền. Nếu tiền thực tế đã nhận nhưng lớp không còn hợp lệ, phần mềm từ chối giao dịch và nhân viên xử lý với khách hàng; hệ thống không tự chuyển lớp hoặc hoàn tiền.

<!-- page -->
## Quy tắc nghiệp vụ về thu phí và việc học

**BR07 — Giao dịch thu phí.** Lập phiếu thu và kích hoạt ghi danh phải cùng thành công hoặc cùng thất bại. Mỗi lần gửi có định danh chống lặp. Gửi lại cùng thao tác không được tạo phiếu thứ hai; mỗi ghi danh chỉ có một phiếu thu hiệu lực cho toàn bộ học phí.

**BR08 — Sửa sai chứng từ.** Phiếu xác nhận không bị sửa hoặc xóa trực tiếp. Quản lý chỉ được lập phiếu thay thế cùng ghi danh, cùng số tiền và ngày thu thực tế để sửa phương thức hoặc ghi chú; phải ghi lý do, giữ phiếu gốc và liên kết thay thế. Thao tác thay thế là một giao dịch, không đổi tình trạng ghi danh hay tổng tiền thực thu. Đổi số tiền, đổi học viên hoặc hoàn tiền nằm ngoài phiên bản đầu.

**BR09 — Buổi và điểm danh.** Buổi có giờ kết thúc sau giờ bắt đầu; chỉ chốt điểm danh sau giờ kết thúc. Mỗi học viên có một kết quả cho một buổi; nháp chưa cập nhật thống kê. Buổi hủy không có điểm danh hợp lệ; buổi hoàn thành không được đổi lịch. Mỗi buổi hủy phải có một buổi thay thế liên kết; lớp chỉ hoàn thành khi đúng N buổi chưa hủy đã kết thúc và chốt điểm danh. Buổi thay thế được tính trong lịch và chuyên cần, buổi hủy bị loại.

**BR10 — Vắng và học bù.** Điểm danh có ba kết quả: Có mặt, Vắng có phép, Vắng không phép. Vắng có phép cần Giáo vụ duyệt đề nghị trước khi chốt. Mỗi cặp ghi danh và buổi gốc có tối đa một quyền bù; chỉ lượt bù Có mặt đã chốt mới sử dụng quyền. Học bù là quan hệ với lần vắng của một học viên, không phải kết quả điểm danh thứ tư.

**BR11 — Bố trí và sửa học bù.** Buổi bù cùng môn, cấp độ, còn chỗ, không trùng lịch; chưa bắt đầu khi bố trí và kết thúc không quá hạn bù. Hạn đề xuất là 30 ngày sau buổi cuối lớp gốc, chốt trên quyền khi tạo; đổi lịch lớp không tự đổi hạn. Đây là tham số cần xác nhận. Hủy hoặc vắng bù cho phép bố trí lại trước hạn, không giữ hai lịch bù hiệu lực. Ghi danh hoàn thành vẫn dùng quyền còn hạn. Kết quả lượt bù đã chốt không sửa qua phần mềm; sửa điểm danh gốc đã có bù sử dụng cũng bị chặn để Quản lý xử lý thủ công.

**BR12 — Lịch sử và báo cáo.** Hồ sơ đã được tham chiếu chỉ được ngừng hoạt động. Sửa điểm danh phải có lý do, giữ giá trị cũ và tính lại thống kê; không tạo bản ghi thứ hai. Tiền thực thu tính từ phiếu hiệu lực theo ngày thu gốc. Chuyên cần lớp gốc bằng Có mặt chia tổng buổi gốc chưa hủy đã chốt của học viên; tỷ lệ hiển thị Không có dữ liệu nếu mẫu số bằng 0. Lượt bù được báo cáo riêng, không cộng hai lần vào tử số.

<!-- page -->
## Yêu cầu chức năng về quản trị và tuyển sinh

Tất cả FR01–FR18 thuộc phạm vi phiên bản đầu. Tiêu chí chấp nhận dưới đây là điều kiện cần kiểm thử khi triển khai, chưa phải kết quả kiểm thử đã đạt.

**FR01 — Đăng nhập và phân quyền.** Người dùng đăng nhập bằng tài khoản do Quản lý cấp, đăng xuất và bị chặn khi tài khoản ngừng hoạt động. Quyền theo BR04 phải áp dụng cho cả màn hình và dữ liệu máy chủ.
**Chấp nhận:** Giảng viên truy cập dữ liệu lớp khác hoặc báo cáo học phí bị từ chối; sửa vai trò trên giao diện không tạo thêm quyền.

**FR02 — Quản lý hồ sơ học viên.** Giáo vụ tạo, cập nhật, tìm kiếm học viên và người liên hệ. Học viên có mã riêng, ngày sinh không ở tương lai; có ít nhất một người liên hệ với số điện thoại.
**Chấp nhận:** Hai học viên có thể cùng dùng một người liên hệ; thiếu tên hoặc số liên hệ không lưu được; hồ sơ đã có ghi danh không bị xóa.

**FR03 — Quản lý danh mục.** Quản lý thiết lập môn, cấp độ, khóa, học phí, giảng viên và phòng. Số buổi, học phí và sức chứa phải dương; mã danh mục không trùng.
**Chấp nhận:** Sửa học phí khóa không đổi ghi danh cũ; ngừng hoạt động giảng viên hoặc phòng không xóa lịch sử và không cho xếp lịch mới.

**FR04 — Tạo và mở lớp.** Giáo vụ tạo lớp từ khóa, khai báo sĩ số và giảng viên. Mở tuyển sinh chỉ khi lớp có đủ buổi chưa hủy, các buổi hợp lệ và không vượt sức chứa.
**Chấp nhận:** Không mở lớp khi thiếu lịch hoặc lớp một kèm một có sĩ số 2; điều kiện không hợp lệ được chỉ rõ.

**FR05 — Lập lịch từng buổi.** Giáo vụ xếp ngày giờ, phòng và giảng viên cho từng buổi; kiểm tra BR03 tại lúc lưu.
**Chấp nhận:** Hai buổi liền nhau lưu được; hai yêu cầu đồng thời dùng cùng phòng trong giờ giao nhau chỉ một yêu cầu thành công.

**FR06 — Lập ghi danh chờ thanh toán.** Giáo vụ chọn học viên và lớp, xem học phí chốt và kiểm tra điều kiện trước khi tạo hồ sơ. Ghi danh chờ thanh toán không chiếm chỗ; có thể hủy nếu chưa thu tiền.
**Chấp nhận:** Từ chối đăng ký trùng chưa hủy, lớp đã bắt đầu hoặc lịch học viên bị xung đột; hủy hồ sơ chưa thu không sinh phiếu thu.

<!-- page -->
## Yêu cầu chức năng về thu phí và điểm danh

**FR07 — Thu phí và kích hoạt ghi danh.** Giáo vụ nhập đúng học phí chốt, ngày thu, phương thức Tiền mặt hoặc Chuyển khoản và xác nhận đã nhận tiền. Hệ thống kiểm tra lại điều kiện rồi lưu phiếu và kích hoạt theo BR05–BR07.
**Chấp nhận:** Thu một phần hoặc thu thừa bị chặn; hai người kích hoạt chỗ cuối chỉ một người thành công; lỗi lưu không để lại phiếu hoặc ghi danh kích hoạt một phần; gửi lại không thu lặp.

**FR08 — Xem và sửa sai phiếu thu.** Giáo vụ xem hoặc in chứng từ; Quản lý thay thế chứng từ sai theo BR08. Phiếu hiển thị học viên, lớp, số tiền, ngày thu, phương thức, người thu và mã duy nhất; ghi rõ là phiếu thu nội bộ.
**Chấp nhận:** Thay phương thức đúng quyền giữ nguyên tổng thu và ngày thu; phiếu gốc còn trong lịch sử; đổi số tiền hoặc xóa phiếu bị từ chối.

**FR09 — Theo dõi trạng thái lớp.** Giáo vụ bắt đầu và hoàn thành lớp; chỉ hoàn thành khi đủ số buổi của khóa đã kết thúc và chốt điểm danh, bao gồm buổi thay thế cho lịch hủy. Hủy lớp chỉ khi chưa có ghi danh đã thu.
**Chấp nhận:** Khóa 12 buổi hủy 1 buổi không được kết thúc với 11 buổi; không hoàn thành lớp còn buổi chưa chốt; quyền bù còn hạn vẫn dùng được sau khi lớp gốc hoàn thành.

**FR10 — Điểm danh và nhận xét.** Giảng viên xem đúng danh sách chính thức và học viên bù của buổi được giao, lưu nháp, chốt ba trạng thái chuyên cần và nhập nhận xét.
**Chấp nhận:** Hồ sơ chờ thanh toán không nằm trong danh sách học; không chốt trước giờ kết thúc; chốt lại cùng dữ liệu không nhân bản điểm danh hoặc quyền bù.

**FR11 — Sửa điểm danh lớp gốc có lưu vết.** Giảng viên phụ trách hoặc Quản lý được sửa kết quả lớp gốc đã chốt với lý do; lượt bù đã chốt không sửa qua chức năng này. Thống kê được tính lại; sửa làm vô hiệu quyền bù đang bố trí phải hủy lịch bù trong cùng giao dịch.
**Chấp nhận:** Lịch sử có người sửa, thời điểm, trước và sau; điểm danh gốc đã có lượt bù sử dụng không được tự sửa sang kết quả khác.

**FR12 — Duyệt đề nghị nghỉ.** Giáo vụ ghi đề nghị nghỉ theo học viên và buổi, duyệt hoặc từ chối kèm lý do. Kết quả duyệt làm căn cứ chốt Vắng có phép.
**Chấp nhận:** Đề nghị từ chối không tạo quyền bù; mỗi cặp ghi danh và buổi gốc có tối đa một đề nghị đang hiệu lực; hai học viên vắng cùng buổi có đề nghị riêng; Vắng có phép chưa duyệt không chốt được.

<!-- page -->
## Yêu cầu chức năng về học bù và báo cáo

**FR13 — Bố trí và theo dõi học bù.** Giáo vụ xem quyền bù từ điểm danh đã chốt và chọn buổi phù hợp theo BR10–BR11. Giảng viên điểm danh lượt bù trong buổi đích; có mặt mới sử dụng quyền.
**Chấp nhận:** Không chọn lớp sai môn, sai cấp độ, hết chỗ hoặc hết hạn; một quyền không có hai lịch bù hoạt động; vắng hoặc hủy lượt bù không được báo là đã học.

**FR14 — Đổi hoặc hủy buổi chưa hoàn thành.** Giáo vụ đổi giờ, phòng hoặc giảng viên sau khi kiểm tra lại toàn bộ người tham gia và lượt bù. Hủy buổi giữ lịch sử và giải phóng các lịch bù để bố trí lại.
**Chấp nhận:** Không đổi buổi gây trùng lịch học viên; buổi đã chốt không bị đổi; buổi hủy không chiếm phòng, không được điểm danh và không tính chuyên cần.

**FR15 — Báo cáo sĩ số và chuyên cần.** Quản lý, Giáo vụ xem danh sách ghi danh theo trạng thái, chuyên cần lớp gốc và lượt bù theo lớp hoặc học viên. Giảng viên chỉ xem báo cáo chuyên cần lớp được giao.
**Chấp nhận:** Chỉ số Sĩ số đang học chỉ đếm ghi danh Có hiệu lực; lớp kết thúc vẫn xem được danh sách Hoàn thành. Chuyên cần theo BR12; mẫu số 0 hiển thị Không có dữ liệu; lượt bù trình bày riêng.

**FR16 — Báo cáo học phí và tiền thực thu.** Quản lý, Giáo vụ lọc phiếu hiệu lực theo ngày thu, lớp, môn và phương thức; xem ghi danh chờ thanh toán riêng với tiền đã thu.
**Chấp nhận:** Tổng báo cáo bằng tổng chứng từ nguồn; phiếu thay thế không cộng hai lần; không gọi tiền thu là lợi nhuận hay học phí dự kiến là tiền thực thu.

**FR17 — Tra cứu và xuất dữ liệu.** Người có quyền tìm theo mã hoặc tên, lọc danh sách, phân trang và xuất CSV theo đúng bộ lọc. Dữ liệu xuất tuân theo cùng phạm vi quyền như màn hình.
**Chấp nhận:** Giảng viên không xuất học phí; bộ lọc không có kết quả vẫn trả danh sách rỗng rõ ràng; file tiếng Việt đọc đúng và không kích hoạt công thức từ dữ liệu người dùng.

**FR18 — Nhật ký và ngừng hoạt động.** Quản lý xem lịch sử thay đổi quan trọng, ngừng tài khoản hoặc danh mục và bảo toàn đối tượng đã được tham chiếu.
**Chấp nhận:** Thao tác thu, thay phiếu, đổi lịch, sửa điểm danh có người thực hiện và thời điểm; người dùng không xóa nhật ký qua chức năng thông thường.

<!-- page -->
## Đặc tả các Use Case trọng tâm

**UC01 — Ghi danh và thu học phí**
**Tác nhân:** Giáo vụ. **Liên quan:** FR06–FR08; BR02, BR03, BR05–BR08.
**Tiền điều kiện:** Đã đăng nhập; học viên có hồ sơ; lớp Mở tuyển sinh và chưa bắt đầu.

1. Giáo vụ chọn học viên và lớp; hệ thống hiển thị lịch, điều kiện và học phí.
2. Hệ thống kiểm tra đăng ký trùng, lịch và điều kiện; tạo ghi danh Chờ thanh toán cùng học phí chốt.
3. Giáo vụ nhận đủ tiền, chọn phương thức, nhập ngày thu và xác nhận khoản đã nhận.
4. Hệ thống kiểm tra lại sĩ số, trạng thái và lịch; lưu phiếu thu và chuyển ghi danh sang Có hiệu lực trong một giao dịch.
5. Giáo vụ nhận mã phiếu thu và thông tin lớp để bàn giao cho học viên.

**Hậu điều kiện:** Có một phiếu thu hiệu lực; ghi danh chiếm một chỗ. **Ngoại lệ:** Lớp hết chỗ, đã bắt đầu hoặc thu sai số tiền thì từ chối; lỗi lưu thì hoàn tác. Khi mất phản hồi, gửi lại cùng định danh thao tác trả về kết quả cũ nếu giao dịch đã thành công.

**UC02 — Lập hoặc đổi lịch học**
**Tác nhân:** Giáo vụ. **Liên quan:** FR04, FR05, FR14; BR01–BR03, BR09.
**Tiền điều kiện:** Lớp tồn tại; phòng và giảng viên đang hoạt động; buổi cần đổi chưa hoàn thành.

1. Giáo vụ chọn lớp, ngày, giờ, phòng và giảng viên.
2. Hệ thống kiểm tra thời lượng, sức chứa và các khoảng thời gian giao nhau.
3. Với lịch đổi, hệ thống kiểm tra thêm học viên chính thức, lượt bù đã bố trí và giờ kết thúc không vượt hạn của mỗi quyền bù.
4. Khi hợp lệ, lưu buổi và lịch sử thay đổi; hiển thị lịch cập nhật.

**Hậu điều kiện:** Có lịch hợp lệ, không gây xung đột. **Ngoại lệ:** Hiển thị đối tượng và buổi đang trùng, không lưu một phần. Nếu tài nguyên vừa bị người khác chiếm, kiểm tra lại tại lúc ghi và từ chối giao dịch xung đột.

<!-- page -->
## Đặc tả điểm danh và học bù

**UC03 — Điểm danh và nhận xét buổi học**
**Tác nhân:** Giảng viên được phân công. **Liên quan:** FR10–FR12; BR04, BR09–BR12.
**Tiền điều kiện:** Buổi chưa hủy; danh sách học viên chính thức và học bù đã xác định.

1. Giảng viên mở buổi được giao; hệ thống hiển thị học viên và đề nghị nghỉ đã duyệt.
2. Giảng viên ghi kết quả, nhận xét; có thể lưu nháp để kiểm tra.
3. Sau giờ kết thúc, Giảng viên chốt điểm danh.
4. Hệ thống kiểm tra đủ kết quả, quyền thao tác và vắng có phép; lưu chính thức trong một giao dịch.
5. Hệ thống cập nhật thống kê, tạo quyền bù cho lần vắng đủ điều kiện hoặc sử dụng quyền của lượt bù có mặt.

**Hậu điều kiện:** Mỗi học viên có một kết quả đã chốt cho buổi. **Ngoại lệ:** Thiếu kết quả, vắng có phép chưa duyệt, buổi hủy hoặc quyền đã dùng thì không chốt. Sửa sai sau chốt thực hiện bằng FR11, giữ lịch sử và xử lý quan hệ học bù.

**UC04 — Bố trí học bù**
**Tác nhân:** Giáo vụ; Giảng viên xác nhận việc tham dự. **Liên quan:** FR12–FR14; BR02, BR03, BR10–BR11.
**Tiền điều kiện:** Điểm danh gốc Vắng có phép đã chốt; quyền bù còn hạn và chưa sử dụng.

1. Giáo vụ chọn quyền bù; xem môn, cấp độ, buổi gốc và hạn.
2. Hệ thống liệt kê buổi phù hợp chưa bắt đầu, kết thúc không quá hạn bù; Giáo vụ chọn buổi.
3. Hệ thống kiểm tra chỗ, lịch học viên và lịch bù đang giữ; lưu một lượt bù Đã bố trí.
4. Khi buổi đích diễn ra, Giảng viên chốt kết quả lượt bù.
5. Có mặt chuyển quyền sang Đã sử dụng; nếu vắng, quyền trở về Chờ bố trí khi còn hạn.

**Hậu điều kiện:** Mỗi lần vắng của một cặp ghi danh và buổi gốc có tối đa một lượt bù đã sử dụng. **Ngoại lệ:** Buổi bù hủy thì giải phóng lịch; hết hạn không bố trí mới; không có lớp phù hợp thì giữ Chờ bố trí để Giáo vụ xử lý, không tự hoàn tiền.

<!-- page -->
## Đặc tả báo cáo và biến đổi trạng thái

**UC05 — Đối chiếu báo cáo**
**Tác nhân:** Quản lý hoặc Giáo vụ. **Liên quan:** FR15–FR17; BR07, BR08, BR12.
**Tiền điều kiện:** Đã đăng nhập với quyền phù hợp.

1. Người dùng chọn khoảng ngày, lớp hoặc môn và loại báo cáo.
2. Hệ thống truy vấn các bản ghi được phép, áp dụng đúng định nghĩa tiền thu, sĩ số hoặc chuyên cần.
3. Người dùng xem tổng, mở danh sách nguồn để đối chiếu và xuất CSV theo cùng bộ lọc.

**Hậu điều kiện:** Tổng và dữ liệu nguồn nhất quán. **Ngoại lệ:** Không có dữ liệu hiển thị danh sách rỗng và tổng tiền 0; tỷ lệ có mẫu số 0 hiển thị Không có dữ liệu. Người không có quyền bị từ chối ở máy chủ.

| Đối tượng | Trạng thái và điều kiện chuyển |
| --- | --- |
| Lớp | Dự kiến → Mở tuyển sinh khi đủ lịch → Đang học khi tới buổi đầu → Hoàn thành khi đúng N buổi của khóa đã chốt, kể cả buổi thay thế. Hủy chỉ khi chưa có ghi danh đã thu. |
| Ghi danh | Chờ thanh toán → Có hiệu lực cùng giao dịch thu đủ → Hoàn thành theo lớp. Chờ thanh toán có thể Hủy; Có hiệu lực không tự hủy trong MVP. |
| Buổi | Đã lên lịch → Hoàn thành sau giờ kết thúc và chốt điểm danh; hoặc Hủy trước hoàn thành. Buổi thay thế có mã mới. |
| Điểm danh | Chưa ghi → Nháp → Đã chốt. Kết quả chuyên cần được lưu tách biệt; chỉnh sửa đã chốt giữ lịch sử. |
| Quyền bù | Chờ bố trí → Đã bố trí → Đã sử dụng khi có mặt; hủy hoặc vắng lượt bù trở lại Chờ bố trí nếu còn hạn; quá hạn chuyển Hết hạn. |
| Phiếu thu | Hiệu lực → Được thay thế khi phiếu mới cùng số tiền, ngày thu và ghi danh được lưu thành công. Không có thao tác xóa. |

Không suy ra đã thu tiền từ trạng thái lớp hoặc đã học từ trạng thái Đã bố trí. Các đối tượng có vòng đời riêng, liên kết bằng mã để giữ đúng lịch sử.

<!-- page -->
## Yêu cầu phi chức năng

Các NFR dưới đây là mục tiêu kiểm thử đề xuất. Kết quả phải được ghi theo môi trường và dữ liệu thử khi ứng dụng được triển khai; chưa có kết quả đo trong báo cáo đợt 1.

| Mã | Yêu cầu và cách kiểm chứng |
| --- | --- |
| NFR01 | Phân quyền tại máy chủ cho mọi truy cập và xuất dữ liệu. Kiểm thử từng vai trò và thay mã lớp, học viên hoặc chứng từ; mọi truy cập trái quyền bị từ chối. |
| NFR02 | Không lưu mật khẩu rõ; không ghi mật khẩu vào nhật ký. Chỉ lưu kết quả băm bằng cơ chế chuẩn của nền tảng; kiểm tra dữ liệu và thử đăng nhập sau khi khóa tài khoản. |
| NFR03 | Giao dịch thu, thay phiếu và chốt điểm danh có tính nguyên tử và chống lặp. Thử lỗi tại các bước ghi, gửi lặp và 2 thao tác tranh chỗ cuối; không có dữ liệu dở dang. |
| NFR04 | Mục tiêu 95% thao tác tra cứu danh sách hoàn tất trong 2 giây với 10 người dùng đồng thời, 1.000 học viên, 100 lớp, 2.000 buổi. Ghi cấu hình máy, giới hạn trang 50 dòng và điều kiện mạng khi đo. |
| NFR05 | Giao diện tiếng Việt, nhãn rõ, trạng thái rỗng hoặc lỗi và giữ dữ liệu form khi lỗi. Ba tác vụ ghi danh, thu phí, điểm danh thực hiện được bằng bàn phím trên màn hình từ 1280 × 720. |
| NFR06 | Sao lưu và khôi phục CSDL cùng nhật ký từ bộ dữ liệu demo. Sau khôi phục, số bản ghi, liên kết và tổng phiếu thu phải khớp; phương án demo có thể chạy local khi mạng lỗi. |
| NFR07 | Lưu người thực hiện, thời điểm và lý do cho sửa chứng từ, lịch, điểm danh. Không xóa lịch sử qua chức năng thường; người xem nhật ký phải có quyền. Kiểm tra bằng kịch bản trước và sau thay đổi. |
| NFR08 | Thời gian nghiệp vụ thống nhất theo Asia/Ho_Chi_Minh; tiền VND không dùng số thực dấu phẩy động. CSV mã hóa UTF-8 và vô hiệu hóa giá trị có thể trở thành công thức; kiểm tra file bằng dữ liệu tiếng Việt và chuỗi bắt đầu bằng dấu bằng. |

**Giới hạn vận hành.** Phiên bản học phần phục vụ dữ liệu mẫu, chưa cam kết mức độ sẵn sàng của hệ thống production. Không sử dụng thông tin cá nhân thật để dựng demo khi chưa được người cung cấp đồng ý.

<!-- page -->
## Ma trận truy vết yêu cầu

Ma trận giúp kiểm tra mỗi nhóm chức năng trong scope đều có yêu cầu và kịch bản nghiệm thu. TC01–TC12 là mã kịch bản dự kiến, không thể hiện test đã chạy.

| Phạm vi | Yêu cầu | Quy tắc | Kịch bản cần kiểm thử |
| --- | --- | --- | --- |
| Tài khoản và quyền | FR01, FR18 | BR04, BR12 | TC01: Giảng viên bị chặn lớp khác và báo cáo học phí; tài khoản khóa không đăng nhập. |
| Hồ sơ và danh mục | FR02, FR03 | BR01, BR06, BR12 | TC02: Chung người liên hệ; không xóa hồ sơ có tham chiếu; đổi giá không sửa ghi danh cũ. |
| Lớp và lịch | FR04, FR05, FR14 | BR01–BR03, BR09 | TC03: Thiếu lịch; trùng giờ và 2 người lưu cùng phòng; phòng mới thiếu sức chứa. |
| Ghi danh | FR06, FR07 | BR02, BR03, BR05 | TC04: Trùng ghi danh; lớp đã bắt đầu; chờ thu không giữ chỗ; tranh chỗ cuối. |
| Thu học phí | FR07 | BR06, BR07 | TC05: Đủ, thiếu, thừa; gửi lặp; lỗi giữa giao dịch không kích hoạt hoặc sinh phiếu một phần. |
| Chứng từ | FR08, FR16 | BR08, BR12 | TC06: Thay phiếu đúng quyền, cùng số tiền và ngày thu; giữ lịch sử và không cộng hai lần. |
| Vòng đời lớp | FR09 | BR05, BR09, BR11 | TC07: Hủy 1 trong 12 buổi phải có buổi thay thế; chưa đủ điểm danh không hoàn thành; lớp xong vẫn dùng quyền bù còn hạn. |
| Điểm danh | FR10, FR11 | BR04, BR09–BR12 | TC08: Chốt đúng giờ; lưu lặp; sửa có lý do; chặn sửa gốc đã có bù sử dụng. |
| Nghỉ và học bù | FR12, FR13, FR14 | BR02, BR03, BR10, BR11 | TC09: Vắng chưa duyệt; sai môn/cấp độ; hết chỗ; 2 lịch bù; hủy/vắng bù và hết hạn. |
| Báo cáo chuyên cần | FR15 | BR09, BR12 | TC10: Mẫu số 0; buổi hủy không tính; học bù trình bày riêng. |
| Báo cáo thu phí | FR16 | BR06–BR08, BR12 | TC11: Tiền thực thu bằng phiếu hiệu lực theo ngày thu; hồ sơ chưa thu không cộng tiền. |
| Tra cứu và xuất | FR17 | BR04, BR12 | TC12: Bộ lọc khớp nguồn; không lộ dữ liệu trái quyền; tiếng Việt và chống công thức CSV. |

NFR01–NFR08 được kiểm chứng bằng các kịch bản bảo mật, toàn vẹn, tải, khả dụng và khôi phục tương ứng. Khi thay BR hoặc FR, nhóm cập nhật UC, thiết kế và TC liên quan trong cùng lần rà soát.

<!-- page -->
# Chương 3 Thiết kế
## Mô hình miền sơ bộ

Mô hình sau xác định các khái niệm và quan hệ chính để chuẩn bị phân tích hướng đối tượng. Tên lớp dùng tiếng Anh. Sơ đồ chưa phải thiết kế lớp chi tiết hoặc ERD; thuộc tính, phương thức, khóa và chiến lược lưu dữ liệu sẽ được hoàn thiện sau khi SRS được xác nhận.

[[diagram:domain.png|Hình 3 Quan hệ các đối tượng miền cốt lõi]]

Điểm danh học viên chính thức liên kết ghi danh với buổi gốc. Lượt bù liên kết quyền bù, học viên và buổi đích; kết quả tham dự lượt bù được lưu trên lượt bù, tách khỏi điểm danh lớp gốc. Việc này tránh nhầm học viên bù thành một ghi danh mới hoặc thu lại học phí.

## Định hướng kiến trúc và giao diện

Nhóm đề xuất ứng dụng web nguyên khối phân tầng: giao diện, dịch vụ nghiệp vụ và truy cập dữ liệu quan hệ. Ràng buộc sĩ số, lịch, tiền và quyền được xử lý ở lớp nghiệp vụ và CSDL; giao diện chỉ hỗ trợ nhập và phản hồi. Cách tổ chức này phục vụ việc đặc tả lớp và giao dịch OOAD, đồng thời giảm số thành phần triển khai.

Màn hình dự kiến cho đợt 2 gồm Đăng nhập; Hồ sơ học viên; Danh mục; Lớp và lịch; Ghi danh và phiếu thu; Buổi học và điểm danh; Nghỉ và học bù; Báo cáo; Tài khoản và lịch sử. Prototype cần thể hiện trạng thái lỗi, không có dữ liệu, bị từ chối quyền và mất phản hồi sau khi thu phí.

<!-- page -->
# Chương 4 Xây dựng và triển khai ứng dụng
## Đánh giá tính khả thi

Phạm vi khả thi ở mức đồ án vì sử dụng một chi nhánh, ba vai trò, khóa có số buổi cố định và thu phí trọn khóa. Độ khó chính nằm ở kiểm soát giao dịch, xung đột lịch và quan hệ điểm danh với học bù; nhóm cần triển khai luồng xuyên suốt trước các chức năng mở rộng.

| Khía cạnh | Đánh giá và điều kiện |
| --- | --- |
| Nghiệp vụ | Có thể mô hình hóa bằng các đối tượng rõ ràng. Cần xác nhận chính sách giữ chỗ, thu trọn khóa, sửa phiếu và thời hạn bù với trung tâm. |
| Kỹ thuật | Web phân tầng và CSDL quan hệ phù hợp giao dịch. Cần kiểm chứng cạnh tranh chỗ/lịch và chống lặp, không chỉ kiểm tra form. |
| Nhân lực | Có 6 thành viên; Quốc Hướng điều phối. Phân công theo hiện vật, có người rà soát chéo để giảm phụ thuộc một cá nhân. |
| Tiến độ | Chưa có deadline chính thức trong nguồn hiện có. Dùng thứ tự mốc và đầu ra; lịch theo ngày được chốt khi nhận lịch lớp. |
| Chi phí và demo | Ưu tiên công cụ sẵn có và dữ liệu mẫu; chuẩn bị chạy local. Chưa kết luận chi phí bằng 0 hoặc đã có hạ tầng triển khai. |

## Kế hoạch thực hiện theo thứ tự

1. Xác nhận giả định nghiệp vụ, sửa phạm vi và chốt SRS bản 1.0.
2. Hoàn thiện Use Case, Activity, Sequence cho ghi danh, thu phí, xếp lịch và điểm danh/học bù.
3. Thiết kế lớp chi tiết, dữ liệu và prototype; rà soát lại ma trận truy vết.
4. Chọn ngôn ngữ, framework và CSDL theo năng lực nhóm; triển khai lớp/lịch, ghi danh/thu phí, điểm danh/học bù rồi báo cáo.
5. Kiểm thử chức năng và ngoại lệ theo TC/NFR; đóng gói demo, hướng dẫn và báo cáo cuối kỳ.

**Trạng thái triển khai.** Báo cáo đợt 1 trình bày phân tích và phương án. Chưa có bằng chứng trong nguồn đã đọc về ứng dụng SE100 chạy được, test đã đạt hoặc môi trường đã triển khai. Component và Deployment Diagram được lập khi chốt công nghệ ở giai đoạn tiếp theo.

<!-- page -->
## Phân công cho giai đoạn tiếp theo

Phân công dưới đây là kế hoạch do báo cáo đề xuất, không phải xác nhận công việc đã hoàn thành. Trưởng nhóm điều phối scope và tổng hợp tài liệu; các thành viên chịu trách nhiệm đầu ra riêng và rà soát chéo.

| Thành viên | Đầu ra chính | Người rà soát |
| --- | --- | --- |
| Trần Hữu Quốc Hướng | Scope, quản lý thay đổi, ma trận truy vết; tổng hợp SRS, slide và kết quả góp ý. | Nguyễn Tuấn Khang |
| Nguyễn Tuấn Khang | Actor, lớp/lịch; UC02, Activity/Sequence và prototype lớp/lịch. | Dương Nguyễn Phú Quý |
| Nguyễn Lê Đức Huy | Ghi danh, học phí; UC01, chứng từ mẫu và ngoại lệ giao dịch thu. | Nguyễn Văn Hoàng |
| Dương Nguyễn Phú Quý | Điểm danh, nghỉ/học bù; UC03–UC04 và biến đổi trạng thái. | Nguyễn Lê Đức Huy |
| Nguyễn Văn Hoàng | Đối tượng dữ liệu, mô hình miền, dữ liệu mẫu và báo cáo UC05. | Đào Phúc Đại |
| Đào Phúc Đại | NFR, kịch bản TC01–TC12, kiểm tra tính nhất quán và biểu mẫu góp ý. | Trần Hữu Quốc Hướng |

## Rủi ro cần theo dõi

| Rủi ro | Cách xử lý |
| --- | --- |
| Chưa khảo sát trung tâm thật | Gắn nhãn giả định; ưu tiên xác nhận quy trình và chính sách trước thiết kế chi tiết. |
| Scope tăng từ tài liệu định hướng | Mỗi đề xuất mới phải có lý do, FR/BR và ảnh hưởng kế hoạch; trưởng nhóm tổng hợp trước khi chốt. |
| Sai số tiền, chỗ hoặc lịch khi thao tác đồng thời | Thiết kế giao dịch, ràng buộc dữ liệu và thử cạnh tranh; kiểm tra lại tại lúc lưu. |
| Chính sách học bù không phù hợp thực tế | Xác nhận điều kiện và hạn; giữ quan hệ buổi gốc, không mở rộng tự động hoàn phí. |
| Mất thời gian tích hợp tài liệu | Thống nhất mã yêu cầu, thuật ngữ và mẫu đặc tả; mỗi đầu ra có người review. |
| Thiếu URL góp ý và MSSV | Trưởng nhóm bổ sung trước khi trình bày; không tạo thông tin hoặc QR giả. |

<!-- page -->
# Chương 5 Tổng kết
## Kết quả của bản báo cáo đợt 1

Bản tài liệu đã hệ thống hóa phương án phạm vi một chi nhánh, ba tác nhân phần mềm và luồng nghiệp vụ chính. Phần SRS xác định 18 FR, 8 NFR, 12 BR, 5 Use Case trọng tâm, các vòng đời dữ liệu và 12 nhóm kịch bản kiểm thử dự kiến. Mô hình miền, định hướng kiến trúc và phân công tạo cơ sở cho báo cáo lần 2.

Các kết quả này là đầu ra tài liệu hiện tại. Chúng không thay thế biên bản khảo sát, xác nhận của giảng viên hoặc kết quả triển khai và kiểm thử.

## Tiêu chí chốt nội dung đợt 1

- Sáu thành viên đọc lại scope, FR/BR và ma trận truy vết; ghi các mâu thuẫn hoặc đề xuất thay đổi.
- Xác nhận với người đại diện trung tâm các quy tắc giữ chỗ, thời điểm ghi danh, thu trọn khóa, sửa phiếu và học bù.
- Mỗi chức năng trong phạm vi có actor, dữ liệu, điều kiện hợp lệ, ngoại lệ và tiêu chí chấp nhận.
- Không giữ các thao tác thuộc phạm vi loại trừ trong sơ đồ, Use Case hoặc prototype.
- Bổ sung MSSV của Đào Phúc Đại và QR của biểu mẫu góp ý; chia sẻ kết quả cho giảng viên, đánh dấu ý kiến hữu ích.

## Ưu điểm và giới hạn

Phạm vi có luồng hoàn chỉnh, quy tắc xử lý đồng thời và tiêu chí kiểm thử cụ thể. Đặc tả phân biệt lớp với khóa, tiền thực thu với học phí dự kiến, điểm danh lớp gốc với lượt học bù. Những lựa chọn này giúp giảm mâu thuẫn khi thiết kế OOAD.

Giới hạn hiện tại là thiếu khảo sát thực tế, lịch báo cáo chính thức và xác nhận chính sách. Thu đủ một lần và không nhận giữa khóa làm phiên bản đầu đơn giản hơn nhưng có thể khác cách vận hành của trung tâm. Nhóm sẽ cập nhật có kiểm soát khi nhận thông tin thực tế.

## Hướng phát triển sau phiên bản đầu

Sau khi nghiệm thu luồng lõi, có thể xem xét cổng phụ huynh, thu phí nhiều đợt, bảo lưu/chuyển lớp và nhiều chi nhánh. Các chức năng này không được tính vào cam kết hiện tại và phải có phân tích tác động riêng.

<!-- page -->
# Tài liệu tham khảo và phụ lục
## Nguồn được sử dụng

1. SE100.md — Đề cương môn Phương pháp phát triển phần mềm hướng đối tượng; dùng xác định định hướng học phần và nội dung OOAD.
2. Gợi ý nội dung báo cáo tiến độ.md — Hướng dẫn lần 1 về yêu cầu, luồng, ngoại lệ và tính khả thi; hướng dẫn QR góp ý và khung 5 chương.
3. docs/DE_TAI.md — Định hướng đề tài ngày 22/09/2026; dùng lấy bối cảnh và nhóm nghiệp vụ, sau đó thu hẹp scope cho phiên bản đầu.
4. AGENTS.md của SE100 — Ngữ cảnh môn, trưởng nhóm và quy cách tài liệu. Danh sách 6 thành viên cập nhật theo ảnh và thông tin người dùng cung cấp ngày 13/10/2026.

## Câu hỏi cần khảo sát với trung tâm

- Trung tâm thu trọn khóa hay nhiều đợt? Có nhận người vào giữa khóa và giữ chỗ khi chưa đóng tiền không?
- Lớp được mở khi nào, có yêu cầu tuổi/trình độ ra sao và ai được đổi lịch hoặc hủy lớp?
- Ai xác nhận tiền mặt/chuyển khoản, sửa phiếu sai và đối chiếu tiền thu? Biểu mẫu hiện dùng có trường nào bắt buộc?
- Nghỉ có phép được duyệt theo điều kiện nào? Học bù ở lớp khác, hạn 30 ngày và trường hợp không có lớp phù hợp được xử lý ra sao?
- Ai được xem thông tin học viên, nhận xét và học phí? Có tài liệu/chứng từ mẫu nào cho phép nhóm sử dụng không?

## Nội dung biểu mẫu góp ý trong lớp

Biểu mẫu góp ý phục vụ nhận xét báo cáo, tách biệt với khảo sát yêu cầu nghiệp vụ. Khi thiết lập, cần thu họ tên, MSSV, thông tin nhóm và xác nhận người góp ý có mặt tại lớp theo hướng dẫn môn; không tự tạo dữ liệu người tham dự.

1. Phạm vi một chi nhánh và luồng lõi có đủ cho đồ án? Chức năng nào đang thừa hoặc thiếu?
2. Tác nhân và quyền có hợp lý? Quy tắc ghi danh hoặc thu phí nào còn mâu thuẫn?
3. Ngoại lệ về trùng lịch, chỗ cuối và học bù còn thiếu tình huống nào?
4. Yêu cầu FR/NFR nào chưa đo hoặc kiểm thử được? Đề xuất chỉnh cụ thể.
5. Nhận xét về tính khả thi, mô hình miền và nội dung cần ưu tiên cho lần 2.

Trưởng nhóm tổng hợp, trả lời và đánh dấu ý kiến hữu ích rồi chia sẻ kết quả với giảng viên. Tài liệu chưa có biểu mẫu trực tuyến nên chưa thể ghi nhận việc đã thu góp ý.
