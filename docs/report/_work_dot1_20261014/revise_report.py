from pathlib import Path
import shutil
import re

WORK = Path(__file__).resolve().parent
REPORT = WORK.parent
COURSE = REPORT.parent.parent
OLD = REPORT / '_work_dot1_20261013'
URL = 'https://docs.google.com/forms/d/e/1FAIpQLSenTD2JN9DCcaVJOOXoAiWOsRG7jEftdgfszZExJ_lw_65Rvg/viewform?usp=header'
WORK.mkdir(exist_ok=True)
backup = WORK / 'original_report.docx'
if not backup.exists():
    shutil.copyfile(REPORT / 'SE100_BaoCaoTienDo_Dot1_Scope_SRS.docx', backup)
text = (OLD / 'report_source.md').read_text(encoding='utf-8')
text = text.replace('tiền thực thu', 'học phí ghi nhận').replace('Tiền thực thu', 'Học phí ghi nhận')
text = text.replace('đổi hoặc hủy buổi chưa hoàn thành', 'đổi hoặc hủy buổi chưa bắt đầu')
text = text.replace('Đổi hoặc hủy buổi chưa hoàn thành', 'Đổi hoặc hủy buổi chưa bắt đầu')
text = text.replace('buổi cần đổi chưa hoàn thành', 'buổi cần đổi chưa bắt đầu')
text = text.replace('Giáo vụ bắt đầu và hoàn thành lớp;', 'Lớp tự chuyển sang Đang học khi đến giờ bắt đầu buổi đầu; Giáo vụ xác nhận hoàn thành lớp;')
text = text.replace('Mỗi buổi hủy phải có một buổi thay thế liên kết;', 'Chỉ đổi hoặc hủy lịch trước giờ bắt đầu. Với lớp tiếp tục tổ chức, mỗi buổi hủy phải có một buổi thay thế liên kết và không tạo chuỗi thay thế bị phân nhánh; hủy toàn lớp chưa thu không phải tạo buổi thay thế;')
text = text.replace('Hạn đề xuất là 30 ngày sau buổi cuối lớp gốc, chốt trên quyền khi tạo; đổi lịch lớp không tự đổi hạn.', 'Hạn đề xuất là 30 ngày sau ngày kết thúc dự kiến của lớp gốc tại lúc cấp quyền. Nếu lớp được kéo dài, cập nhật mọi quyền chưa sử dụng sang hạn mới khi hạn mới muộn hơn; không rút ngắn hạn đã cấp. Cập nhật hạn và đổi lịch cùng một giao dịch.')
text = text.replace('Điểm danh có ba kết quả:', 'Điểm danh lớp gốc có ba kết quả:')
text = text.replace('Học bù là quan hệ với lần vắng của một học viên, không phải kết quả điểm danh thứ tư.', 'Lượt bù chỉ có kết quả Có mặt hoặc Vắng; vắng bù không tạo quyền bù mới. Học bù liên kết với lần vắng của một học viên, không phải kết quả điểm danh thứ tư.')
text = text.replace('**BR07 — Giao dịch thu phí.**', '**BR07 — Giao dịch thu phí và tiền chờ xử lý.**')
text = text.replace('mỗi ghi danh chỉ có một phiếu thu hiệu lực cho toàn bộ học phí.', 'mỗi ghi danh chỉ có một phiếu thu hiệu lực cho toàn bộ học phí. Kiểm tra điều kiện trước khi nhận tiền và kiểm tra lại lúc lưu. Nếu đã nhận tiền nhưng không kích hoạt được, Giáo vụ ghi PaymentIncident riêng với số tiền thực nhận, thời điểm, bằng chứng và lý do; không coi đó là phiếu thu học phí. Mất mạng phải ghi sổ giao nhận và nhập đối chiếu khi có kết nối. Quản lý xác nhận xử lý: ghi nhận lại chỉ khi đủ mọi điều kiện, đồng thời liên kết phiếu thu và đóng khoản chờ trong cùng giao dịch; hoặc xác nhận đã trả tiền ngoài phần mềm, lưu bằng chứng, thời điểm và người xử lý. Mỗi khoản nhận tiền có mã đối chiếu duy nhất; gửi lại hoặc nhập từ sổ không được ghi nhận hai lần.')
text = text.replace('**FR07 — Thu phí và kích hoạt ghi danh.**', '**FR07 — Thu phí và kích hoạt ghi danh.**')
text = text.replace('Hệ thống kiểm tra lại điều kiện rồi lưu phiếu và kích hoạt theo BR05–BR07.', 'Hệ thống kiểm tra trước khi nhận tiền và kiểm tra lại lúc lưu phiếu, kích hoạt theo BR05–BR07. Nếu đã nhận tiền nhưng giao dịch thất bại, Giáo vụ ghi khoản chờ xử lý; Quản lý xác nhận xử lý theo BR07.')
text = text.replace('gửi lại không thu lặp.', 'gửi lại không thu lặp; khoản đã nhận nhưng chưa kích hoạt xuất hiện trong sổ chờ; xử lý lại thành công không cộng tiền hai lần.')
text = text.replace('xem ghi danh chờ thanh toán riêng với tiền đã thu.', 'xem ghi danh chờ thanh toán riêng với tiền đã nhận; trình bày riêng số tiền đã nhận chưa phân bổ và tiền đã trả lại thủ công. Đối chiếu theo mã khoản nhận để tránh cộng trùng.')
text = text.replace('không gọi tiền thu là lợi nhuận hay học phí dự kiến là học phí ghi nhận.', 'không gọi tiền thu là lợi nhuận; khoản chờ không bị ẩn hoặc cộng trùng với phiếu thu sau xử lý.')
text = text.replace('3. Giáo vụ nhận đủ tiền, chọn phương thức, nhập ngày thu và xác nhận khoản đã nhận.', '3. Giáo vụ kiểm tra lại điều kiện trước nhận tiền; nhận đủ tiền, chọn phương thức, nhập thời điểm thu và mã đối chiếu khoản nhận.')
text = text.replace('Khi mất phản hồi, gửi lại cùng định danh thao tác trả về kết quả cũ nếu giao dịch đã thành công.', 'Khi mất phản hồi, tra cứu bằng mã đối chiếu hoặc gửi lại cùng định danh để nhận kết quả cũ. Nếu chưa có phiếu mà đã nhận tiền, ghi khoản chờ xử lý theo BR07; không nhận tiền lần nữa.')
text = text.replace('3. Sau giờ kết thúc, Giảng viên chốt điểm danh.', '3. Sau giờ kết thúc, Giảng viên chốt điểm danh lớp gốc và kết quả lượt bù; lượt bù chỉ chọn Có mặt hoặc Vắng.')
text = text.replace('Sửa sai sau chốt thực hiện bằng FR11, giữ lịch sử và xử lý quan hệ học bù.', 'Sửa sai điểm danh lớp gốc sau chốt thực hiện bằng FR11, giữ lịch sử và xử lý quan hệ học bù. Lượt bù đã chốt bị khóa sửa theo BR11.')
text = text.replace('Tổng và dữ liệu nguồn nhất quán.', 'Học phí ghi nhận, tiền đã nhận chưa phân bổ và tiền trả lại có danh sách nguồn riêng, không đếm trùng một khoản nhận.')
text = text.replace('Giáo vụ đổi giờ, phòng hoặc giảng viên sau khi kiểm tra lại', 'Giáo vụ chỉ đổi hoặc hủy trước giờ bắt đầu, kiểm tra lại')
text = text.replace('buổi đã chốt không bị đổi;', 'buổi đã bắt đầu không bị đổi hoặc hủy;')
text = text.replace('Thu một phần hoặc thu thừa bị chặn;', 'Thu một phần hoặc thu thừa không kích hoạt; tiền đã nhận sai số tiền phải ghi khoản chờ xử lý;')
text = text.replace('không thể xếp', 'không thể xếp')
text = text.replace('Trước mở tuyển sinh, lớp phải có đúng N buổi chưa hủy theo số buổi đã chốt.', 'Trước mở tuyển sinh, lớp phải có đúng N buổi chưa hủy theo số buổi đã chốt. Sau khi mở, không thêm buổi ngoài số N; hủy và tạo buổi thay thế phải cùng một giao dịch. Chỉ tuyển trước giờ buổi đầu. Khi đến giờ buổi đầu, hệ thống tự chuyển lớp sang Đang học và hủy ghi danh Chờ thanh toán chưa thu, giữ lịch sử; khoản tiền chờ xử lý vẫn được theo dõi riêng. Không nhận tiền hoặc ghi danh mới sau thời điểm này.')
text = text.replace('Số học viên chính thức cộng các lượt bù đã bố trí tại một buổi', 'Toàn bộ học viên chính thức, kể cả người dự kiến vắng, cộng các lượt bù đã bố trí tại một buổi')
text = text.replace('ngừng hoạt động giảng viên hoặc phòng không xóa lịch sử và không cho xếp lịch mới.', 'ngừng hoạt động giảng viên hoặc phòng không xóa lịch sử và không cho xếp lịch mới; phải bố trí lại các buổi tương lai trước khi ngừng, không làm vô hiệu lịch đang diễn ra.')
text = text.replace('buổi hủy không có điểm danh hợp lệ;', 'buổi hủy không có điểm danh hợp lệ;')

