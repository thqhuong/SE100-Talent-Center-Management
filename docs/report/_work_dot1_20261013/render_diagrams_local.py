from pathlib import Path
import re
from PIL import Image, ImageDraw, ImageFont

BASE = Path(__file__).resolve().parent.parent.parent.parent
DIAGRAMS = BASE / 'docs' / 'diagrams'
FONT = Path('C:/Windows/Fonts/arial.ttf')
BOLD = Path('C:/Windows/Fonts/arialbd.ttf')


def canvas(width, height):
    image = Image.new('RGB', (width, height), 'white')
    return image, ImageDraw.Draw(image)


def lines(text):
    return text.split('\n')


def text_center(draw, center, text, size=28, bold=False):
    font = ImageFont.truetype(str(BOLD if bold else FONT), size)
    rows = lines(text)
    line_height = size * 1.35
    top = center[1] - len(rows) * line_height / 2
    for row in rows:
        bounds = draw.textbbox((0, 0), row, font=font)
        draw.text((center[0] - (bounds[2] - bounds[0]) / 2, top - bounds[1]), row, fill='#111111', font=font)
        top += line_height


def box(draw, bounds, text, size=28, bold=False, fill='white', ellipse=False):
    if ellipse:
        draw.ellipse(bounds, fill=fill, outline='#555555', width=3)
    else:
        draw.rounded_rectangle(bounds, radius=10, fill=fill, outline='#555555', width=3)
    text_center(draw, ((bounds[0] + bounds[2]) / 2, (bounds[1] + bounds[3]) / 2), text, size, bold)


def arrow(draw, points, label=None, label_pos=None):
    draw.line(points, fill='#555555', width=3, joint='curve')
    end, previous = points[-1], points[-2]
    dx, dy = end[0] - previous[0], end[1] - previous[1]
    length = (dx * dx + dy * dy) ** .5
    ux, uy = dx / length, dy / length
    bx, by = end[0] - ux * 13, end[1] - uy * 13
    draw.polygon([end, (bx + uy * 6, by - ux * 6), (bx - uy * 6, by + ux * 6)], fill='#555555')
    if label:
        text_center(draw, label_pos, label, 24)


image, draw = canvas(1100, 870)
draw.rounded_rectangle((395, 15, 1080, 850), radius=14, fill='white', outline='#777777', width=3)
text_center(draw, (738, 52), 'Phạm vi phần mềm', 30, True)
actors = [(150, 180, 'Quản lý'), (150, 440, 'Giáo vụ'), (150, 705, 'Giảng viên')]
for x, y, label in actors:
    box(draw, (25, y - 43, 275, y + 43), label, 30, True, '#f2f2f2')
cases = [
    (150, 'Tài khoản và danh mục'),
    (330, 'Hồ sơ, ghi danh\nvà thu học phí'),
    (525, 'Lớp, lịch, điểm danh\nvà học bù'),
    (735, 'Báo cáo và tra cứu'),
]
for y, label in cases:
    box(draw, (490, y - 65, 1020, y + 65), label, 28, ellipse=True)
for start, end in [(180,150),(180,330),(180,735),(440,330),(440,525),(440,735),(705,525),(705,735)]:
    draw.line([(275,start),(490,end)], fill='#888888', width=2)
text_center(draw, (345, 793), 'Theo quyền\nđược cấp', 20)
image.save(DIAGRAMS / 'use_cases.png')
(DIAGRAMS / 'use_cases.mmd').write_text('''flowchart LR
  M["Quản lý"]
  O["Giáo vụ"]
  T["Giảng viên"]
  subgraph SYS["Phạm vi phần mềm"]
    A(["Tài khoản và danh mục"])
    B(["Hồ sơ, ghi danh và thu học phí"])
    C(["Lớp, lịch, điểm danh và học bù"])
    D(["Báo cáo và tra cứu"])
  end
  M --- A
  M --- B
  M --- D
  O --- B
  O --- C(["Lớp, lịch, điểm danh và học bù"])
  O --- D
  T --- C
  T --- D
''', encoding='utf-8')

image, draw = canvas(1080, 1270)
nodes = [
    (65, 'Mở lớp và xếp đủ lịch'),
    (215, 'Lập ghi danh chờ thanh toán'),
    (365, 'Giáo vụ xác nhận đã nhận đủ học phí'),
    (680, 'Lưu phiếu thu và kích hoạt ghi danh'),
    (835, 'Chốt điểm danh và nhận xét buổi học'),
    (1125, 'Đối chiếu sĩ số, chuyên cần và tiền thu'),
]
for y, label in nodes:
    box(draw, (230,y-46,1050,y+46), label, 28)
