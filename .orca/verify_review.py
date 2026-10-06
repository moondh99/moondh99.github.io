"""Focused integrity checks for the approved CV review changes."""
from html.parser import HTMLParser
from pathlib import Path
import re
import subprocess
from urllib.parse import urlparse

root = Path(__file__).resolve().parents[1]
source = (root / 'index.html').read_text()
class Inventory(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids=[]; self.links=[]; self.assets=[]; self.tags=[]
    def handle_starttag(self, tag, attrs):
        a=dict(attrs); self.tags.append((tag,a))
        if 'id' in a: self.ids.append(a['id'])
        if tag=='a': self.links.append(a.get('href',''))
        if tag=='img': self.assets.append(a['src'])
        if tag=='link' and a.get('rel') in ('icon','preload'): self.assets.append(a['href'])
p=Inventory(); p.feed(source)
assert len(p.ids)==len(set(p.ids)), 'Duplicate IDs'
for href in p.links:
    if href.startswith('#'): assert href[1:] in p.ids, href
    elif not urlparse(href).scheme: assert (root/href).is_file(), href
for asset in p.assets: assert (root/asset).is_file(), asset
assert (root/'assets/og-portfolio.jpg').is_file()
assert len([1 for t,a in p.tags if t=='h1'])==1
assert len([1 for t,a in p.tags if t=='article' and a.get('class')=='proj'])==4
assert len([1 for t,a in p.tags if t=='summary'])==8
assert not any(h.startswith('tel:') for h in p.links)
assert not re.search(r'010[-\s]?\d{4}[-\s]?\d{4}', source)
assert '졸업 예정' not in source and '2026.08 졸업' in source
assert '처리 속도' not in source and '처리속도' not in source
assert 'github.com/moondh99/dearlog' in source
assert all('linkedin' not in h.lower() for h in p.links)
assert 'target.matches(\'.proj\')' in source
scripts=re.findall(r'<script>(.*?)</script>',source,re.S)
subprocess.run(['node', '--check'], input='\n'.join(scripts), text=True, check=True, capture_output=True)
print(f'OK — {len(p.ids)} unique IDs; {len(p.links)} links; {len(p.assets)} local assets; 4 projects; 8 keyboard disclosures; no public phone')
