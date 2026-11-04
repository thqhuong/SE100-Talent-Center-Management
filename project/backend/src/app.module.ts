import { Controller, Get, Inject, Module, ServiceUnavailableException } from '@nestjs/common';
import { ThrottlerModule } from '@nestjs/throttler';
import { DatabaseService } from './database.service';
import { AuthController } from './auth/auth.controller';
import { AuthService } from './auth/auth.service';
import { ScheduleController } from './schedule/schedule.controller';

@Controller()
class CatalogController {
  constructor(@Inject(DatabaseService) private readonly db:DatabaseService) {}
  @Get('health')
  async health() {
    try { await this.db.$queryRaw`SELECT 1`; return {status:'ok'}; }
    catch {throw new ServiceUnavailableException('Cơ sở dữ liệu chưa sẵn sàng.');}
  }
  @Get('public/programs')
  async programs() {
    const programs=await this.db.program.findMany({where:{isActive:true},orderBy:{code:'asc'},
      select:{id:true,name:true,subject:{select:{name:true}},levelName:true,objective:true,deliveryModes:true}});
    return {programs:programs.map(p=>({id:p.id,name:p.name,subject:p.subject.name,level:p.levelName,
      description:p.objective??'',deliveryModes:p.deliveryModes}))};
  }
}
@Module({
  imports:[ThrottlerModule.forRoot([{name:'default',ttl:60_000,limit:30}])],
  providers:[DatabaseService, AuthService],
  controllers:[CatalogController, AuthController, ScheduleController],
})
export class AppModule {}
