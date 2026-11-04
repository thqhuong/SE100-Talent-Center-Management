import { Body, Controller, Get, HttpCode, Inject, Post, Req, Res, UnsupportedMediaTypeException, UseGuards } from '@nestjs/common';
import { Throttle, ThrottlerGuard } from '@nestjs/throttler';
import type { Request, Response } from 'express';
import { AuthService, requireSameOrigin } from './auth.service';

@Controller('auth')
export class AuthController {
  constructor(@Inject(AuthService) private readonly auth: AuthService) {}
  @Post('login') @HttpCode(200) @UseGuards(ThrottlerGuard) @Throttle({ default: {limit:30, ttl:60_000} })
  login(@Body() body: unknown, @Req() req: Request, @Res({passthrough:true}) res: Response) {
    requireSameOrigin(req);
    if (!req.is('application/json')) throw new UnsupportedMediaTypeException('Cần gửi dữ liệu JSON.');
    return this.auth.login(body,req,res);
  }
  @Get('me')
  async me(@Req() req: Request) {
    const {id,name,email,role} = await this.auth.actor(req);
    return {user:{id,name,email,role}};
  }
  @Post('logout') @HttpCode(204)
  logout(@Req() req: Request, @Res({passthrough:true}) res: Response) {
    requireSameOrigin(req);
    return this.auth.logout(req,res);
  }
}
