// Gera ../plano-de-aula.docx a partir de ../plano-de-aula.md com diagramação ABNT
// NBR 14724 (apresentação), NBR 6024 (numeração de seções e alíneas),
// NBR 10520 (citações) e NBR 6023 (referências).
// Uso: cd tools && node gerar-plano-docx.js
const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, Header,
  AlignmentType, WidthType, BorderStyle, ShadingType, LevelFormat, PageNumber,
  VerticalAlign, TabStopType,
} = require('docx');

const SRC = path.join(__dirname, '..', 'plano-de-aula.md');
const OUT = path.join(__dirname, '..', 'plano-de-aula.docx');

// ---------- medidas (DXA: 1 cm ≈ 567)
const CM = 567;
const PAGE = { w: 11906, h: 16838 };                       // A4
const MARGIN = { top: 3 * CM, left: 3 * CM, bottom: 2 * CM, right: 2 * CM };
const TEXT_W = PAGE.w - MARGIN.left - MARGIN.right;        // largura útil
const FONT = 'Arial';
const SZ = 24, SZ_SMALL = 20;                              // 12 pt e 10 pt (meios-pontos)
const L15 = 360, L1 = 240;                                 // entrelinhas 1,5 e simples

// ---------- leitura do markdown
const raw = fs.readFileSync(SRC, 'utf8').replace(/\r/g, '');
const fm = {};
let body = raw;
const m = raw.match(/^---\n([\s\S]*?)\n---\n/);
if (m) {
  m[1].split('\n').forEach(l => { const i = l.indexOf(':'); if (i > 0) fm[l.slice(0, i).trim()] = l.slice(i + 1).trim(); });
  body = raw.slice(m[0].length);
}

// ---------- texto com marcações inline: **negrito**, *itálico*, ~subscrito~
function runs(text, opt = {}) {
  const out = [];
  const re = /(\*\*[^*]+\*\*|\*[^*]+\*|~[^~]+~)/g;
  let last = 0, mm;
  const base = { font: FONT, size: opt.size || SZ, bold: opt.bold, italics: opt.italics, allCaps: opt.caps };
  while ((mm = re.exec(text))) {
    if (mm.index > last) out.push(new TextRun({ ...base, text: text.slice(last, mm.index) }));
    const t = mm[0];
    if (t.startsWith('**')) out.push(new TextRun({ ...base, text: t.slice(2, -2), bold: true }));
    else if (t.startsWith('~')) out.push(new TextRun({ ...base, text: t.slice(1, -1), subScript: true }));
    else out.push(new TextRun({ ...base, text: t.slice(1, -1), italics: true }));
    last = mm.index + t.length;
  }
  if (last < text.length) out.push(new TextRun({ ...base, text: text.slice(last) }));
  return out;
}

// ---------- blocos
const P = {
  body: t => new Paragraph({ children: runs(t), alignment: AlignmentType.JUSTIFIED,
    indent: { firstLine: Math.round(1.25 * CM) }, spacing: { line: L15, before: 0, after: 0 } }),
  h1: t => new Paragraph({ children: runs(t, { bold: true, caps: true }), alignment: AlignmentType.LEFT,
    keepNext: true, spacing: { line: L15, before: L15, after: L15 } }),
  h2: t => new Paragraph({ children: runs(t, { bold: true }), alignment: AlignmentType.LEFT,
    keepNext: true, spacing: { line: L15, before: L15, after: L15 } }),
  hRef: t => new Paragraph({ children: runs(t, { bold: true, caps: true }), alignment: AlignmentType.CENTER,
    keepNext: true, spacing: { line: L15, before: 0, after: L15 }, pageBreakBefore: true }),
  quote: t => new Paragraph({ children: runs(t, { size: SZ_SMALL }), alignment: AlignmentType.JUSTIFIED,
    indent: { left: 4 * CM }, spacing: { line: L1, before: L15, after: L15 } }),
  caption: t => new Paragraph({ children: runs(t, { size: SZ_SMALL }), alignment: AlignmentType.LEFT,
    keepNext: true, spacing: { line: L1, before: L15, after: 60 } }),
  source: t => new Paragraph({ children: runs(t, { size: SZ_SMALL }), alignment: AlignmentType.LEFT,
    spacing: { line: L1, before: 60, after: L15 } }),
  ref: t => new Paragraph({ children: runs(t), alignment: AlignmentType.LEFT,
    spacing: { line: L1, before: 0, after: L1 } }),
};

let listInstance = 0;
function alineas(items) {
  listInstance++;
  return items.map((t, i) => {
    let txt = t;
    if (i === items.length - 1) txt = txt.replace(/;\s*$/, '.');   // última alínea termina em ponto
    return new Paragraph({ children: runs(txt), alignment: AlignmentType.JUSTIFIED,
      numbering: { reference: 'alinea', level: 0, instance: listInstance },
      spacing: { line: L15, before: 0, after: 0 } });
  });
}

