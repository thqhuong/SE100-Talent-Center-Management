const { PrismaClient } = require('@prisma/client');
const { encodePassword } = require('./password.cjs');
const db = new PrismaClient();
const fixture = 'harmony-starter-v1';

async function seed() {
  if (process.env.DEMO_SEED !== 'true' || process.env.NODE_ENV === 'production') {
    throw new Error('Demo initialization requires DEMO_SEED=true in a development environment.');
  }
  const password = 'HarmonyDemo2026!';
  const credentials = await Promise.all(Array.from({length: 5}, () => encodePassword(password)));
  await db.$transaction(async tx => {
    await tx.$executeRaw`SELECT pg_advisory_xact_lock(62100601)`;
    if (await tx.seedRun.findUnique({where:{name:fixture}})) return;
    if (await tx.account.count() || await tx.courseClass.count() || await tx.student.count() || await tx.staffUser.count()) {
      throw new Error('Refusing to add demo accounts to a populated database.');
    }

    for (const [i,[alias,fullName,role,staffCode]] of [
      ['manager','Trần Quốc Bảo','MANAGER','QL-01'],
      ['staff','Lê Thu Hà','ACADEMIC_STAFF','GVU-01'],
      ['teacher','Nguyễn Hoàng Nam','TEACHER','GV-01'],
    ].entries()) {
      await tx.account.create({data:{email:alias+'@harmony.test',passwordHash:credentials[i],
        staff:{create:{id:'demo-staff-'+alias,staffCode,fullName,role}}}});
    }
    const room = await tx.room.create({data:{roomCode:'P-101',name:'Phòng Piano P-101',maxHumanCapacity:5}});
    const samples = [
      {alias:'an',student:'Nguyễn Minh An',code:'PIANO',subject:'Piano',name:'Piano cơ bản',classCode:'PN-CB1-K12',mode:'ONSITE',
        topic:'Nhịp phách và vị trí nốt Đô',description:'Gọi tên nốt nhạc, giữ nhịp và phối hợp hai tay trong bài luyện đầu tiên.',
        start:'2026-11-10T18:00:00+07:00',end:'2026-11-10T19:00:00+07:00'},
      {alias:'binh',student:'Trần Gia Bình',code:'VOCAL',subject:'Thanh nhạc',name:'Thanh nhạc nền tảng',classCode:'TN-CB1-K02',mode:'ONLINE',
        topic:'Lấy hơi và giữ cao độ',description:'Luyện tư thế, kiểm soát hơi thở và hát đúng cao độ qua lớp trực tuyến có giảng viên.',
        start:'2026-11-12T19:00:00+07:00',end:'2026-11-12T20:00:00+07:00'},
    ];
    for (const [i,s] of samples.entries()) {
      const subject = await tx.subject.create({data:{code:s.code,name:s.subject,requiresIndividualInstrument:s.mode==='ONSITE'}});
      const program = await tx.program.create({data:{
        code:s.code+'-CB1',name:s.name,levelName:'Cơ bản',objective:s.description,subjectId:subject.id,deliveryModes:[s.mode],
      }});
      const topic = await tx.programTopic.create({data:{programId:program.id,sessionOrder:1,topicCode:s.code+'-01',title:s.topic}});
      await tx.teacherQualification.create({data:{teacherId:'demo-staff-teacher',subjectId:subject.id,levelName:'Cơ bản'}});
      if (s.mode==='ONSITE') {
        await tx.roomEquipment.create({data:{roomId:room.id,subjectId:subject.id,equipmentName:'Đàn piano điện',totalQuantity:5,goodQuantity:5}});
      }
      const course = await tx.courseClass.create({data:{
        classCode:s.classCode,programId:program.id,name:s.name+' · '+s.classCode,classType:'GROUP',deliveryMode:s.mode,status:'ONGOING',
        startDate:new Date(s.start),committedSessionsCount:1,
      }});
      await tx.classSession.create({data:{
        id:'demo-session-'+s.alias,classId:course.id,topicId:topic.id,sessionNumber:1,roomId:s.mode==='ONSITE'?room.id:null,
        assignedTeacherId:'demo-staff-teacher',startTime:new Date(s.start),endTime:new Date(s.end),
      }});
      const learner = await tx.student.create({data:{studentCode:'HV-0'+(i+1),fullName:s.student}});
      await tx.account.create({data:{email:s.alias+'@harmony.test',passwordHash:credentials[i+3],studentId:learner.id}});
      const enrollment = await tx.enrollment.create({data:{enrollmentCode:'GD-0'+(i+1),studentId:learner.id,classId:course.id,
        agreedTuitionFee:2400000,idempotencyKey:'demo-enroll-'+s.alias}});
      await tx.receipt.create({data:{receiptCode:'PT-0'+(i+1),enrollmentId:enrollment.id,payerName:s.student,amount:2400000,
        paymentMethod:'CASH',idempotencyKey:'demo-payment-'+s.alias,createdByStaffId:'demo-staff-staff'}});
    }
    await tx.seedRun.create({data:{name:fixture}});
  }, {timeout:30000});
  console.log('Demo dataset ready.');
}
seed().catch(error => {
  console.error(error instanceof Error && error.constructor === Error ? error.message : 'Demo initialization failed. Check database availability and migrations.');
  process.exitCode = 1;
}).finally(() => db.$disconnect());