def section(title, end):
    return text.split('## ' + title + '\n', 1)[1].split(end, 1)[0].strip()

members = text.split('| Thành viên | MSSV | Vai trò |', 1)[1].split('\n\n', 1)[0]
members = '| Thành viên | MSSV | Vai trò |' + members.replace('________', '24520244')
br1 = section('Quy tắc nghiệp vụ về lớp và ghi danh', '<!-- page -->')
br1 = br1.split('**Lưu ý về giữ chỗ.**')[0].strip()
br2 = section('Quy tắc nghiệp vụ về thu phí và việc học', '<!-- page -->')
fr1 = section('Yêu cầu chức năng về quản trị và tuyển sinh', '<!-- page -->')
fr2 = section('Yêu cầu chức năng về thu phí và điểm danh', '<!-- page -->')
fr3 = section('Yêu cầu chức năng về học bù và báo cáo', '<!-- page -->')
uc1 = section('Đặc tả các Use Case trọng tâm', '<!-- page -->')
uc2 = section('Đặc tả điểm danh và học bù', '<!-- page -->')
uc3 = section('Đặc tả báo cáo và biến đổi trạng thái', '<!-- page -->').split('| Đối tượng |')[0].strip()
nfr = section('Yêu cầu phi chức năng', '<!-- page -->')
trace = section('Ma trận truy vết yêu cầu', '<!-- page -->')
trace = trace.replace('TC11: Học phí ghi nhận bằng phiếu hiệu lực theo ngày thu; hồ sơ chưa thu không cộng tiền.', 'TC11: Phiếu hiệu lực khớp tổng học phí; khoản chờ có nguồn, xử lý lại không đếm trùng; trả tiền thủ công có bằng chứng.')
assign = section('Phân công cho giai đoạn tiếp theo', '## Rủi ro cần theo dõi')

