#!/bin/sh
# Rebuild portfolio.pdf (tagged, 16:9 slides) from .orca/portfolio-slides.html.
# Usage: sh .orca/build-portfolio-pdf.sh   (run from repo root)
set -eu
PORT=8766
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

python3 -m http.server $PORT >/dev/null 2>&1 &
SRV=$!
trap 'kill $SRV' EXIT
sleep 1
"$CHROME" --headless=new --disable-gpu --no-pdf-header-footer --virtual-time-budget=15000 \
  --print-to-pdf=portfolio.pdf "http://localhost:$PORT/.orca/portfolio-slides.html" 2>/dev/null
pdfinfo portfolio.pdf | grep -E 'Pages|Page size|Tagged'
