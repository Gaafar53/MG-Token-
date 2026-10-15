// MG-CHAIN PHONE LOCK - قفل البلوكشين من التليفون
const fs = require('fs');
const crypto = require('crypto');

const FILE = 'mg_chain.json';
const LOCK_FILE = 'PHONE_BLOCKCHAIN_LOCKED.json';

if (!fs.existsSync(FILE)) {
  console.log('❌ مفيش mg_chain.json - شغل python mg.py الاول');
  process.exit(1);
}

let chain = JSON.parse(fs.readFileSync(FILE, 'utf8'));

// قفل كل بلوك
let locked = chain.map(b => {
  let hash = crypto.createHash('sha256').update(JSON.stringify(b)).digest('hex');
  return { ...b, locked_hash: hash, locked_at: new Date().toISOString(), locked_by: 'PHONE' };
});

fs.writeFileSync(LOCK_FILE, JSON.stringify(locked, null, 2));
console.log(`🔒 تم قفل ${locked.length} بلوك`);
console.log(`📦 محفوظ في ${LOCK_FILE}`);
console.log(`🪙 Token: 0x148f95e0364b1d290676f791e7c9500cb839eeaa`);
console.log(`👛 Wallet: 0x7564ac8dc5dcfa570a11dd3b21f579aee8e41982`);

// اعمله read-only
require('child_process').execSync(`chmod 444 ${LOCK_FILE} && chmod 444 ${FILE}`);
console.log('✅ البلوكشين بقى مقفول ضد التعديل');
