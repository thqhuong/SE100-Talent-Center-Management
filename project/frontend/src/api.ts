export type Role = 'MANAGER' | 'ACADEMIC_STAFF' | 'TEACHER' | 'STUDENT';
export interface User { id: string; name: string; email: string; role: Role }
export interface Program {
  id: string;
  name: string;
  subject: string;
  level: string;
  description: string;
  deliveryModes: string[];
}
export interface Session {
  id: string;
  className: string;
  programName: string;
  startsAt: string;
  endsAt: string;
  mode: string;
  location: string;
}

export class ApiError extends Error {
  constructor(public readonly status: number) {
    super('HTTP ' + status);
  }
}

async function request<T>(path: string, init: RequestInit = {}): Promise<T> {
  const response = await fetch('/api/v1' + path, {
    credentials: 'same-origin',
    cache: 'no-store',
    ...init,
    headers: { Accept: 'application/json', ...(init.body ? { 'Content-Type': 'application/json' } : {}), ...init.headers },
  });
  if (!response.ok) throw new ApiError(response.status);
  const body = await response.text();
  return body ? JSON.parse(body) as T : undefined as T;
}

export const api = {
  async publicPrograms(signal: AbortSignal) {
    return (await request<{ programs: Program[] }>('/public/programs', { signal })).programs;
  },
  async currentUser(signal: AbortSignal) {
    try { return (await request<{ user: User }>('/auth/me', { signal })).user; }
    catch (error) {
      if (error instanceof ApiError && error.status === 401) return null;
      throw error;
    }
  },
  async login(email: string, password: string) {
    return (await request<{ user: User }>('/auth/login', { method: 'POST', body: JSON.stringify({ email, password }) })).user;
  },
  logout() { return request<void>('/auth/logout', { method: 'POST' }); },
  async schedule(signal: AbortSignal) {
    return (await request<{ sessions: Session[] }>('/me/schedule', { signal })).sessions;
  },
};
