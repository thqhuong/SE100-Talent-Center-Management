import { useQuery } from '@tanstack/react-query';
import { api } from './api';
import { KeyboardArt, modeLabel, Notice } from './ui';

export default function Catalogue() {
  const programs = useQuery({ queryKey: ['programs'], queryFn: ({ signal }) => api.publicPrograms(signal) });
  return <div className="view">
    <section className="hero">
      <div>
        <p className="eyebrow">Trung tâm đào tạo âm nhạc</p>
        <h1>Học nhạc tại <em>Harmony.</em></h1>
        <p className="lead">Khám phá các chương trình theo bộ môn, trình độ và hình thức học phù hợp với bạn.</p>
        <a className="primary-link" href="#chuong-trinh">Xem chương trình <span aria-hidden="true">↓</span></a>
      </div>
      <KeyboardArt/>
    </section>
    <section aria-labelledby="chuong-trinh" className="section">
      <div className="section-title"><h2 id="chuong-trinh">Chương trình đào tạo</h2>
        {programs.data && <span className="total">{programs.data.length} chương trình</span>}
      </div>
      {programs.isPending ? <Notice>Đang tải chương trình…</Notice>
        : programs.isError ? <Notice alert retry={() => void programs.refetch()}>Chưa tải được chương trình học. Hãy kiểm tra kết nối rồi thử lại.</Notice>
        : !programs.data.length ? <Notice>Trung tâm đang cập nhật danh mục chương trình.</Notice>
        : <div className="program-grid">{programs.data.map((p, i) => <article className="program-card" key={p.id}>
          <div className="program-meta"><span className="mark" aria-hidden="true">{String(i + 1).padStart(2, '0')}</span><span>{p.subject}</span></div>
          <h3>{p.name}</h3>
          <p>{p.description}</p>
          <dl className="program-facts"><div><dt>Trình độ</dt><dd>{p.level}</dd></div><div><dt>Hình thức</dt><dd>{p.deliveryModes.map(modeLabel).join(' · ') || 'Đang cập nhật'}</dd></div></dl>
        </article>)}</div>}
    </section>
  </div>;
}
