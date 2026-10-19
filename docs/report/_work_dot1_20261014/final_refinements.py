from pathlib import Path
import hashlib
import json
work=Path(__file__).resolve().parent
p=work/'report_source.md'
s=p.read_text(encoding='utf-8')
s=s.replace('có thể hủy nếu chưa thu tiền.', 'có thể hủy khi chưa có phiếu học phí hiệu lực, giữ liên kết và lịch sử khoản chờ nếu có.')
s=s.replace('hủy hồ sơ chưa thu không sinh phiếu thu.', 'hủy ghi danh chưa có phiếu hiệu lực không sinh phiếu mới và không xóa khoản tiền chờ.')
s=s.replace('sửa điểm danh, xử lý khoản chờ có người thực hiện và thời điểm;', 'sửa điểm danh có người thực hiện và thời điểm;')
p.write_text(s,encoding='utf-8')
hashes={x.name:hashlib.sha256(x.read_bytes()).hexdigest() for x in (work/'render_final').glob('page-*.png')}
(work/'reviewed_v2_hashes.json').write_text(json.dumps(hashes),encoding='utf-8')
print('Applied final text refinements and recorded reviewed page hashes.')