const border = { style: BorderStyle.SINGLE, size: 4, color: '000000' };
const borders = { top: border, bottom: border, left: border, right: border };
function quadro(rows) {
  const n = rows[0].length;
  // larguras proporcionais ao conteúdo (com mínimo), somando a largura útil
  const wgt = Array.from({ length: n }, (_, c) => Math.max(8, Math.min(60, Math.max(...rows.map(r => (r[c] || '').length)))));
  const tot = wgt.reduce((a, b) => a + b, 0);
  const cols = wgt.map(w => Math.floor(TEXT_W * w / tot));
  cols[n - 1] += TEXT_W - cols.reduce((a, b) => a + b, 0);
  return new Table({
    width: { size: TEXT_W, type: WidthType.DXA }, columnWidths: cols,
    rows: rows.map((r, ri) => new TableRow({
      tableHeader: ri === 0, cantSplit: true,
      children: r.map((c, ci) => new TableCell({
        width: { size: cols[ci], type: WidthType.DXA }, borders, verticalAlign: VerticalAlign.CENTER,
        margins: { top: 50, bottom: 50, left: 90, right: 90 },
        shading: ri === 0 ? { type: ShadingType.CLEAR, color: 'auto', fill: 'D9D9D9' } : undefined,
        children: [new Paragraph({ children: runs(c, { size: SZ_SMALL, bold: ri === 0 }),
          alignment: ri === 0 ? AlignmentType.CENTER : AlignmentType.LEFT, spacing: { line: L1, before: 0, after: 0 } })],
      })),
    })),
  });
}

// ---------- conversão do corpo
const lines = body.split('\n');
const children = [];
let inRefs = false;
for (let i = 0; i < lines.length; i++) {
  const l = lines[i];
  if (!l.trim()) continue;
  if (l.startsWith('## ')) {
    const t = l.slice(3).trim();
    if (/^REFER[ÊE]NCIAS/i.test(t)) { inRefs = true; children.push(P.hRef(t)); }
    else children.push(P.h1(t));
    continue;
  }
  if (l.startsWith('### ')) { children.push(P.h2(l.slice(4).trim())); continue; }
  if (l.startsWith('|')) {
    const rows = [];
    while (i < lines.length && lines[i].startsWith('|')) {
      const cells = lines[i].trim().replace(/^\||\|$/g, '').split('|').map(c => c.trim());
      if (!cells.every(c => /^:?-+:?$/.test(c))) rows.push(cells);
      i++;
    }
    i--;
    children.push(quadro(rows));
    continue;
  }
  if (l.startsWith('- ')) {
    const items = [];
    while (i < lines.length && lines[i].startsWith('- ')) { items.push(lines[i].slice(2).trim()); i++; }
    i--;
    children.push(...alineas(items));
    continue;
  }
  if (l.startsWith('> ')) { children.push(P.quote(l.slice(2).trim())); continue; }
  if (/^(Quadro|Tabela|Figura) \d+/.test(l)) { children.push(P.caption(l.trim())); continue; }
  if (/^Fonte:/.test(l)) { children.push(P.source(l.trim())); continue; }
  children.push(inRefs ? P.ref(l.trim()) : P.body(l.trim()));
}

// ---------- capa / folha de rosto (sem número de página visível)
const C = (t, o = {}) => new Paragraph({ children: runs(t, { bold: o.bold, caps: o.caps }), alignment: AlignmentType.CENTER,
  spacing: { line: L15, before: o.before || 0, after: 0 } });
const capa = [
  C(fm.instituicao || '', { bold: true, caps: true }),
  C(fm.autor || '', { caps: true, before: 1800 }),
  C(`${fm.titulo || ''}:`, { bold: true, caps: true, before: 3000 }),
  C(fm.subtitulo || '', { bold: true }),
  new Paragraph({ children: runs(fm.natureza || ''), alignment: AlignmentType.JUSTIFIED,
    indent: { left: 8 * CM }, spacing: { line: L1, before: 1800, after: 0 } }),
  C(fm.local || '', { before: 3400 }),
  C(fm.ano || ''),
];

const header = new Header({ children: [new Paragraph({ alignment: AlignmentType.RIGHT,
  children: [new TextRun({ font: FONT, size: SZ_SMALL, children: [PageNumber.CURRENT] })] })] });

const pageProps = { page: { size: { width: PAGE.w, height: PAGE.h },
  margin: { ...MARGIN, header: 2 * CM, footer: CM } } };

const doc = new Document({
  creator: fm.autor || '', title: `${fm.titulo}: ${fm.subtitulo}`,
  styles: { default: { document: { run: { font: FONT, size: SZ } } } },
  numbering: { config: [{ reference: 'alinea', levels: [{ level: 0, format: LevelFormat.LOWER_LETTER, text: '%1)',
    alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: Math.round(1.25 * CM) + 397, hanging: 397 } } } }] }] },
  sections: [
    { properties: pageProps, children: capa },
    { properties: pageProps, headers: { default: header }, children },
  ],
});

Packer.toBuffer(doc).then(b => { fs.writeFileSync(OUT, b); console.log('Gerado:', OUT, b.length, 'bytes'); });
