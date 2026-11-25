"""Gera slides PDF e plano PDF (ABNT) com Chrome headless."""
import re, html, sys, base64, pathlib
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path('/Users/diegosouza/Documents/projeto/Aula_senai')
SCR = pathlib.Path(__import__('tempfile').mkdtemp())
OUTDIR = ROOT / 'pdf'
OUTDIR.mkdir(exist_ok=True)
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'


# ---------------------------------------------------------------- plano
def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', t)
    t = re.sub(r'\*([^*]+)\*', r'<i>\1</i>', t)
    t = re.sub(r'~([^~]+)~', r'<sub>\1</sub>', t)
    return t


def plano_html():
    raw = (ROOT / 'plano-de-aula.md').read_text('utf8').replace('\r', '')
    fm = {}
    m = re.match(r'^---\n([\s\S]*?)\n---\n', raw)
    body = raw
    if m:
        for l in m.group(1).split('\n'):
            i = l.find(':')
            if i > 0:
                fm[l[:i].strip()] = l[i + 1:].strip()
        body = raw[m.end():]
    lines = body.split('\n')
    out, in_refs, i = [], False, 0
    while i < len(lines):
        l = lines[i]
        if not l.strip():
            i += 1; continue
        if l.startswith('## '):
            t = l[3:].strip()
            if re.match(r'^REFER[ÊE]NCIAS', t, re.I):
                in_refs = True; out.append(f'<h1 class="refs">{inline(t)}</h1>')
            else:
                out.append(f'<h1>{inline(t)}</h1>')
        elif l.startswith('### '):
            out.append(f'<h2>{inline(l[4:].strip())}</h2>')
        elif l.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].startswith('|'):
                cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-+:?', c) for c in cells):
                    rows.append(cells)
                i += 1
            i -= 1
            h = '<table>' + ''.join(
                '<tr>' + ''.join((f'<th>{inline(c)}</th>' if ri == 0 else f'<td>{inline(c)}</td>') for c in r) + '</tr>'
                for ri, r in enumerate(rows)) + '</table>'
            out.append(h)
        elif l.startswith('- '):
            items = []
            while i < len(lines) and lines[i].startswith('- '):
                items.append(lines[i][2:].strip()); i += 1
            i -= 1
            items[-1] = re.sub(r';\s*$', '.', items[-1])
            out.append('<ol class="al">' + ''.join(f'<li>{inline(t)}</li>' for t in items) + '</ol>')
        elif l.startswith('> '):
            out.append(f'<p class="quote">{inline(l[2:].strip())}</p>')
        elif re.match(r'^(Quadro|Tabela|Figura) \d+', l):
            out.append(f'<p class="cap">{inline(l.strip())}</p>')
        elif l.startswith('Fonte:'):
            out.append(f'<p class="src">{inline(l.strip())}</p>')
        else:
            out.append(f'<p class="{"ref" if in_refs else "body"}">{inline(l.strip())}</p>')
        i += 1

    capa = f'''<div class="capa">
<p class="c b">{inline(fm.get("instituicao",""))}</p>
<p class="c" style="margin-top:3.2cm">{inline(fm.get("autor",""))}</p>
<p class="c b" style="margin-top:5.3cm">{inline(fm.get("titulo",""))}:</p>
<p class="c b nocaps">{inline(fm.get("subtitulo",""))}</p>
<p class="nat">{inline(fm.get("natureza",""))}</p>
<div class="foot"><p class="c">{inline(fm.get("local",""))}</p><p class="c">{inline(fm.get("ano",""))}</p></div>
</div>'''
    css = '''
@page{size:A4;margin:3cm 2cm 2cm 3cm;
  @top-right{content:counter(page);font:10pt Arial,Helvetica,sans-serif;vertical-align:bottom;padding-bottom:0.6cm}}
@page:first{@top-right{content:none}}
html{font-family:Arial,Helvetica,sans-serif;font-size:12pt;color:#000}
body{margin:0}
p{margin:0}
.capa{height:24.6cm;position:relative;page-break-after:always;text-align:center;line-height:1.5}
.capa .c{text-transform:uppercase}.capa .nocaps{text-transform:none}.capa .b{font-weight:bold}
.capa .nat{margin:3.2cm 0 0 8cm;text-align:justify;line-height:1.15}
.capa .foot{position:absolute;bottom:0;left:0;right:0}
p.body{text-align:justify;text-indent:1.25cm;line-height:1.5}
h1{font-size:12pt;font-weight:bold;text-transform:uppercase;line-height:1.5;margin:18pt 0;break-after:avoid}
h2{font-size:12pt;font-weight:bold;line-height:1.5;margin:18pt 0;break-after:avoid}
h1.refs{text-align:center;break-before:page;margin-top:0}
ol.al{list-style:none;counter-reset:al;margin:0;padding:0 0 0 calc(1.25cm + 0.7cm);line-height:1.5;text-align:justify}
ol.al li{counter-increment:al;position:relative}
ol.al li::before{content:counter(al, lower-alpha) ")";position:absolute;left:-0.7cm}
.quote{margin:18pt 0 18pt 4cm;font-size:10pt;line-height:1;text-align:justify}
.cap{font-size:10pt;margin:18pt 0 3pt;break-after:avoid}
.src{font-size:10pt;margin:3pt 0 18pt}
table{width:100%;border-collapse:collapse;font-size:10pt;line-height:1.15}
th,td{border:0.75pt solid #000;padding:2.5pt 4.5pt;vertical-align:middle;text-align:left}
th{background:#d9d9d9;text-align:center}
tr{break-inside:avoid}
thead{display:table-header-group}
p.ref{text-align:left;line-height:1;margin-bottom:12pt}
'''
    return f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Plano de aula</title><style>{css}</style></head><body>{capa}{"".join(out)}</body></html>'


