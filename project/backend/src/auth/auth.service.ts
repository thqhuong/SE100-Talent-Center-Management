import { BadRequestException, ForbiddenException, Inject, Injectable, UnauthorizedException } from '@nestjs/common';
import { Prisma } from '@prisma/client';
import { createHash, randomBytes } from 'node:crypto';
import { Request, Response } from 'express';
import { DatabaseService } from '../database.service';
import { DUMMY_HASH, verifyPassword } from './password';

const profile = {
  staff: { select: { id: true, fullName: true, role: true, isActive: true } },
  student: { select: { id: true, fullName: true, isActive: true } },
} satisfies Prisma.AccountInclude;
type Account = Prisma.AccountGetPayload<{include: typeof profile}>;
function identity(account: Account) {
  const person = account.staff ?? account.student;
  if (!person?.isActive) throw new UnauthorizedException('Tài khoản không hoạt động.');
  return { id: account.id, name: person.fullName, email: account.email, role: account.staff?.role ?? 'STUDENT' as const };
}
export type Actor = ReturnType<typeof identity> & {staffId: string | null; studentId: string | null};
const name = 'harmony_session';
const ttl = 8 * 60 * 60 * 1000;
const cookieOptions = () => ({
  httpOnly: true, sameSite: 'strict' as const, path: '/api/v1',
  secure: process.env.COOKIE_SECURE === 'true' ||
    (process.env.COOKIE_SECURE !== 'false' && process.env.NODE_ENV === 'production'),
});
function tokenHash(req: Request) {
  const raw = (req.headers.cookie ?? '').split(';').map(v => v.trim()).find(v => v.startsWith(name + '='))?.slice(name.length + 1);
  return raw && /^[a-f0-9]{64}$/.test(raw) ? digest(raw) : null;
}
function digest(token: string) { return createHash('sha256').update(token).digest('hex'); }

@Injectable()
export class AuthService {
  constructor(@Inject(DatabaseService) private readonly db: DatabaseService) {}

  async login(input: unknown, req: Request, res: Response) {
    if (!input || typeof input !== 'object' || !('email' in input) || typeof input.email !== 'string' ||
        !('password' in input) || typeof input.password !== 'string' || input.email.length > 254 ||
        !input.password.length || Buffer.byteLength(input.password) > 512) {
      throw new BadRequestException('Nhập email và mật khẩu hợp lệ.');
    }
    const email = input.email.trim().toLowerCase();
    const account = await this.db.account.findUnique({ where: { email }, include: profile });
    const valid = await verifyPassword(input.password, account?.passwordHash ?? DUMMY_HASH);
    if (!account || !valid) throw new UnauthorizedException('Email hoặc mật khẩu chưa đúng.');
    const user = identity(account);
    const token = randomBytes(32).toString('hex');
    const previous = tokenHash(req);
    await this.db.$transaction([
      this.db.authSession.deleteMany({where:{OR:[{expiresAt:{lte:new Date()}}, ...(previous ? [{tokenHash:previous}] : [])]}}),
      this.db.authSession.create({data:{accountId:account.id,tokenHash:digest(token),expiresAt:new Date(Date.now()+ttl)}}),
    ]);
    res.cookie(name, token, {...cookieOptions(),maxAge:ttl});
    return { user };
  }

  async actor(req: Request): Promise<Actor> {
    const hash = tokenHash(req);
    const session = hash && await this.db.authSession.findFirst({
      where:{tokenHash:hash,expiresAt:{gt:new Date()}}, include:{account:{include:profile}},
    });
    if (!session) throw new UnauthorizedException('Vui lòng đăng nhập.');
    return {...identity(session.account),studentId:session.account.studentId,staffId:session.account.staffId};
  }

  async logout(req: Request, res: Response) {
    const hash = tokenHash(req);
    if (hash) await this.db.authSession.deleteMany({where:{tokenHash:hash}});
    res.clearCookie(name, cookieOptions());
  }
}

export function requireSameOrigin(req: Request): void {
  if (['same-site', 'cross-site'].includes(req.get('Sec-Fetch-Site') ?? '')) {
    throw new ForbiddenException('Yêu cầu phải xuất phát từ ứng dụng.');
  }
  const origin = req.get('Origin');
  if (!origin) return;
  const expected = process.env.PUBLIC_ORIGIN ?? req.protocol + '://' + req.get('host');
  if (origin !== expected) throw new ForbiddenException('Nguồn yêu cầu không hợp lệ.');
}
