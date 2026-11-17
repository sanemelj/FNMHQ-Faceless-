#!/usr/bin/env python3
"""FNMHQ Facebook photo card 1080x1350. Usage: card.py spec.json out.jpg
spec: {photo, pos, kicker, big, sub, lines:[...], q, credit, accent}"""
import json,sys,os,base64
from playwright.sync_api import sync_playwright
spec=json.load(open(sys.argv[1])); out=sys.argv[2]; here=os.path.dirname(os.path.abspath(__file__))
def b64(p,m): return f"data:{m};base64,"+base64.b64encode(open(p,'rb').read()).decode()
ph=os.path.abspath(spec['photo']); acc=spec.get('accent','#e2282e')
font=lambda n:b64(os.path.join(here,n),'font/woff2')
lines=''.join(f'<div class="ln">{l}</div>' for l in spec.get('lines',[]))
html=f"""<html><head><style>
@font-face{{font-family:AN;src:url({font('anton.woff2')})}}
@font-face{{font-family:IT;src:url({font('inter-tight-latin-800-normal.woff2')});font-weight:800}}
@font-face{{font-family:IT5;src:url({font('inter-tight-latin-500-normal.woff2')})}}
@font-face{{font-family:JB;src:url({font('jetbrains-mono-latin-500-normal.woff2')})}}
body{{margin:0;width:540px;height:675px;overflow:hidden;background:#000}}
.bg{{position:absolute;inset:0;background:url({b64(ph,'image/jpeg')}) {spec.get('pos','50% 30%')}/cover}}
.gr{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.55) 0%,rgba(0,0,0,0) 28%,rgba(0,0,0,.15) 48%,rgba(0,0,0,.92) 100%)}}
.crest{{position:absolute;right:16px;top:14px;width:62px}}
.kick{{position:absolute;left:24px;top:24px;font:800 17px IT;color:#fff;background:{acc};padding:5px 10px;letter-spacing:.06em;text-transform:uppercase}}
.box{{position:absolute;left:24px;right:24px;bottom:46px}}
.big{{font-family:AN;font-size:{spec.get('bigsize',92)}px;line-height:.92;color:#fff;text-transform:uppercase;text-shadow:0 4px 18px rgba(0,0,0,.6)}}
.big b{{color:#f2b632;font-weight:400}}
.sub{{font:800 22px IT;color:#f2b632;text-transform:uppercase;margin-top:8px;letter-spacing:.02em}}
.ln{{font:500 19px IT5;color:#fff;margin-top:6px}}
.q{{display:inline-block;margin-top:12px;font:800 19px IT;color:#141010;background:#fff;padding:6px 12px}}
.cr{{position:absolute;left:24px;bottom:16px;font:500 10px JB;color:rgba(255,255,255,.75);letter-spacing:.03em}}
.wm{{position:absolute;right:20px;bottom:14px;font:400 16px AN;color:#fff;letter-spacing:.04em}}.wm i{{color:{acc};font-style:normal}}
</style></head><body><div class="bg"></div><div class="gr"></div>
<img class="crest" src="{b64(os.path.join(here,'crest.png'),'image/png')}">
<div class="kick">{spec.get('kicker','')}</div>
<div class="box"><div class="big">{spec['big']}</div><div class="sub">{spec.get('sub','')}</div>{lines}{('<div class="q">'+spec['q']+'</div>') if spec.get('q') else ''}</div>
<div class="cr">{spec.get('credit','')}</div><div class="wm">FNM<i>HQ</i></div></body></html>"""
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':540,'height':675},device_scale_factor=2)
    pg.set_content(html); pg.wait_for_timeout(400); pg.screenshot(path=out,type='jpeg',quality=92); b.close()
print('ok',out)