def main():
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME, headless=True)

        # ---------- plano
        f = SCR / 'plano.html'
        f.write_text(plano_html(), 'utf8')
        pg = b.new_page()
        pg.goto(f.as_uri()); pg.wait_for_timeout(500)
        pg.pdf(path=str(OUTDIR / 'Plano-de-aula_Diego-Souza-Matos.pdf'), prefer_css_page_size=True, print_background=True)
        pg.close()

        # ---------- slides
        ctx = b.new_context(viewport={'width': 1600, 'height': 900}, device_scale_factor=1.5)
        pg = ctx.new_page()
        pg.goto((ROOT / 'slides' / 'aula.html').as_uri() + '?static')
        pg.wait_for_timeout(2500)
        n = pg.evaluate("document.querySelectorAll('section.slide').length")
        shots = []
        for k in range(n):
            if k: pg.evaluate("document.body.dispatchEvent(new KeyboardEvent('keydown',{key:'ArrowRight',bubbles:true}))")
            pg.wait_for_timeout(1800)
            fn = SCR / f'slide{k+1:02d}.jpg'
            pg.screenshot(path=str(fn), type='jpeg', quality=88)
            shots.append(fn)
        ctx.close()
        imgs = ''.join(f'<div class="p"><img src="data:image/jpeg;base64,{base64.b64encode(s.read_bytes()).decode()}"></div>' for s in shots)
        doc = ('<!doctype html><html><head><meta charset="utf-8"><title>Slides</title><style>'
               '@page{size:16in 9in;margin:0}body{margin:0}.p{width:16in;height:9in;page-break-after:always;overflow:hidden}'
               '.p:last-child{page-break-after:auto}img{width:100%;height:100%;display:block}</style></head><body>'
               + imgs + '</body></html>')
        f = SCR / 'slides_pdf.html'
        f.write_text(doc, 'utf8')
        pg = b.new_page()
        pg.goto(f.as_uri()); pg.wait_for_timeout(800)
        pg.pdf(path=str(OUTDIR / 'Slides_Diego-Souza-Matos.pdf'), prefer_css_page_size=True, print_background=True)
        b.close()
    print('ok', n, 'slides')


if __name__ == '__main__':
    main()
