"""
set_mainnet_gate.py — Update ALL mainnet gate timestamps to July 26, 2026.
  Early Access (ea.cryptonova.ai):  July 26 12:00pm EDT = 2026-07-26T16:00:00Z
  Main        (cryptonova.ai):      July 26  3:00pm EDT = 2026-07-26T19:00:00Z

Run from C:\\CryptoNova-Mainnet-App:
  python set_mainnet_gate.py
"""
import os

BASE = r"C:\CryptoNova-Mainnet-App"

EDITS = [
    # ea/index.html — gate redirect
    ("ea/index.html",  "2026-07-19T13:00:00Z", "2026-07-26T16:00:00Z", "ea/index.html EA_OPEN"),
    # ea/coupon.html — coupon page countdown
    ("ea/coupon.html", "2026-07-19T13:00:00Z", "2026-07-26T16:00:00Z", "coupon.html EA_OPEN"),
    ("ea/coupon.html", "2026-07-19T16:00:00Z", "2026-07-26T19:00:00Z", "coupon.html MAIN_OPEN"),
    # coupon.html display text
    ("ea/coupon.html", "July 19, 2026 &nbsp;·&nbsp; <em>9:00 AM EST</em>",
                       "July 26, 2026 &nbsp;·&nbsp; <em>12:00 PM EST</em>", "coupon.html display date"),
    ("ea/coupon.html", "9:00 AM EST",  "12:00 PM EST", "coupon.html any remaining 9am text"),
    ("ea/coupon.html", "July 19, 2026", "July 26, 2026", "coupon.html any remaining July 19 text"),
    # mainnet/index.html — main gate redirect
    ("mainnet/index.html", "2026-07-19T16:00:00Z", "2026-07-26T19:00:00Z", "mainnet/index.html LAUNCH"),
    # mainnet/countdown.html — countdown page
    ("mainnet/countdown.html", "2026-07-19T16:00:00Z", "2026-07-26T19:00:00Z", "countdown.html LAUNCH (Jul19)"),
    ("mainnet/countdown.html", "2026-06-25T16:00:00Z", "2026-07-26T19:00:00Z", "countdown.html LAUNCH (Jun25 old)"),
    ("mainnet/countdown.html", "July 19, 2026", "July 26, 2026", "countdown.html July 19 text"),
    ("mainnet/countdown.html", "Launching July 19", "Launching July 26", "countdown.html title"),
    ("mainnet/countdown.html", "July 19", "July 26", "countdown.html remaining July 19"),
]

total = 0
files_changed = set()
for (rel_path, old, new, desc) in EDITS:
    fpath = os.path.join(BASE, rel_path.replace("/", os.sep))
    if not os.path.exists(fpath):
        print(f"  SKIP (not found): {rel_path}")
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    count = content.count(old)
    if count == 0:
        print(f"  --  no match: {desc}")
        continue
    content = content.replace(old, new)
    tmp = fpath + ".new"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    os.replace(tmp, fpath)
    files_changed.add(rel_path)
    print(f"  ✅ {count}x  {desc}")
    total += count

print(f"\nDone. {total} replacements across {len(files_changed)} file(s).")

# Truncation check
print("\nTail check:")
for rel in ["ea/index.html", "ea/coupon.html", "mainnet/index.html", "mainnet/countdown.html"]:
    fpath = os.path.join(BASE, rel.replace("/", os.sep))
    if not os.path.exists(fpath): continue
    with open(fpath, "rb") as f:
        f.seek(max(0, os.path.getsize(fpath) - 60))
        tail = f.read().decode("utf-8", errors="replace").strip()
    ok = "</html>" in tail
    print(f"  {'✅' if ok else '❌ TRUNCATED'} {rel}")