source = f'''# Báo cáo tiến độ lần 1 SE100
## Phần mềm quản lý trung tâm dạy năng khiếu

**Trường:** Trường Đại học Công nghệ Thông tin, ĐHQG TP Hồ Chí Minh
**Môn học:** Phương pháp phát triển phần mềm hướng đối tượng
**Nội dung:** Xác định yêu cầu đề tài và đánh giá tính khả thi
**Ngày cập nhật:** 14/10/2026

{members}

**Phương án đề xuất.** Ứng dụng web nội bộ cho một chi nhánh, ba vai trò, lớp theo khóa có số buổi cố định. Luồng trọng tâm gồm mở lớp, ghi danh, thu học phí, xếp lịch, điểm danh và học bù. Nội dung là kết quả phân tích sơ bộ; chính sách cần được xác nhận khi khảo sát trung tâm.

[[qr:{URL}]]

<!-- page -->
# Mục lục
[[TOC]]

**Dùng khi báo cáo trước lớp.** Trình bày Chương 1 đến Chương 5 theo thứ tự: bài toán và phạm vi, tác nhân và luồng, các ngoại lệ, mô hình sơ bộ, tính khả thi và góp ý. Phụ lục chứa quy tắc, yêu cầu và Use Case để đối chiếu khi trả lời câu hỏi.

<!-- page -->
# Chương 1 Tổng quan đề tài
## 1.1 Bối cảnh và hoạt động cốt lõi

Trung tâm tổ chức lớp âm nhạc, mỹ thuật, thể thao hoặc kỹ năng theo môn và cấp độ. Hoạt động cốt lõi là tiếp nhận học viên, tổ chức lớp và lịch, thu học phí, theo dõi từng buổi học và giải quyết học bù. Phòng học cùng thiết bị cố định phải phù hợp môn; giảng viên cần chuyên môn phù hợp lớp.

Tài liệu định hướng mô tả việc dùng sổ và bảng tính rời rạc, dẫn đến khó đối chiếu sĩ số, lịch và học phí. Đây là bối cảnh phân tích từ tài liệu hiện có; nhóm chưa có biên bản khảo sát trung tâm để xác nhận tần suất hoặc mức độ của các vấn đề.

## 1.2 Phạm vi và nhu cầu phần mềm

Nhóm đề xuất một chi nhánh, ứng dụng nội bộ, quản lý lớp theo khóa trọn gói và thu đủ học phí một lần. Khóa là mẫu chương trình; lớp là đợt tổ chức cụ thể; buổi là lần học có thời gian, phòng và giảng viên. Lớp một kèm một dùng cùng mô hình với sĩ số tối đa bằng 1.

| Trong phạm vi phiên bản đầu | Ngoài phạm vi phiên bản đầu |
| --- | --- |
| Hồ sơ học viên và người liên hệ; môn, cấp độ, khóa, phòng và giảng viên. | Nhiều chi nhánh; cổng phụ huynh, ứng dụng di động. |
| Mở lớp, xếp từng buổi; kiểm tra trùng phòng, giảng viên và học viên. | Tối ưu lịch tự động; quản lý kho và bảo trì thiết bị. |
| Ghi danh trước khóa; học phí trọn khóa; phiếu thu nội bộ và sổ tiền chờ xử lý. | Thu nhiều đợt, khuyến mãi, cổng thanh toán, kế toán và hóa đơn điện tử. |
| Điểm danh, nhận xét, nghỉ có phép, học bù; báo cáo sĩ số, chuyên cần và thu phí. | Lương, bảo lưu dài hạn, chuyển lớp/hoàn phí tự động, cấp chứng chỉ. |

## 1.3 Mục tiêu cần kiểm chứng

Không vượt sĩ số hoặc trùng lịch khi thao tác đồng thời; học phí và khoản nhận tiền đều đối chiếu được; điểm danh lớp gốc tách khỏi lượt học bù; người dùng chỉ xem và sửa dữ liệu đúng quyền. Những mục tiêu này được cụ thể hóa thành 18 FR, 8 NFR và 12 BR trong phụ lục, chưa phải kết quả kiểm thử.

<!-- page -->
# Chương 2 Phân tích yêu cầu và nghiệp vụ
## 2.1 Tác nhân và quyền sử dụng

Ba tác nhân trực tiếp là Quản lý, Giáo vụ và Giảng viên. Học viên, phụ huynh là bên tham gia nghiệp vụ qua Giáo vụ; chưa đăng nhập vào phần mềm. Quản lý có các quyền của Giáo vụ, cộng quyền quản trị và sửa sai theo quy tắc.

[[diagram:use_cases.png|Hình 1 Tác nhân và các nhóm Use Case trong phạm vi]]

| Vai trò | Giới hạn quyền cần chú ý |
| --- | --- |
| Quản lý | Quản trị tài khoản, danh mục; xác nhận xử lý khoản chờ và thay chứng từ; xem toàn bộ báo cáo; sửa điểm danh có lý do. |
| Giáo vụ | Hồ sơ, lớp, lịch, ghi danh, thu phí, duyệt nghỉ, bố trí bù; tạo/xem khoản chờ. Không tự sửa phiếu đã xác nhận. |
| Giảng viên | Xem lịch, chốt điểm danh, nhận xét và xem chuyên cần buổi/lớp được phân công. Không xếp lịch, bố trí bù hoặc xem học phí. |

Hình dùng đường liền cho liên kết tác nhân và nghiệp vụ. Mũi tên tam giác rỗng hướng từ Quản lý đến Giáo vụ biểu diễn kế thừa quyền. Không dùng liên kết này để biểu diễn thứ tự xử lý; quyền chi tiết được kiểm tra ở máy chủ theo BR04.

<!-- page -->
## 2.2 Luồng nghiệp vụ từ đầu đến cuối

Giáo vụ mở lớp có đủ lịch, tư vấn và lập ghi danh Chờ thanh toán. Hồ sơ này không giữ chỗ. Khi thu, cần kiểm tra lại điều kiện trước nhận tiền và tại lúc ghi dữ liệu. Một giao dịch phải đồng thời lập phiếu thu và kích hoạt ghi danh; sau đó giảng viên theo dõi việc học, Giáo vụ bố trí bù và đối chiếu báo cáo.

[[diagram:workflow.png|Hình 2 Luồng chính và nhánh tiền đã nhận nhưng chưa kích hoạt]]

Tiền mặt hoặc chuyển khoản đã nhận không thể hoàn tác bằng giao dịch CSDL. Nếu ghi nhận thất bại, Giáo vụ ghi sổ khoản chờ xử lý; Quản lý xác nhận ghi nhận lại khi đủ điều kiện hoặc xác nhận đã trả tiền thủ công. Khi mất mạng, ghi sổ giao nhận và đối chiếu khi kết nối lại, dùng cùng mã khoản nhận để tránh ghi trùng.

**Ví dụ:** Hai nhân viên cùng xác nhận chỗ cuối; chỉ một ghi danh được kích hoạt. Nếu người còn lại đã nhận tiền, khoản đó xuất hiện ở sổ chờ, chưa có phiếu học phí. Báo cáo tách Học phí ghi nhận, Tiền đã nhận chưa phân bổ và Tiền trả lại; không bỏ sót hoặc cộng trùng khoản tiền.

<!-- page -->
## 2.3 Ràng buộc và kịch bản ngoại lệ

| Ràng buộc hoặc ngoại lệ | Cách xử lý đề xuất |
| --- | --- |
| Sĩ số và chỗ cuối | Đếm mọi học viên chính thức cùng lượt bù đã bố trí; không lấy chỗ của người dự kiến vắng. Không vượt giới hạn lớp hoặc sức chứa phòng. |
| Trùng lịch | Hai khoảng giao nhau khi bắt đầu A nhỏ hơn kết thúc B và bắt đầu B nhỏ hơn kết thúc A. Buổi liền nhau được phép; kiểm tra lại ở lúc ghi. |
| Đổi hoặc hủy buổi | Chỉ trước giờ bắt đầu. Lớp tiếp tục học phải có buổi thay thế liên kết; hủy toàn lớp chưa thu không cần buổi thay thế. |
| Thu sai hoặc mất phản hồi | Không kích hoạt khi số tiền khác học phí chốt. Tiền đã nhận phải vào sổ chờ; mất phản hồi phải tra cứu kết quả trước khi ghi nhận lại. |
| Vắng có phép và học bù | Giáo vụ duyệt trước chốt điểm danh. Một lần vắng gốc có tối đa một quyền; một quyền có tối đa một lượt bù đang bố trí và một lượt sử dụng. |
| Hủy hoặc vắng buổi bù | Không tính đã học; bố trí lại nếu còn hạn. Vắng buổi bù không sinh quyền bù mới. |
| Sửa điểm danh và phiếu thu | Có lý do và lịch sử; không xóa chứng từ. Chặn sửa gốc đã có bù sử dụng và sửa lượt bù đã chốt trong phiên bản đầu. |

## 2.4 Thuộc tính biến đổi theo thời gian

| Đối tượng | Vòng đời đề xuất |
| --- | --- |
| Lớp và ghi danh | Lớp Dự kiến → Mở tuyển sinh → Đang học theo giờ buổi đầu → Hoàn thành sau đủ N buổi chốt. Ghi danh Chờ thanh toán → Có hiệu lực cùng phiếu thu → Hoàn thành theo lớp. |
| Buổi và điểm danh | Buổi Đã lên lịch → Hoàn thành sau giờ kết thúc và chốt; chỉ Hủy trước bắt đầu. Điểm danh Nháp → Đã chốt, sửa gốc có lưu vết. |
| Quyền và lượt bù | Quyền Chờ bố trí → Đã bố trí → Đã sử dụng khi Có mặt đã chốt; vắng/hủy giải phóng lịch nếu còn hạn; quá hạn Hết hạn. |
| Chứng từ và khoản chờ | Phiếu Hiệu lực → Được thay thế cùng số tiền và ngày thu. Khoản chờ → Đã ghi nhận hoặc Đã trả lại; giữ lịch sử và chứng cứ. |

Học phí, số buổi của lớp và học phí ghi danh được chốt, không đổi theo giá danh mục. Hạn bù đề xuất là 30 ngày sau ngày cuối dự kiến khi cấp; kéo dài lớp chỉ gia hạn quyền chưa sử dụng, không rút ngắn hạn đã cấp. Các chính sách này cần xác nhận với trung tâm.

<!-- page -->
# Chương 3 Mô hình và định hướng thiết kế
## 3.1 Đối tượng và dữ liệu cần thu thập

| Nhóm đối tượng | Dữ liệu chính |
| --- | --- |
| Học viên và người liên hệ | Mã học viên, họ tên, ngày sinh; họ tên, quan hệ, số điện thoại người liên hệ. Một liên hệ có thể dùng cho nhiều học viên. |
| Môn, khóa, lớp và buổi | Môn, cấp độ; số buổi, học phí; sĩ số lớp; thời gian, phòng và giảng viên từng buổi. |
| Ghi danh và thu phí | Học viên, lớp, học phí chốt; phiếu thu, số tiền, thời điểm thực nhận, mã đối chiếu, phương thức và người thu. |
| Nghỉ, điểm danh và bù | Đề nghị và kết quả duyệt; kết quả buổi gốc; quyền bù, hạn, buổi đích và kết quả lượt bù. |
| Tài khoản và lịch sử | Vai trò, trạng thái, mật khẩu băm; người thao tác, thời điểm, trước/sau và lý do sửa. |

[[diagram:domain_finance.png|Hình 3 Mô hình miền ghi danh và thu phí ở mức sơ bộ]]

Mỗi ghi danh thuộc một học viên và một lớp. Receipt lưu cả phiếu cũ, nhưng mỗi ghi danh đã thu chỉ có một phiếu hiệu lực. PaymentIncident có thể liên kết phiếu sau xử lý; không đại diện khoản thu thứ hai. Khi xử lý thành công, liên kết phiếu và đóng khoản chờ trong cùng giao dịch.

<!-- page -->
## 3.2 Mô hình lớp học và học bù

[[diagram:domain_learning.png|Hình 4 Mô hình miền lịch học điểm danh và học bù ở mức sơ bộ]]

Mỗi Lesson thuộc một ClassGroup, dùng một Room và một Instructor. Attendance chỉ liên kết Enrollment với Lesson của chính lớp đã ghi danh. LeaveRequest thuộc một lần đề nghị nghỉ cho cặp ghi danh và buổi gốc; chỉ tối đa một đề nghị hiệu lực cho cặp này.

MakeupEntitlement phát sinh từ Attendance Vắng có phép đã chốt. MakeupBooking liên kết quyền với Lesson đích; kết quả tham dự lưu trên lượt bù, tách khỏi Attendance lớp gốc. Sơ đồ thể hiện số bản ghi lịch sử; ràng buộc “một quyền đang bố trí” và “một phiếu hiệu lực” không thể suy ra chỉ từ bội số 0..*.

## 3.3 Kiến trúc và giao diện dự kiến

Nhóm đề xuất ứng dụng web nguyên khối phân tầng: Giao diện → Dịch vụ nghiệp vụ → Truy cập dữ liệu → CSDL quan hệ. Ràng buộc lịch, sĩ số, giao dịch tiền và phân quyền phải xử lý ở máy chủ; giao diện hỗ trợ nhập liệu và phản hồi.

Đợt 2 sẽ cụ thể hóa màn hình Hồ sơ, Lớp và lịch, Ghi danh và phiếu thu, Điểm danh, Nghỉ và học bù, Khoản tiền chờ xử lý, Báo cáo và Quản trị. Mô hình trong lần 1 là mô hình miền sơ bộ; thuộc tính, phương thức, ERD, Screen Flow và kiến trúc triển khai chi tiết sẽ hoàn thiện ở giai đoạn sau.

<!-- page -->
# Chương 4 Tính khả thi và kế hoạch thực hiện
## 4.1 Đánh giá tính khả thi

| Khía cạnh | Đánh giá và điều kiện thực hiện |
| --- | --- |
| Nghiệp vụ | Có luồng lõi rõ, nhưng cần xác nhận thu trọn khóa, không giữ chỗ, hạn bù và chứng từ với đại diện trung tâm. |
| Kỹ thuật | Web phân tầng và CSDL quan hệ phù hợp. Khó nhất là tranh chỗ/lịch, chống lặp và quan hệ điểm danh với học bù. |
| Nhân lực và tiến độ | Sáu thành viên, Quốc Hướng điều phối. Chưa có hạn báo cáo trong tài liệu; chốt lịch theo lớp và triển khai theo mốc đầu ra. |
| Chi phí và demo | Ưu tiên công cụ sẵn có, dữ liệu mẫu và demo local. Công nghệ, chi phí hạ tầng cụ thể chưa được nhóm xác nhận. |

## 4.2 Mốc công việc và phân công

Thứ tự thực hiện: xác nhận chính sách và SRS → Activity/Sequence cho Use Case lõi → thiết kế lớp, dữ liệu và prototype → triển khai luồng xuyên suốt → kiểm thử và đóng gói demo. Component và Deployment Diagram sẽ lập khi chốt công nghệ.

{assign}

<!-- page -->
# Chương 5 Kết quả và nội dung xin góp ý
## 5.1 Kết quả của lần báo cáo này

Nhóm đã lập phương án phạm vi, ba tác nhân trực tiếp, luồng nghiệp vụ và ngoại lệ; xác định 18 yêu cầu chức năng, 8 yêu cầu phi chức năng, 12 quy tắc và 5 Use Case trọng tâm. Bốn hình mô tả vai trò, luồng và mô hình miền giúp đối chiếu nội dung. Các mã TC trong phụ lục là kịch bản dự kiến, chưa phải test đã chạy.

Chưa có biên bản khảo sát thực tế hoặc bằng chứng ứng dụng chạy được trong hồ sơ của báo cáo. Việc cần làm tiếp theo là xác nhận chính sách, chốt đặc tả, hoàn thiện UML và prototype cho lần 2. Không trình bày các đầu ra dự kiến thành kết quả đã triển khai.

## 5.2 Rủi ro và hướng xử lý

| Rủi ro | Hướng xử lý |
| --- | --- |
| Phạm vi khác cách vận hành thực tế | Khảo sát các quy tắc đang giả định; trưởng nhóm tổng hợp tác động trước khi đổi phạm vi. |
| Ghi nhận tiền hoặc lịch không nhất quán | Kiểm thử giao dịch, thao tác đồng thời, mất phản hồi và sổ chờ; đối chiếu dữ liệu nguồn. |
| Học bù không có lớp phù hợp | Giữ quyền chưa sử dụng và cảnh báo Giáo vụ; không tự khẳng định đã học hoặc hoàn phí. |
| Khó tích hợp phần việc nhóm | Dùng chung thuật ngữ và mã yêu cầu; mỗi hiện vật có người rà soát chéo. |

## 5.3 Câu hỏi góp ý theo thứ tự trình bày

1. Phạm vi một chi nhánh, khóa trọn gói có phù hợp đồ án? Nghiệp vụ nào đang thiếu hoặc thừa?
2. Tác nhân và quyền ở Hình 1 có hợp lý? Học viên/phụ huynh tương tác qua Giáo vụ có đủ cho phiên bản đầu?
3. Luồng ghi danh, thu tiền và sổ chờ có còn tình huống bỏ sót hoặc đếm trùng tiền?
4. Ràng buộc lịch, sĩ số, nghỉ và học bù còn mâu thuẫn hoặc thiếu ngoại lệ nào?
5. Mô hình miền và kế hoạch khả thi chưa? Nên ưu tiên phần nào cho prototype lần 2?

Người góp ý dùng QR ở trang đầu. Nhóm cần ghi nhận họ tên, MSSV, nhóm và việc có mặt tại lớp; trưởng nhóm chia sẻ kết quả cho giảng viên và đánh dấu các góp ý hữu ích. Biểu mẫu góp ý phục vụ phản biện báo cáo, tách biệt với khảo sát yêu cầu của trung tâm.

<!-- page -->
# Tài liệu tham khảo

1. SE100.md. Đề cương môn Phương pháp phát triển phần mềm hướng đối tượng. Tài liệu nội bộ học phần.
2. Gợi ý nội dung báo cáo tiến độ.md. Hướng dẫn lần 1 về yêu cầu, tính khả thi, ràng buộc và ngoại lệ; hướng dẫn thu góp ý và khung báo cáo 5 chương.
3. docs/DE_TAI.md. Khảo sát sơ bộ và định hướng đề tài Phần mềm quản lý trung tâm dạy năng khiếu. Ngày 22/09/2026.

**Câu hỏi khảo sát ưu tiên.** Trung tâm có thu trọn khóa, nhận giữa khóa hoặc giữ chỗ trước thanh toán không? Ai xác nhận tiền và xử lý tiền nhận sai? Nghỉ có phép được duyệt theo điều kiện nào, hạn bù và tình huống không có lớp bù phù hợp ra sao? Ai có quyền đổi lịch, sửa điểm danh và xem thông tin học viên? Biểu mẫu chứng từ thực tế có những trường nào bắt buộc?

<!-- page -->
# Phụ lục A Quy tắc nghiệp vụ
## A.1 Lớp lịch và ghi danh

{br1}

<!-- page -->
## A.2 Thu phí điểm danh và học bù

{br2}

<!-- page -->
# Phụ lục B Yêu cầu chức năng
## B.1 Quản trị và tuyển sinh

{fr1}

<!-- page -->
## B.2 Thu phí và điểm danh

{fr2}

<!-- page -->
## B.3 Học bù và báo cáo

{fr3}

<!-- page -->
# Phụ lục C Use Case trọng tâm
## C.1 Ghi danh thu phí và lập lịch

{uc1}

<!-- page -->
## C.2 Điểm danh và học bù

{uc2}

<!-- page -->
## C.3 Đối chiếu báo cáo

{uc3}

**Quy ước sơ đồ.** Hình 1 dùng liên kết tác nhân–nghiệp vụ và kế thừa tác nhân; Hình 2 dùng hộp công việc, hình thoi quyết định và mũi tên luồng. Hình 3–4 dùng đường quan hệ và bội số tại hai đầu: 1 là đúng một, 0..1 là tối đa một, 0..* là không hoặc nhiều. Tên lớp tiếng Anh để thống nhất khi thiết kế OOAD; chưa thể hiện phương thức hoặc khóa CSDL.

<!-- page -->
# Phụ lục D Yêu cầu phi chức năng

{nfr}

<!-- page -->
# Phụ lục E Ma trận truy vết

{trace}
'''
(WORK / 'report_source.md').write_text(source, encoding='utf-8')
shutil.copyfile(OLD / 'build_report.py', WORK / 'build_report.py')
shutil.copyfile(OLD / 'render_word_pdf.py', WORK / 'render_word_pdf.py')
print('Updated report source and preserved original DOCX.')
