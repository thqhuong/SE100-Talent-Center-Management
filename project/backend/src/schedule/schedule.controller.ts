import { Controller, Get, Inject, NotFoundException, Param, Req } from '@nestjs/common';
import { Prisma } from '@prisma/client';
import type { Request } from 'express';
import { Actor, AuthService } from '../auth/auth.service';
import { DatabaseService } from '../database.service';

function scope(actor: Actor): Prisma.ClassSessionWhereInput {
  const scheduled: Prisma.ClassSessionWhereInput = {
    status: 'SCHEDULED', courseClass: {status:{in:['ONGOING','ENROLLING','COMPLETED']}},
  };
  if (actor.role === 'TEACHER') return {...scheduled, assignedTeacherId:actor.staffId!};
  if (actor.role !== 'STUDENT') return scheduled;
  return {...scheduled, OR:[
    {isPrivateMakeupSession:false,courseClass:{enrollments:{some:{studentId:actor.studentId!,status:'ACTIVE'}}}},
    {makeupBookings:{some:{status:'CONFIRMED',makeupRight:{
      status:'SCHEDULED',expiresAt:{gte:new Date()},enrollment:{studentId:actor.studentId!,status:{in:['ACTIVE','COMPLETED']}},
    }}}},
  ]};
}
const fields = {
  id:true,startTime:true,endTime:true,room:{select:{name:true}},
  courseClass:{select:{name:true,deliveryMode:true,program:{select:{name:true}}}},
} satisfies Prisma.ClassSessionSelect;
function view(session:Prisma.ClassSessionGetPayload<{select:typeof fields}>) {
  return {id:session.id,className:session.courseClass.name,programName:session.courseClass.program.name,
    startsAt:session.startTime,endsAt:session.endTime,mode:session.courseClass.deliveryMode,
    location:session.courseClass.deliveryMode==='ONLINE'?'Phòng học trực tuyến':session.room?.name??'Chưa xếp phòng'};
}

@Controller('me')
export class ScheduleController {
  constructor(@Inject(DatabaseService) private readonly db: DatabaseService,
              @Inject(AuthService) private readonly auth: AuthService) {}
  @Get('schedule')
  async schedule(@Req() req:Request) {
    const actor=await this.auth.actor(req);
    const sessions=await this.db.classSession.findMany({where:scope(actor),select:fields,orderBy:[{startTime:'asc'},{id:'asc'}]});
    return {sessions:sessions.map(view)};
  }
  @Get('sessions/:id')
  async detail(@Req() req:Request,@Param('id') id:string) {
    const actor=await this.auth.actor(req);
    const session=await this.db.classSession.findFirst({where:{AND:[scope(actor),{id}]},select:fields});
    if (!session) throw new NotFoundException('Không tìm thấy buổi học.');
    return {session:view(session)};
  }
}
