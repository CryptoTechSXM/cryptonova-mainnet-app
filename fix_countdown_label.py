import os
fpath = r"C:\CryptoNova-Mainnet-App\mainnet\countdown.html"
with open(fpath, "r", encoding="utf-8") as f:
    content = f.read()
OLD = 'July 26, 2026 &nbsp;·&nbsp; <em>12:00 PM EST</em>'
NEW = 'July 26, 2026 &nbsp;·&nbsp; <em>3:00 PM EST</em>'
if OLD not in content:
    print("ERROR: text not found")
else:
    content = content.replace(OLD, NEW)
    tmp = fpath + ".new"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    os.replace(tmp, fpath)
    print("Done — countdown now shows 3:00 PM EST")