for start, end in [(111,169),(261,319),(411,470),(605,634),(726,789),(881,930),(1065,1079)]:
    arrow(draw, [(640,start),(640,end)])
draw.polygon([(640,470),(890,540),(640,610),(390,540)], fill='#f2f2f2', outline='#555555', width=3)
text_center(draw, (640,540), 'Còn chỗ và\nđiều kiện hợp lệ?', 28)
text_center(draw, (672,624), 'Có', 23)
box(draw, (10,470,310,610), 'Từ chối giao dịch\nGiáo vụ xử lý', 25)
arrow(draw, [(390,540),(310,540)], 'Không', (352,510))
draw.polygon([(640,930),(890,1000),(640,1070),(390,1000)], fill='#f2f2f2', outline='#555555', width=3)
text_center(draw, (640,1000), 'Vắng có phép\nđã được duyệt?', 28)
box(draw, (10,920,305,1080), 'Tạo quyền bù\nBố trí và chốt\nlượt bù', 25)
arrow(draw, [(390,1000),(305,1000)], 'Có', (347,970))
arrow(draw, [(157,1080),(157,1125),(230,1125)])
text_center(draw, (708,1078), 'Không', 18)
image.save(DIAGRAMS / 'workflow.png')

image, draw = canvas(1180, 670)
nodes = {
    'Course': (170,80), 'ClassGroup': (555,80), 'Lesson': (940,80),
    'Student': (170,300), 'Enrollment': (555,300), 'Attendance': (940,300),
    'Receipt': (170,545), 'MakeupEntitlement': (555,545), 'MakeupBooking': (940,545),
}
for name, (x,y) in nodes.items():
    box(draw, (x-145,y-43,x+145,y+43), name, 25 if len(name)>13 else 29, True)
relations = [
    ('Course','ClassGroup','1 → 0..*'),('ClassGroup','Lesson','1 → 0..*'),
    ('Student','Enrollment','1 → 0..*'),('Enrollment','Attendance','1 → 0..*'),
    ('MakeupEntitlement','MakeupBooking','1 → 0..*'),
]
for left,right,label in relations:
    lx,ly=nodes[left]; rx,ry=nodes[right]
    draw.line([(lx+145,ly),(rx-145,ry)],fill='#555555',width=3)
    text_center(draw, ((lx+rx)/2,ly-25), label, 20)
for top,bottom,label in [('ClassGroup','Enrollment','1 → 0..*'),('Lesson','Attendance','1 → 0..*')]:
    tx,ty=nodes[top]; bx,by=nodes[bottom]
    draw.line([(tx,ty+43),(bx,by-43)],fill='#555555',width=3)
    text_center(draw,(tx+68,(ty+by)/2),label,20)
draw.line([(555,343),(555,420),(170,420),(170,502)],fill='#555555',width=3)
text_center(draw,(365,398),'Enrollment 1 → Receipt 0..*',20)
draw.line([(940,343),(940,445),(555,445),(555,502)],fill='#555555',width=3)
text_center(draw,(760,467),'Attendance 1 → Quyền bù 0..1',20)
draw.line([(1085,80),(1140,80),(1140,545),(1085,545)],fill='#555555',width=3)
text_center(draw,(940,615),'Lesson 1 → MakeupBooking 0..*',20)
image.save(DIAGRAMS / 'domain.png')
(DIAGRAMS / 'domain.mmd').write_text('''classDiagram
  direction LR
  Course "1" -- "0..*" ClassGroup
  ClassGroup "1" -- "0..*" Lesson
  ClassGroup "1" -- "0..*" Enrollment
  Student "1" -- "0..*" Enrollment
  Enrollment "1" -- "0..*" Receipt
  Enrollment "1" -- "0..*" Attendance
  Lesson "1" -- "0..*" Attendance
  Attendance "1" -- "0..1" MakeupEntitlement
  MakeupEntitlement "1" -- "0..*" MakeupBooking
  Lesson "1" -- "0..*" MakeupBooking
''', encoding='utf-8')

parts = ['# Sơ đồ báo cáo tiến độ đợt 1 SE100\n',
         'Nguồn Mermaid dưới đây giữ các quan hệ để chỉnh sửa. Ảnh PNG được dựng cục bộ từ cùng mô hình vì dịch vụ render từ xa không khả dụng.\n']
for filename in ['use_cases','workflow','domain']:
    parts.append('## ' + filename + '\n\n```mermaid\n' + (DIAGRAMS/(filename+'.mmd')).read_text(encoding='utf-8') + '```\n')
(DIAGRAMS/'SE100_DOT1_DIAGRAMS.md').write_text('\n'.join(parts),encoding='utf-8')
print('Created three local diagram images and Mermaid sources.')
