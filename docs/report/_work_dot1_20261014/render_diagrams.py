from pathlib import Path
import math
import sys
from PIL import Image, ImageDraw, ImageFont

WORK = Path(__file__).resolve().parent
DIAGRAMS = WORK.parent.parent / 'diagrams'
FONT = 'C:/Windows/Fonts/arial.ttf'
BOLD = 'C:/Windows/Fonts/arialbd.ttf'
DIAGRAMS.mkdir(exist_ok=True)
sources = {}

def canvas(w, h):
    image = Image.new('RGB', (w, h), 'white')
    return image, ImageDraw.Draw(image)

def label(draw, xy, text, size=30, bold=False, align='center'):
    font = ImageFont.truetype(BOLD if bold else FONT, size)
    draw.multiline_text(xy, text, font=font, fill='black', anchor='mm', align=align, spacing=8)

def box(draw, bounds, text, size=30, oval=False):
    if oval:
        draw.ellipse(bounds, fill='white', outline='black', width=3)
    else:
        draw.rectangle(bounds, fill='white', outline='black', width=3)
    label(draw, ((bounds[0]+bounds[2])/2, (bounds[1]+bounds[3])/2), text, size)

def arrow(draw, points, text=None, pos=None, hollow=False):
    draw.line(points, fill='black', width=3, joint='curve')
    end, prev = points[-1], points[-2]
    dx, dy = end[0]-prev[0], end[1]-prev[1]
    norm = math.hypot(dx,dy)
    ux, uy = dx/norm, dy/norm
    stem = (end[0]-ux*18, end[1]-uy*18)
    polygon = [end,(stem[0]+uy*10,stem[1]-ux*10),(stem[0]-uy*10,stem[1]+ux*10)]
    draw.polygon(polygon, fill='white' if hollow else 'black', outline='black', width=3)
    if text:
        label(draw,pos,text,26)

def actor(draw, x, y, name):
    draw.ellipse((x-15,y-58,x+15,y-28), outline='black', width=3)
    draw.line([(x,y-28),(x,y+20)],fill='black',width=3)
    draw.line([(x-35,y-5),(x+35,y-5)],fill='black',width=3)
    draw.line([(x,y+20),(x-25,y+58)],fill='black',width=3)
    draw.line([(x,y+20),(x+25,y+58)],fill='black',width=3)
    label(draw,(x,y+86),name,29,True)

image, draw = canvas(1280, 1080)
draw.rectangle((445,10,1260,1060),outline='black',width=3)
label(draw,(855,45),'Phần mềm quản lý trung tâm năng khiếu',27,True)
actors = {'M':(145,195,'Quản lý'),'O':(145,635,'Giáo vụ'),'T':(145,925,'Giảng viên')}
cases = {
    'A':(145,'Quản trị tài khoản\nvà danh mục'),
    'B':(285,'Xử lý khoản chờ\nvà sửa sai chứng từ'),
    'C':(425,'Hồ sơ, ghi danh\nvà thu học phí'),
    'D':(565,'Quản lý lớp\nvà xếp lịch'),
    'E':(705,'Duyệt nghỉ\nvà bố trí học bù'),
    'F':(845,'Xem lịch, điểm danh\nvà nhận xét'),
    'G':(985,'Tra cứu và báo cáo\ntheo phạm vi quyền'),
}
edges = [('M','A'),('M','B'),('M','F'),('O','C'),('O','D'),('O','E'),('O','G'),('T','F'),('T','G')]
for a,b in edges:
    x,y,_=actors[a]; cy,_=cases[b]
    if (a,b)==('M','F'):
        points=[(x+40,y),(340,y),(340,845),(535,845)]
    else:
        points=[(x+40,y),(535,cy)]
    draw.line(points,fill='black',width=3)
for x,y,name in actors.values():
    actor(draw,x,y,name)
arrow(draw,[(95,300),(95,570)],hollow=True)
for y,name in cases.values():
    box(draw,(535,y-50,1205,y+50),name,28,oval=True)
