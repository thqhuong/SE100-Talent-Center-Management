from __future__ import annotations

import base64
import concurrent.futures
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

from docx import Document
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor


WORK = Path(__file__).resolve().parent
COURSE = WORK.parent.parent.parent
DIAGRAMS = COURSE / 'docs' / 'diagrams'
OUTPUT = WORK.parent / 'SE100_BaoCaoTienDo_Dot1_Scope_SRS.docx'
SOURCE = WORK / 'report_source.md'

THEME = '''%%{init: {"theme":"base","themeVariables":{"primaryColor":"#ffffff","primaryTextColor":"#000000","primaryBorderColor":"#555555","lineColor":"#555555","secondaryColor":"#f2f2f2","tertiaryColor":"#ffffff","fontFamily":"Arial","fontSize":"17px"},"flowchart":{"htmlLabels":false,"curve":"linear"}}}%%
'''

SOURCES = {
    'use_cases': THEME + '''flowchart LR
    M["Quản lý"]
    O["Giáo vụ"]
    T["Giảng viên"]
    subgraph SYS["Phần mềm quản lý trung tâm dạy năng khiếu"]
        A(["Quản trị tài khoản và danh mục"])
        B(["Quản lý hồ sơ và ghi danh"])
        C(["Thu học phí và chứng từ"])
        D(["Quản lý lớp và lịch"])
        E(["Điểm danh và nhận xét"])
        F(["Duyệt nghỉ và bố trí học bù"])
        G(["Báo cáo và tra cứu"])
    end
    M --- A
    M --- C
    M --- G
    O --- B
    O --- C
    O --- D
    O --- F
    O --- G
    T --- D
    T --- E
    T --- G
''',
    'workflow': THEME + '''flowchart TD
    A["Mở lớp và xếp đủ lịch"] --> B["Lập ghi danh chờ thanh toán"]
    B --> C["Giáo vụ xác nhận đã nhận đủ học phí"]
    C --> D{"Còn chỗ và mọi điều kiện hợp lệ?"}
    D -->|"Không"| E["Từ chối giao dịch; Giáo vụ xử lý"]
    D -->|"Có"| F["Lưu phiếu thu và kích hoạt ghi danh"]
    F --> G["Học theo lịch; chốt điểm danh và nhận xét"]
    G --> H{"Vắng có phép đã được duyệt?"}
    H -->|"Có"| I["Tạo quyền bù; bố trí và chốt lượt bù"]
    H -->|"Không"| J["Đối chiếu sĩ số, chuyên cần và tiền thu"]
    I --> J
''',
    'domain': THEME + '''classDiagram
    direction LR
    class Student
    class Course
    class ClassGroup
    class Enrollment
    class Receipt
    class Lesson
    class Instructor
    class Room
    class Attendance
    class MakeupEntitlement
    class MakeupBooking
    Course "1" -- "0..*" ClassGroup
    ClassGroup "1" -- "0..*" Enrollment
    Student "1" -- "0..*" Enrollment
    Enrollment "1" -- "0..*" Receipt
    ClassGroup "1" -- "0..*" Lesson
    Instructor "1" -- "0..*" Lesson
    Room "1" -- "0..*" Lesson
    Lesson "1" -- "0..*" Attendance
    Enrollment "1" -- "0..*" Attendance
    Attendance "1" -- "0..1" MakeupEntitlement
    MakeupEntitlement "1" -- "0..*" MakeupBooking
    Lesson "1" -- "0..*" MakeupBooking
''',
}


def render_diagram(item):
    name, source = item
    (DIAGRAMS / (name + '.mmd')).write_text(source, encoding='utf-8')
    png = DIAGRAMS / (name + '.png')
    if png.exists():
        return {'name': name, 'cached': True, 'bytes': png.stat().st_size}
    data = json.dumps({'code': source, 'mermaid': {'theme': 'base'}}, ensure_ascii=False).encode('utf-8')
    encoded = base64.urlsafe_b64encode(data).decode('ascii')
    request = urllib.request.Request('https://mermaid.ink/img/' + encoded + '?type=png&scale=2&bgColor=white', headers={'Accept': 'image/png'})
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            result = response.read()
    except urllib.error.HTTPError as error:
        raise RuntimeError(f'{name}: {error.code} {error.read().decode("utf-8", errors="replace")}') from error
    if not result.startswith(b'\x89PNG'):
        raise RuntimeError(f'{name}: unexpected response {result[:150]!r}')
    png.write_bytes(result)
    return {'name': name, 'bytes': len(result)}


def format_inline(paragraph, text):
    for index, part in enumerate(re.split(r'\*\*(.*?)\*\*', text)):
        if not part:
            continue
        run = paragraph.add_run(part)
        run.bold = index % 2 == 1
        run.font.color.rgb = RGBColor(0, 0, 0)
        run.font.name = 'Times New Roman'


