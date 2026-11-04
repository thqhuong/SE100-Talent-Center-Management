// Run against the development stack with its fictional seed accounts.
import assert from 'node:assert/strict';
const base = new URL(process.env.STARTER_URL || 'http://127.0.0.1:3000');
async function api(path, { method = 'GET', cookie, body, expected = 200 } = {}) {
  const headers = { Origin: process.env.STARTER_ORIGIN || base.origin.replace('127.0.0.1', 'localhost') };
  if (cookie) headers.Cookie = cookie;
  if (body) headers['Content-Type'] = 'application/json';
  const res = await fetch(new URL('/api/v1' + path, base), {method, headers, body: body ? JSON.stringify(body) : undefined});
  assert.ok([expected].flat().includes(res.status), method + ' ' + path + ' returned ' + res.status);
  return res;
}
async function login(account, role) {
  const res = await api('/auth/login', {method:'POST',body:{email:account+'@harmony.test',password:'HarmonyDemo2026!'},expected:[200,201]});
  const raw = res.headers.get('set-cookie') || '';
  assert.match(raw, /HttpOnly/i);
  const cookie = raw.split(';')[0];
  assert.equal((await (await api('/auth/me',{cookie})).json()).user.role,role);
  return cookie;
}
const home = await fetch(base);
assert.equal(home.status,200);
assert.match(await home.text(),/id=["']root["']/);
await api('/health');
const {programs} = await (await api('/public/programs')).json();
assert.ok(programs.some(p=>/piano/i.test(p.name)) && programs.some(p=>/thanh nhạc/i.test(p.name)));
assert.equal(new Set(programs.map(p=>p.id)).size,programs.length);
await api('/me/schedule',{expected:401});
await api('/auth/login',{method:'POST',body:{email:'an@harmony.test',password:'wrong'},expected:401});
for (const [account,role] of [['manager','MANAGER'],['staff','ACADEMIC_STAFF'],['teacher','TEACHER']]) {
  const cookie=await login(account,role);
  await api('/auth/logout',{method:'POST',cookie,expected:[200,201,204]});
}
const an=await login('an','STUDENT'), binh=await login('binh','STUDENT');
const a=(await (await api('/me/schedule',{cookie:an})).json()).sessions;
const b=(await (await api('/me/schedule',{cookie:binh})).json()).sessions;
assert.ok(a.length && b.length);
assert.ok(a.some(s=>s.mode==='ONSITE') && b.some(s=>s.mode==='ONLINE'));
assert.ok(a.every(s=>!b.some(t=>t.id===s.id)));
await api('/me/sessions/'+encodeURIComponent(a[0].id),{cookie:an});
await api('/me/sessions/'+encodeURIComponent(a[0].id),{cookie:binh,expected:[403,404]});
await api('/auth/logout',{method:'POST',cookie:an,expected:[200,204,201]});
await api('/auth/me',{cookie:an,expected:401});
console.log('Public catalog, all four roles, personal schedules, denied cross-student access and revoked sessions passed.');
