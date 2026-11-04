import { useState, type FormEvent } from 'react';
import { Button, Input } from 'antd';
import { ApiError, api, type User } from './api';
import { Notice } from './ui';

interface Props { onLogin: (user: User) => void }

export default function Login({ onLogin }: Props) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState('');

  async function submit(event: FormEvent) {
    event.preventDefault();
    if (busy) return;
    setBusy(true); setError('');
    try { onLogin(await api.login(email.trim(), password)); }
    catch (e) {
      setError(e instanceof ApiError && e.status === 401
        ? 'Email hoặc mật khẩu chưa đúng. Hãy kiểm tra lại thông tin đăng nhập.'
        : 'Không thể đăng nhập lúc này. Hãy kiểm tra kết nối và thử lại.');
    } finally { setBusy(false); }
  }

  return <section className="login-page view">
    <p className="eyebrow">Tài khoản Harmony</p>
    <h1>Đăng nhập</h1>
    <p className="lead">Dùng tài khoản trung tâm đã cấp để mở lịch của bạn.</p>
    <form className="login-form" onSubmit={submit} aria-busy={busy}>
      <label htmlFor="email">Email</label>
      <Input id="email" type="email" autoComplete="username" required value={email} onChange={e => setEmail(e.target.value)} disabled={busy}/>
      <label htmlFor="password">Mật khẩu</label>
      <Input.Password id="password" autoComplete="current-password" required value={password} onChange={e => setPassword(e.target.value)} disabled={busy}/>
      {error && <Notice alert>{error}</Notice>}
      <Button type="primary" htmlType="submit" loading={busy} block>Đăng nhập</Button>
    </form>
    {import.meta.env.DEV && import.meta.env.VITE_DEMO_HINTS === 'true' &&
      <details className="demo-details"><summary>Tài khoản để thử trên máy cá nhân</summary>
        <p>Chọn người dùng để điền thông tin, sau đó nhấn Đăng nhập.</p>
        <div className="demo-options">{[
          ['an','Học viên An'],['binh','Học viên Bình'],['teacher','Giảng viên'],['staff','Giáo vụ'],['manager','Quản lý'],
        ].map(([key,label]) => <button type="button" key={key} disabled={busy} onClick={() => {
          setEmail(key + '@harmony.test'); setPassword('HarmonyDemo2026!'); setError('');
        }}>{label}</button>)}</div>
      </details>}
  </section>;
}