def set_cell_shading(cell, fill):
    props = cell._tc.get_or_add_tcPr()
    shade = OxmlElement('w:shd')
    shade.set(qn('w:fill'), fill)
    props.append(shade)


def add_table(document, lines):
    rows = [[cell.strip() for cell in line.strip().strip('|').split('|')] for line in lines]
    rows = [r for r in rows if not all(re.fullmatch(r'[:\- ]+', c) for c in r)]
    columns = len(rows[0])
    table = document.add_table(rows=0, cols=columns)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    width = 16.0
    if columns == 2:
        widths = [4.2, 11.8]
    elif columns == 3:
        widths = [7.2, 3.0, 5.8] if 'Thành viên' in rows[0][0] and 'MSSV' in rows[0][1] else [3.1, 3.1, 9.8]
    elif columns == 4:
        widths = [3.1, 2.5, 2.5, 7.9]
    else:
        widths = [width / columns] * columns
    if 'Thành viên' in rows[0][0] and 'Đầu ra' in rows[0][1]:
        widths = [4.2, 7.6, 4.2]
    if rows[0][0] == 'Phiên bản':
        widths = [1.7, 2.4, 7.3, 4.6]
    for column, col_width in zip(table.columns, widths):
        column.width = Cm(col_width)
    borders = OxmlElement('w:tblBorders')
    for edge in ['top', 'left', 'bottom', 'right', 'insideH', 'insideV']:
        border = OxmlElement('w:' + edge)
        border.set(qn('w:val'), 'single')
        border.set(qn('w:sz'), '4')
        border.set(qn('w:color'), 'D9D9D9')
        borders.append(border)
    table._tbl.tblPr.append(borders)
    for row_index, texts in enumerate(rows):
        row = table.add_row()
        no_split = OxmlElement('w:cantSplit')
        row._tr.get_or_add_trPr().append(no_split)
        if row_index == 0:
            repeat = OxmlElement('w:tblHeader')
            row._tr.get_or_add_trPr().append(repeat)
        for column_index, (cell, cell_text) in enumerate(zip(row.cells, texts)):
            cell.width = Cm(widths[column_index])
            cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            props = cell._tc.get_or_add_tcPr()
            margins = OxmlElement('w:tcMar')
            for side in ['top', 'left', 'bottom', 'right']:
                value = OxmlElement('w:' + side)
                value.set(qn('w:w'), '75' if side in ['top', 'bottom'] else '95')
                value.set(qn('w:type'), 'dxa')
                margins.append(value)
            props.append(margins)
            paragraph = cell.paragraphs[0]
            paragraph.paragraph_format.space_after = Pt(0)
            paragraph.paragraph_format.line_spacing = 1.03
            paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT
            format_inline(paragraph, cell_text)
            for run in paragraph.runs:
                run.font.size = Pt(11.5)
                if row_index == 0:
                    run.bold = True
            if row_index == 0:
                set_cell_shading(cell, 'EAEAEA')
            if cell_text.isdecimal() or cell_text == '__________________':
                paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    after = document.add_paragraph()
    after.paragraph_format.space_after = Pt(2)
    after.paragraph_format.line_spacing = Pt(3)
    after.paragraph_format.space_before = Pt(0)
    after.add_run().font.size = Pt(3)


