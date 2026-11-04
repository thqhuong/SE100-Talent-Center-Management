import { useEffect } from 'react';
import { useQuery, useQueryClient } from '@tanstack/react-query';
import { Link } from 'react-router-dom';
import { api, ApiError, type User, type Session, type Role } from './api';
import { modeLabel, Notice, roleNames } from './ui';

const timeZone = 'Asia/Ho_Chi_Minh';
const clock = new Intl.DateTimeFormat('vi-VN', { hour: '2-digit', minute: '2-digit', timeZone });
const day = new Intl.DateTimeFormat('vi-VN', { weekday: 'long', day: 'numeric', month: 'numeric', year: 'numeric', timeZone });
const scope: Record<Role, { title: string; description: string; empty: string }> = {
  MANAGER: { title: 'Lịch hoạt động', description: 'Theo dõi các buổi đào tạo của trung tâm theo lớp và hình thức học.', empty: 'Trung tâm chưa có buổi học nào trong lịch.' },
  ACADEMIC_STAFF: { title: 'Lịch điều phối', description: 'Tra cứu thời gian, lớp và địa điểm để hướng dẫn học viên.', empty: 'Chưa có buổi học để điều phối.' },
  TEACHER: { title: 'Lịch giảng dạy', description: 'Các buổi dạy được phân công cho bạn tại trung tâm và trực tuyến.', empty: 'Bạn chưa được phân công buổi dạy nào.' },
  STUDENT: { title: 'Lịch học của tôi', description: 'Xem chương trình, thời gian và địa điểm các buổi học của bạn.', empty: 'Bạn chưa có buổi học nào. Hãy liên hệ Giáo vụ để kiểm tra ghi danh.' },
};

function SessionRow({session}: {session: Session}) {
  const start = new Date(session.startsAt), end = new Date(session.endsAt);
  return <li className="session-row">
    <div className="session-time"><strong>{clock.format(start)} – {clock.format(end)}</strong><span>{day.format(start)}</span></div>
    <div className="session-class"><strong>{session.className}</strong><span>{session.programName}</span></div>
    <div className="session-location"><span className={session.mode === 'ONLINE' ? 'mode online' : 'mode'}>{modeLabel(session.mode)}</span><span>{session.location}</span></div>
  </li>;
}

export default function Workspace({user}:{user: User}) {
  const client = useQueryClient();
  const list = useQuery({queryKey:['schedule',user.id], queryFn:({signal})=>api.schedule(signal)});
  useEffect(() => {
    if (list.error instanceof ApiError && list.error.status === 401) void client.invalidateQueries({queryKey:['viewer']});
  },[list.error,client]);
  const info = scope[user.role];
  return <div className="workspace view">
    <div className="workspace-intro">
      <p className="eyebrow">{roleNames[user.role]} · Không gian cá nhân</p>
      <h1>{info.title}</h1><p className="lead">{info.description}</p>
    </div>
    <div className="workspace-grid"><section className="schedule" aria-labelledby="sessions">
      <div className="section-title"><h2 id="sessions">Danh sách buổi học</h2>{list.data && <span className="total">{list.data.length} buổi</span>}</div>
      {list.isPending ? <Notice>Đang tải lịch…</Notice>
        : list.isError ? <Notice alert retry={() => void list.refetch()}>Chưa tải được lịch. Hãy kiểm tra kết nối và thử lại.</Notice>
        : !list.data.length ? <Notice>{info.empty}</Notice>
        : <ul className="session-list">{[...list.data].sort((a,b)=>Date.parse(a.startsAt)-Date.parse(b.startsAt)).map(s=><SessionRow session={s} key={s.id}/>)}</ul>}
      <p className="footnote">Thời gian hiển thị theo giờ Việt Nam (UTC+7).</p>
    </section>
    <aside className="profile"><p className="eyebrow">Tài khoản hiện tại</p><h2>{user.name}</h2>
      <p className="profile-email">{user.email}</p><span className="profile-role">{roleNames[user.role]}</span>
      <Link to="/" className="profile-link">Xem chương trình đào tạo <span aria-hidden="true">→</span></Link>
    </aside></div>
  </div>;
}
