"""
set_mainnet_gate.py — Update all 3 mainnet gate timestamps to July 26, 2026.
  Early Access (ea.cryptonova.ai):  July 26 12:00pm EDT = 2026-07-26T16:00:00Z
  Main        (cryptonova.ai):      July 26  3:00pm EDT = 2026-07-26T19:00:00Z

Run from C:\\CryptoNova-Mainnet-App:
  python set_mainnet_gate.py
"""
import re, os

BASE = r"C:\CryptoNova-Mainnet-App"

EA_OLD_DATE   = '2026-07-19T13:00:00Z'   # 9am EDT — old EA open
EA_NEW_DATE   = '2026-07-26T16:00:00Z'   # 12pm EDT — new EA open

MAIN_OLD_DATE = '2026-07-19T16:00:00Z'   # 12pm EDT — old main open
MAIN_NEW_DATE = '2026-07-26T19:00:00Z'   # 3pm EDT  — new main open

# countdown.html has an older date too
OLD_COUNTDOWN = '2026-06-25T16:00:00Z'

EDITS = [
    # (file, old_string, new_string, description)
    (
        r"ea\index.html",
        EA_OLD_DATE,
        EA_NEW_DATE,
        "EA gate timestamp"
    ),
    (
        r"mainnet\index.html",
        MAIN_OLD_DATE,
        MAIN_NEW_DATE,
        "Main gate timestamp"
    ),
    (
        r"mainnet\countdown.html",
        OLD_COUNTDOWN,
        MAIN_NEW_DATE,
        "Countdown LAUNCH_UTC (old June date)"
    ),
    (
        r"mainnet\countdown.html",
        MAIN_OLD_DATE,
        MAIN_NEW_DATE,
        "Countdown LAUNCH_UTC (July 19 reference)"
    ),
    (
        r"mainnet\countdown.html",
        "Launching July 19",
        "Launching July 26",
        "Countdown page title"
    ),
    (
        r"mainnet\countdown.html",
        "July 19",
        "July 26",
        "Any remaining July 19 text"
    ),
    (
        r"mainnet\index.html",
        "Launching July 19",
        "Launching July 26",
        "Main index title if present"
    ),
]

total = 0
for (rel_path, old, new, desc) in EDITS:
    fpath = os.path.join(BASE, rel_path)
    if not os.path.exists(fpath):
        print(f"  SKIP (not found): {rel_path}")
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    count = content.count(old)
    if count == 0:
        print(f"  no match — {desc} in {rel_path}")
        continue
    content = content.replace(old, new)
    tmp = fpath + ".new"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    os.replace(tmp, fpath)
    print(f"  ✅ {count}x  {desc}  ({rel_path})")
    total += count

print(f"\nDone. {total} total replacements.")
print("\nVerify tail of each file:")
for rel in [r"ea\index.html", r"mainnet\index.html", r"mainnet\countdown.html"]:
    fpath = os.path.join(BASE, rel)
    if not os.path.exists(fpath): continue
    with open(fpath, "rb") as f:
        f.seek(max(0, os.path.getsize(fpath) - 80))
        tail = f.read().decode("utf-8", errors="replace").strip()
    ok = tail.endswith("</html>") or tail.endswith("</html>\n")
    print(f"  {'✅' if ok else '❌ TRUNCATED'} {rel}: ...{tail[-40:]!r}")

print("\nNEXT:")
print("  git add -A")
print("  git commit -m \"chore: set mainnet gate to July 26 (12pm EA / 3pm Main EDT)\"")
print("  git push origin <branch>")