def make_document():
    document = Document()
    section = document.sections[0]
    section.page_width = Cm(21)
    section.page_height = Cm(29.7)
    section.top_margin = Cm(2)
    section.bottom_margin = Cm(2)
    section.left_margin = Cm(2.5)
    section.right_margin = Cm(2.5)
    section.header_distance = Cm(0.9)
    section.footer_distance = Cm(0.9)
    for name in ['Normal', 'Title', 'Subtitle', 'Heading 1', 'Heading 2', 'Caption', 'List Bullet', 'List Number']:
        style = document.styles[name]
        style.font.name = 'Times New Roman'
        style.font.color.rgb = RGBColor(0, 0, 0)
        fonts = style.element.get_or_add_rPr().find(qn('w:rFonts'))
        if fonts is not None:
            for attribute in list(fonts.attrib):
                if 'theme' in attribute.lower():
                    del fonts.attrib[attribute]
            for attribute in ['ascii', 'hAnsi', 'eastAsia', 'cs']:
                fonts.set(qn('w:' + attribute), 'Times New Roman')
        for border in style.element.findall('.//' + qn('w:pBdr')):
            border.getparent().remove(border)
        props = style.paragraph_format
        props.space_after = Pt(6)
        props.line_spacing = 1.1
        props.widow_control = True
    document.styles['Normal'].font.size = Pt(12)
    document.styles['Title'].font.size = Pt(20)
    document.styles['Title'].font.bold = True
    document.styles['Heading 1'].font.size = Pt(16)
    document.styles['Heading 1'].font.bold = True
    document.styles['Heading 1'].paragraph_format.space_before = Pt(0)
    document.styles['Heading 1'].paragraph_format.space_after = Pt(10)
    document.styles['Heading 2'].font.size = Pt(13)
    document.styles['Heading 2'].font.bold = True
    document.styles['Heading 2'].paragraph_format.space_before = Pt(9)
    document.styles['Heading 2'].paragraph_format.space_after = Pt(6)
    document.styles['Subtitle'].font.size = Pt(16)
    document.styles['Subtitle'].font.bold = True
    document.styles['Caption'].font.size = Pt(10.5)
    document.styles['Caption'].font.italic = True
    document.styles['Caption'].font.bold = False
    document.styles['Caption'].paragraph_format.space_after = Pt(8)
    document.styles['List Bullet'].font.size = Pt(12)
    document.styles['List Number'].font.size = Pt(12)
    for name in ['Normal', 'Title', 'Subtitle', 'Heading 1', 'Heading 2', 'Caption', 'List Bullet', 'List Number']:
        rpr = document.styles[name].element.get_or_add_rPr()
        size_cs = rpr.find(qn('w:szCs'))
        if size_cs is None:
            size_cs = OxmlElement('w:szCs')
            rpr.append(size_cs)
        size_cs.set(qn('w:val'), str(round(document.styles[name].font.size.pt * 2)))
    footer = section.footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    footer.add_run('SE100  •  Báo cáo đợt 1  •  ').font.size = Pt(9)
    field = OxmlElement('w:fldSimple')
    field.set(qn('w:instr'), 'PAGE')
    footer._p.append(field)
    core = document.core_properties
    core.title = 'Báo cáo tiến độ đợt 1 phần mềm quản lý trung tâm dạy năng khiếu'
    core.subject = 'SE100 Scope và SRS'
    core.author = 'Nhóm SE100 — Trần Hữu Quốc Hướng và các thành viên'
    core.keywords = 'SE100, OOAD, scope, SRS, quản lý trung tâm năng khiếu'
    core.comments = 'Dự thảo v0.1; chính sách nghiệp vụ đề xuất chưa có xác nhận khảo sát.'
    lines = SOURCE.read_text(encoding='utf-8').splitlines()
    i = 0
    title_seen = False
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        if line == '<!-- page -->':
            document.add_page_break()
            i += 1
            continue
        if line.startswith('|'):
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                table_lines.append(lines[i])
                i += 1
            add_table(document, table_lines)
            continue
        diagram = re.fullmatch(r'\[\[diagram:(.+?)\|(.+?)\]\]', line)
        if diagram:
            from PIL import Image
            path = DIAGRAMS / diagram.group(1)
            with Image.open(path) as img:
                image_width, image_height = img.size
            max_width_cm, max_height_cm = 16, 12.3
            picture_width_cm = min(max_width_cm, max_height_cm * image_width / image_height)
            paragraph = document.add_paragraph()
            paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            paragraph.paragraph_format.keep_with_next = True
            paragraph.add_run().add_picture(str(path), width=Cm(picture_width_cm))
            caption = document.add_paragraph(diagram.group(2), style='Caption')
            caption.alignment = WD_ALIGN_PARAGRAPH.CENTER
            i += 1
            continue
        if line.startswith('# '):
            if not title_seen:
                paragraph = document.add_paragraph(line[2:], style='Title')
                paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
                title_seen = True
            else:
                document.add_paragraph(line[2:], style='Heading 1')
        elif line.startswith('## '):
            style = 'Subtitle' if len(document.paragraphs) <= 2 else 'Heading 2'
            paragraph = document.add_paragraph(line[3:], style=style)
            if style == 'Subtitle':
                paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        elif line.startswith('- '):
            paragraph = document.add_paragraph(style='List Bullet')
            format_inline(paragraph, line[2:])
        elif re.match(r'^\d+\. ', line):
            paragraph = document.add_paragraph()
            paragraph.paragraph_format.left_indent = Cm(0.45)
            paragraph.paragraph_format.first_line_indent = Cm(-0.45)
            format_inline(paragraph, line)
        else:
            paragraph = document.add_paragraph()
            paragraph.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            format_inline(paragraph, line)
        i += 1
    document.save(OUTPUT)
    print(json.dumps({'output': str(OUTPUT), 'bytes': OUTPUT.stat().st_size, 'planned_pages': 1 + SOURCE.read_text(encoding='utf-8').count('<!-- page -->')}, ensure_ascii=False))


if __name__ == '__main__':
    if '--doc-only' not in sys.argv:
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            for result in executor.map(render_diagram, SOURCES.items()):
                print(json.dumps(result, ensure_ascii=False))
    make_document()
