const { PrismaClient } = require('@prisma/client');
const { randomUUID } = require('node:crypto');
const { encodePassword } = require('./password.cjs');
const db = new PrismaClient();

async function createAdmin() {
  const email = process.env.ADMIN_EMAIL?.trim().toLowerCase();
  const password = process.env.ADMIN_PASSWORD;
  const fullName = process.env.ADMIN_NAME?.trim() || 'Quản lý';
  if (!email || email.length > 254 || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email) ||
      !password || password.length < 12 || Buffer.byteLength(password) > 512) {
    throw new Error('Set ADMIN_EMAIL and a password of at least 12 characters in ADMIN_PASSWORD.');
  }
  const passwordHash = await encodePassword(password);
  await db.$transaction(async tx => {
    await tx.$executeRaw`SELECT pg_advisory_xact_lock(62100601)`;
    if (await tx.staffUser.count({where:{role:'MANAGER'}})) throw new Error('A manager already exists.');
    if (await tx.account.findUnique({where:{email}})) throw new Error('An account with that email already exists.');
    await tx.account.create({data:{email,passwordHash,staff:{create:{
      staffCode:'QL-'+randomUUID(),fullName,role:'MANAGER',
    }}}});
  });
  console.log('Initial manager created.');
}
createAdmin().catch(error => {
  console.error(error instanceof Error && error.constructor === Error ? error.message : 'Could not create manager. Check database availability and migrations.');
  process.exitCode = 1;
}).finally(() => db.$disconnect());
