#!/bin/sh
# Rebuild portfolio.pdf (tagged) from the live pages: home + four featured cases.
# Usage: sh .orca/build-portfolio-pdf.sh   (run from repo root)
set -eu
PAGES='/ /projects/yangju/ /projects/finsight/ /projects/ontong/ /projects/nca/'
PORT=8766
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
TMP=_print-portfolio.html

css=$(for p in $PAGES; do f=".${p}index.html"; [ "$p" = / ] && f=index.html; grep -o '<link rel="stylesheet" href="[^"]*">' "$f"; done | awk '!seen[$0]++')

cat > "$TMP" <<EOF
<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>문대한 서비스 기획 PM 포트폴리오</title>
$css
<style>.print-part+.print-part{break-before:page}</style></head><body><div id="out"></div>
<script>
(async()=>{const out=document.getElementById('out');
for(const p of '$PAGES'.split(' ')){const t=await (await fetch(p)).text();
const d=new DOMParser().parseFromString(t,'text/html');const w=document.createElement('div');
w.className='print-part '+d.body.className;w.append(d.querySelector('main'));
w.querySelectorAll('img').forEach(i=>i.loading='eager');out.append(w);}
document.title='문대한 서비스 기획 PM 포트폴리오';})();
</script></body></html>
EOF

python3 -m http.server $PORT >/dev/null 2>&1 &
SRV=$!
trap 'kill $SRV; rm -f "$TMP"' EXIT
sleep 1
"$CHROME" --headless=new --disable-gpu --no-pdf-header-footer --virtual-time-budget=15000 \
  --print-to-pdf=portfolio.pdf "http://localhost:$PORT/$TMP" 2>/dev/null
pdfinfo portfolio.pdf | grep -E 'Pages|Tagged'