image.save(DIAGRAMS/'use_cases.png')
sources['use_cases'] = 'flowchart LR\n' + '\n'.join(f'  {a}["{v[2]}"]' for a,v in actors.items()) + '\n  subgraph SYS["Phần mềm quản lý trung tâm năng khiếu"]\n' + '\n'.join(f'    {c}(["{v[1].replace(chr(10)," ")}"])' for c,v in cases.items()) + '\n  end\n' + '\n'.join(f'  {a} --- {b}' for a,b in edges) + '\n  M --|> O\n'

image, draw = canvas(1400,1040)
steps=[(160,90,'Mở lớp\nvà xếp đủ lịch'),(690,90,'Lập ghi danh\nChờ thanh toán'),(1190,280,'Nhận tiền\nvà xác nhận thu'),(690,565,'Phiếu thu + ghi danh\ncùng một giao dịch'),(160,565,'Ghi sổ tiền\nchờ xử lý'),(690,790,'Học theo lịch\nchốt điểm danh'),(690,985,'Đối chiếu báo cáo\nhọc phí và tiền chờ')]
for x,y,name in steps:
    box(draw,(x-145,y-53,x+145,y+53),name,28)
arrow(draw,[(305,90),(545,90)])
draw.polygon([(1190,20),(1380,90),(1190,160),(1000,90)],fill='white',outline='black',width=3)
label(draw,(1190,90),'Còn hợp lệ\ntrước nhận tiền?',26)
arrow(draw,[(835,90),(1000,90)])
arrow(draw,[(1190,160),(1190,227)],'Có',(1260,187))
arrow(draw,[(1000,90),(965,90),(965,225),(835,225)],'Không',(928,175))
box(draw,(545,172,835,278),'Không hợp lệ\nchọn lớp khác',26)
arrow(draw,[(690,172),(690,143)])
draw.polygon([(1190,375),(1370,440),(1190,505),(1010,440)],fill='white',outline='black',width=3)
label(draw,(1190,440),'Lưu hợp lệ\nvà thành công?',27)
arrow(draw,[(1190,333),(1190,375)])
arrow(draw,[(1190,505),(1190,565),(835,565)],'Có',(1080,595))
arrow(draw,[(1010,440),(160,440),(160,512)],'Không, đã nhận tiền',(590,410))
arrow(draw,[(690,618),(690,737)])
arrow(draw,[(690,843),(690,932)])
arrow(draw,[(160,618),(160,720)])
box(draw,(10,720,310,855),'Quản lý xác nhận\nghi nhận lại hoặc\ntrả tiền thủ công',26)
arrow(draw,[(160,855),(160,985),(545,985)],'Đã trả lại',(325,940))
arrow(draw,[(310,760),(350,760),(350,565),(545,565)])
label(draw,(440,650),'Ghi nhận lại\nđủ điều kiện',23)
box(draw,(1010,735,1380,845),'Vắng có phép đã duyệt\n→ quyền bù\n→ bố trí và chốt lượt bù',24)
arrow(draw,[(835,790),(1010,790)])
arrow(draw,[(1195,845),(1195,985),(835,985)])
image.save(DIAGRAMS/'workflow.png')
sources['workflow'] = '''flowchart LR
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
'''

def relation(draw, points, left, right, lp, rp):
    draw.line(points,fill='black',width=3,joint='curve')
    label(draw,lp,left,28)
    label(draw,rp,right,28)

image, draw = canvas(1400,700)
nodes = {
    'Course':(200,90),'ClassGroup':(700,90),'Student':(1200,90),
    'Enrollment':(700,340),'Receipt':(200,590),'PaymentIncident':(1200,590),
}
relation(draw,[(345,90),(555,90)],'1','0..*',(365,60),(522,60))
relation(draw,[(700,137),(700,293)],'1','0..*',(735,162),(752,265))
relation(draw,[(1200,137),(1200,340),(845,340)],'1','0..*',(1235,162),(897,310))
relation(draw,[(555,340),(200,340),(200,543)],'1','0..*',(515,310),(252,510))
relation(draw,[(845,370),(1200,370),(1200,543)],'1','0..*',(895,398),(1250,510))
relation(draw,[(345,590),(1055,590)],'0..1','0..1',(405,558),(1000,558))
label(draw,(700,640),'Liên kết sau xử lý',27)
for name,(x,y) in nodes.items():
    box(draw,(x-145,y-47,x+145,y+47),name,29)
