// ═══════════════════════════════════════════════════════════════════════
// CryptoNova — Early Access Coupon Verifier
// POST /api/verify-coupon  { code: "XXXX" }  → { valid: true/false }
//
// ENV VAR required in Vercel dashboard (ea project only):
//   EA_COUPON_CODES  — comma-separated list of valid codes (case-insensitive)
//   Example: GENESIS2026,NOVA-LEADER-01,NOVA-LEADER-02
// ═══════════════════════════════════════════════════════════════════════

export default async function handler(req, res) {
  const origin = req.headers.origin || '';
  const allowed = ['https://ea.cryptonova.ai', 'https://ea.crypto-nova.app', 'vercel.app'];
  const isAllowed = allowed.some(o => origin.includes(o)) || origin === '';
  res.setHeader('Access-Control-Allow-Origin', isAllowed ? origin : 'https://ea.cryptonova.ai');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  let body;
  try { body = typeof req.body === 'string' ? JSON.parse(req.body) : req.body; }
  catch { return res.status(400).json({ valid: false }); }

  const { code } = body || {};
  if (!code || typeof code !== 'string') return res.status(400).json({ valid: false });

  const raw = process.env.EA_COUPON_CODES || '';
  if (!raw) {
    console.warn('EA_COUPON_CODES env var not set on this Vercel project');
    return res.status(200).json({ valid: false, note: 'no codes configured' });
  }

  const codes = raw.split(',').map(c => c.trim().toUpperCase()).filter(Boolean);
  const valid = codes.includes(code.trim().toUpperCase());

  // Slow down invalid attempts — makes brute-force impractical
  if (!valid) {
    await new Promise(r => setTimeout(r, 700));
    return res.status(200).json({ valid: false });
  }

  console.log(`EA coupon redeemed: ${code.trim().toUpperCase().slice(0, 4)}****`);
  return res.status(200).json({ valid: true });
}
