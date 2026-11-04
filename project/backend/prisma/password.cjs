const { randomBytes, scrypt } = require('node:crypto');
const { promisify } = require('node:util');
const derive = promisify(scrypt);
async function encodePassword(password) {
  const salt = randomBytes(16).toString('hex');
  const key = await derive(password, salt, 64);
  return salt + ':' + key.toString('hex');
}
module.exports = { encodePassword };