image.save(DIAGRAMS/'domain_finance.png')
sources['domain_finance'] = '''classDiagram
  direction LR
  Course "1" -- "0..*" ClassGroup
  ClassGroup "1" -- "0..*" Enrollment
  Student "1" -- "0..*" Enrollment
  Enrollment "1" -- "0..*" Receipt
  Enrollment "1" -- "0..*" PaymentIncident
  Receipt "0..1" -- "0..1" PaymentIncident : linked after resolution
'''

image, draw = canvas(1500,1000)
nodes={'ClassGroup':(220,70),'Room':(750,70),'Instructor':(1280,70),'Enrollment':(220,310),'Lesson':(750,310),'LeaveRequest':(1280,540),'Attendance':(750,540),'MakeupEntitlement':(750,775),'MakeupBooking':(220,775)}
relation(draw,[(370,70),(480,70),(480,310),(600,310)],'1','0..*',(408,40),(555,279))
relation(draw,[(750,117),(750,263)],'1','0..*',(784,142),(795,239))
relation(draw,[(1280,117),(1280,310),(900,310)],'1','0..*',(1315,143),(958,278))
relation(draw,[(370,310),(450,310),(450,540),(600,540)],'1','0..*',(411,338),(556,508))
relation(draw,[(750,357),(750,493)],'1','0..*',(785,382),(795,470))
relation(draw,[(750,587),(750,728)],'1','0..1',(785,611),(795,700))
relation(draw,[(600,775),(370,775)],'1','0..*',(562,742),(417,742))
relation(draw,[(600,340),(520,340),(520,690),(220,690),(220,728)],'1','0..*',(551,366),(272,714))
relation(draw,[(370,285),(440,285),(440,190),(1450,190),(1450,540),(1430,540)],'1','0..*',(410,240),(1460,577))
relation(draw,[(900,310),(1020,310),(1020,540),(1130,540)],'1','0..*',(950,342),(1090,508))
for name,(x,y) in nodes.items():
    box(draw,(x-150,y-47,x+150,y+47),name,28)
label(draw,(750,930),'Attendance thuộc lớp gốc; MakeupBooking dùng Lesson đích',28)
image.save(DIAGRAMS/'domain_learning.png')
sources['domain_learning'] = '''classDiagram
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
'''
for name,source in sources.items():
    (DIAGRAMS/(name+'.mmd')).write_text(source,encoding='utf-8')
documentation=['# Sơ đồ báo cáo tiến độ lần 1 SE100','Nguồn Mermaid và ảnh biểu diễn cùng tập tác nhân, nghiệp vụ và quan hệ. Bội số là số bản ghi lịch sử; điều kiện hiệu lực do BR quy định.']
for name,source in sources.items():
    documentation.append(f'## {name}\n\n```mermaid\n{source}```')
(DIAGRAMS/'SE100_DOT1_DIAGRAMS.md').write_text('\n\n'.join(documentation),encoding='utf-8')
sys.path.insert(0,str(WORK/'vendor'))
import qrcode
import zxingcpp
url='https://docs.google.com/forms/d/e/1FAIpQLSenTD2JN9DCcaVJOOXoAiWOsRG7jEftdgfszZExJ_lw_65Rvg/viewform?usp=header'
qr=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M,box_size=12,border=4)
qr.add_data(url)
qr.make(fit=True)
qrimage=qr.make_image(fill_color='black',back_color='white').convert('RGB')
qrimage.save(DIAGRAMS/'feedback_qr.png')
decoded=zxingcpp.read_barcode(qrimage)
assert decoded and decoded.text==url
print('Rendered four diagrams and verified QR exact URL.')
