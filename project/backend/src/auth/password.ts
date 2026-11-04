import { scrypt, timingSafeEqual } from 'node:crypto';
import { promisify } from 'node:util';

const derive = promisify(scrypt);
// Unknown accounts perform the same expensive check as existing accounts.
export const DUMMY_HASH = '00000000000000000000000000000000:' + '00'.repeat(64);

export async function verifyPassword(password: string, encoded: string): Promise<boolean> {
  if (!/^[a-f0-9]{32}:[a-f0-9]{128}$/.test(encoded)) return false;
  const [salt, hash] = encoded.split(':');
  const actual = await derive(password, salt, 64) as Buffer;
  return timingSafeEqual(actual, Buffer.from(hash, 'hex'));
}
