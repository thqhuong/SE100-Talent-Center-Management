import type { ReactNode } from 'react';
import type { Role } from './api';

export const roleNames: Record<Role, string> = {
  MANAGER: 'Quản lý', ACADEMIC_STAFF: 'Giáo vụ', TEACHER: 'Giảng viên', STUDENT: 'Học viên',
};

export function modeLabel(mode: string) {
  if (mode === 'ONLINE') return 'Trực tuyến';
  if (mode === 'ONSITE') return 'Tại trung tâm';
  return mode;
}

export function Notice({ children, retry, alert = false }: { children: ReactNode; retry?: () => void; alert?: boolean }) {
  return <div className="notice" role={alert ? 'alert' : 'status'}>
    <span>{children}</span>
    {retry && <button className="text-action" onClick={retry}>Thử lại</button>}
  </div>;
}

export function KeyboardArt() {
  return <svg className="keyboard-art" aria-hidden="true" viewBox="0 0 400 228" fill="none">
    <rect width="400" height="228" rx="4" fill="#DAE4D8"/>
    <circle cx="333" cy="4" r="90" fill="#C1D3C0"/>
    <circle cx="51" cy="219" r="108" fill="#C9D8C7"/>
    <g transform="translate(63 37) rotate(-7 135 72)">
      <rect x="0" y="0" width="278" height="144" rx="8" fill="#284A3F"/>
      <rect x="11" y="11" width="256" height="26" rx="3" fill="#345B4D"/>
      <g fill="#D9E6D8"><circle cx="27" cy="24" r="3"/><circle cx="38" cy="24" r="3"/></g>
      <path d="M218 24h33" stroke="#A9BDA8" strokeWidth="2"/>
      {Array.from({ length: 14 }, (_, i) => <rect key={i} x={11 + i * 18.3} y="44" width="17.1" height="89" rx="1.8" fill="#FCF9ED"/>)}
      {[0,1,3,4,5,7,8,10,11,12].map(i => <rect key={i} x={22.6 + i * 18.3} y="43" width="11.5" height="55" rx="1.5" fill="#253E34"/>)}
    </g>
  </svg>;
}
