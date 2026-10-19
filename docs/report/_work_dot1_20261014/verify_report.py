from pathlib import Path
from docx import Document
from PIL import Image
import pdfplumber
import json
import re
import sys
import hashlib

WORK=Path(__file__).resolve().parent
sys.path.insert(0,str(WORK/'vendor'))
import zxingcpp
DOCX=WORK.parent/'SE100_BaoCaoTienDo_Dot1_Scope_SRS.docx'
PDF=WORK/'render_final'/'SE100_BaoCaoTienDo_Dot1_Scope_SRS.pdf'
doc=Document(DOCX)
pages=pdfplumber.open(PDF)
assert len(pages.pages)==21
page_text=[p.extract_text() or '' for p in pages.pages]
toc=[]
headings=[]
for p in doc.paragraphs:
    if p.style.name.lower() in ('toc 1','toc 2'):
        name,page=p.text.rsplit('\t',1)
        toc.append((name,int(page)))
    if p.style.name in ('Heading 1','Heading 2'):
        headings.append(p.text)
assert len(toc)==len(headings)==34, (len(toc),len(headings))
assert [x[0] for x in toc]==headings
for name,number in toc:
    assert name in page_text[number-1], (name,number)
for p in pages.pages:
    assert all(c.get('non_stroking_color') in (0,(0,),(0,0,0),[0,0,0],None) for c in p.chars), 'Non-black text'
    assert all(c['x0']>=60 and c['x1']<=p.width-55 and c['top']>=40 and c['bottom']<=p.height-15 for c in p.chars), 'Text outside page margins'
source=(WORK/'report_source.md').read_text(encoding='utf-8')
for prefix,n in [('FR',18),('BR',12),('NFR',8),('UC',5)]:
    actual=set(re.findall(r'\*\*('+prefix+r'\d{2})\s*[—-]',source)) if prefix!='NFR' else set(re.findall(r'\| (NFR\d{2}) \|',source))
    assert actual=={f'{prefix}{i:02}' for i in range(1,n+1)}, (prefix,actual)
assert '24520244' in page_text[0]
assert '[[TOC]]' not in '\n'.join(page_text)
qr=zxingcpp.read_barcode(Image.open(WORK/'render_final'/'page-1.png'))
assert qr and qr.text=='https://docs.google.com/forms/d/e/1FAIpQLSenTD2JN9DCcaVJOOXoAiWOsRG7jEftdgfszZExJ_lw_65Rvg/viewform?usp=header'
assert len(doc.inline_shapes)==5
hashes=json.loads((WORK/'reviewed_v2_hashes.json').read_text())
changed=[p.name for p in (WORK/'render_final').glob('page-*.png') if p.name in hashes and hashlib.sha256(p.read_bytes()).hexdigest()!=hashes[p.name]]
result={'pages':21,'toc_entries_checked':len(toc),'text_color':'black','numbered_heading_count':len(headings),'requirements':{'FR':18,'BR':12,'NFR':8,'UC':5},'inline_images':5,'qr_decoded_from_rendered_cover':True,'changed_pages_since_full_visual_review':changed,'output_bytes':DOCX.stat().st_size}
(WORK/'verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
