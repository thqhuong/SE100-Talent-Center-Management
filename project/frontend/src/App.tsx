import { useEffect, useState } from 'react';
import { Button } from 'antd';
import { useQuery, useQueryClient } from '@tanstack/react-query';
import { Link, Navigate, Route, Routes, useLocation, useNavigate } from 'react-router-dom';
import { api, ApiError, type User } from './api';
import Catalogue from './Catalogue';
import Login from './Login';
import Workspace from './Workspace';
import { Notice } from './ui';

export default function App() {
  const client = useQueryClient();
  const navigate = useNavigate();
  const location = useLocation();
  const viewer = useQuery({queryKey: ['viewer'], queryFn: ({signal}) => api.currentUser(signal)});
  const user = viewer.data ?? null;
  const [ending, setEnding] = useState(false);
  const [logoutError,setLogoutError] = useState(false);

  useEffect(() => {
    const sync = () => {
      client.removeQueries({queryKey:['schedule']});
      void client.invalidateQueries({queryKey:['viewer']});
    };
    const onStorage = (event: StorageEvent) => { if (event.key === 'harmony.session.changed') sync(); };
    window.addEventListener('storage',onStorage);
    return () => window.removeEventListener('storage',onStorage);
  },[client]);

  useEffect(() => {
    document.title = ({ '/dang-nhap':'Đăng nhập', '/tai-khoan':'Lịch của bạn', '/':'Chương trình đào tạo' }[location.pathname] || 'Trang không tồn tại') + ' · Harmony';
    window.scrollTo(0,0);
  },[location.pathname]);

  function changeUser(next:User|null) {
    void client.cancelQueries({queryKey:['viewer']});
    client.removeQueries({queryKey:['schedule']});
    client.setQueryData(['viewer'],next);
    try { localStorage.setItem('harmony.session.changed',String(Date.now())); } catch { /* Some private browsers disable storage. */ }
    setLogoutError(false);
    navigate(next ? '/tai-khoan' : '/', {replace:true});
  }
  async function logout() {
    setEnding(true); setLogoutError(false);
    try { await api.logout(); changeUser(null); }
    catch (e) { if (e instanceof ApiError && e.status === 401) changeUser(null); else setLogoutError(true); }
    finally { setEnding(false); }
  }
  const wait = <Notice>Đang kiểm tra tài khoản…</Notice>;
  const failed = <Notice alert retry={()=>void viewer.refetch()}>Chưa kết nối được với máy chủ. Hãy thử lại.</Notice>;
  return <div className="site"><a className="skip" href="#main">Đến nội dung</a>
    <header className="mast"><div className="container mast-inner">
      <Link className="brand" to="/" aria-label="Harmony – Trang chủ"><img src="/harmony.svg" alt="" width="39" height="39"/><span><strong>Harmony</strong><small>Trung tâm âm nhạc</small></span></Link>
      <nav aria-label="Điều hướng chính">
        <Link to="/" className="nav-link" aria-current={location.pathname==='/'?'page':undefined}>Chương trình</Link>
        {user ? <>
          <Link className="nav-link" to="/tai-khoan" aria-current={location.pathname==='/tai-khoan'?'page':undefined}>Lịch của tôi</Link>
          <Button onClick={()=>void logout()} loading={ending}>Đăng xuất</Button></>
          : <Link className="header-login" to="/dang-nhap" aria-current={location.pathname==='/dang-nhap'?'page':undefined}>Đăng nhập <span aria-hidden="true">↗</span></Link>}
      </nav>
    </div></header>
    <main id="main" className="container content" tabIndex={-1}>
      {logoutError && <Notice alert retry={()=>void logout()}>Chưa thể đăng xuất. Hãy thử lại.</Notice>}
      <Routes>
        <Route path="/" element={<Catalogue/>}/>
        <Route path="/dang-nhap" element={viewer.isPending?wait:user?<Navigate to="/tai-khoan" replace/>:<Login onLogin={changeUser}/>}/>
        <Route path="/tai-khoan" element={viewer.isPending?wait:viewer.isError?failed:user?<Workspace key={user.id} user={user}/>:<Navigate to="/dang-nhap" replace/>}/>
        <Route path="*" element={<section className="login-page"><h1>Không tìm thấy trang</h1><Link className="primary-link" to="/">Về trang chương trình</Link></section>}/>
      </Routes>
    </main>
    <footer className="site-footer"><div className="container">Harmony <span aria-hidden="true">/</span> Trung tâm đào tạo âm nhạc</div></footer>
  </div>;
}
