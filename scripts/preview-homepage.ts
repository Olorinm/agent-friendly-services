/** Local review of the generated Markdown itself, with no separate data/layout implementation. */
import fs from 'node:fs';
import path from 'node:path';
import { ROOT } from './lib.ts';
const out = path.join(ROOT, 'data/experiments/results/homepage-layout-preview');
fs.mkdirSync(out, { recursive: true });
const pages = new Map([
  ['README.zh-CN.md', 'index.html'], ['README.md', 'index.en.html'],
  ['generated/services.md', 'services.html'], ['generated/tasks.en.md', 'tasks.html'],
  ['generated/evaluations.md', 'evaluations.html'],
]);
const escape = (s: string) => s.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;');
const inline = (s: string) => s.replace(/`([^`]+)`/g, (_, text) => `<code>${escape(text)}</code>`)
  .replace(/\[([^\]]+)\]\(([^\s]+)\)/g, '<a href="$2">$1</a>')
  .replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
// Only the Markdown constructs emitted by this repository are needed here.
function render(source: string) {
  return source.split('\n\n').map(block => {
    if (/^\|/.test(block)) {
      const rows = block.split('\n').map(line => line.replace(/^\|\s*|\s*\|$/g, '').split(/(?<!\\)\|/));
      const row = (cells: string[], tag: string) => `<tr>${cells.map(c => `<${tag}>${inline(c.trim().replaceAll('\\|', '|'))}</${tag}>`).join('')}</tr>`;
      return `<table><thead>${row(rows[0], 'th')}</thead><tbody>${rows.slice(2).map(r => row(r, 'td')).join('')}</tbody></table>`;
    }
    if (/^</.test(block)) return block;
    if (/^#{1,6} /.test(block)) return block.replace(/^(#{1,6}) (.*)$/gm, (_, h, text) => `<h${h.length}>${inline(text)}</h${h.length}>`);
    if (/^- /.test(block)) return `<ul>${block.split('\n').map(s => `<li>${inline(s.replace(/^- /, ''))}</li>`).join('')}</ul>`;
    return `<p>${inline(block)}</p>`;
  }).join('\n');
}
const css = `*{box-sizing:border-box}body{color:#1f2328;background:white;font:16px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;margin:0}main{max-width:1280px;margin:36px auto;padding:0 28px 60px}h1{font-size:32px}h2{border-bottom:1px solid #d1d9e0;padding-bottom:8px}h3{margin-top:28px}p{margin:14px 0}a{color:#0969da;text-decoration:none}a:hover{text-decoration:underline}table{width:100%;border-collapse:collapse;margin:16px 0;font-size:14px}th,td{border:1px solid #d1d9e0;padding:10px 12px;vertical-align:top;text-align:left}th[align=right],td[align=right]{text-align:right}td[align=right]{white-space:nowrap}tbody tr:nth-child(even){background:#f6f8fa}details{margin:16px 0 24px}summary{cursor:pointer}h4{font-size:16px}code{background:#f6f8fa} @media(max-width:700px){main{padding:0 12px}table{display:block;overflow:auto}th,td{min-width:80px}}`;
for (const [source, filename] of pages) {
  const body = render(fs.readFileSync(path.join(ROOT, source), 'utf8')).replace(/href="([^"]+)"/g, (whole, href) => {
    if (/^(https?:|#)/.test(href)) return whole;
    const [relative, anchor] = href.split('#');
    const resolved = path.posix.normalize(path.posix.join(path.posix.dirname(source), relative));
    const target = pages.get(resolved) ?? `https://github.com/Olorinm/agent-friendly-services/blob/main/${resolved}`;
    return `href="${target}${anchor ? '#' + anchor : ''}"`;
  });
  fs.writeFileSync(path.join(out, filename), `<!doctype html><html lang="${source.includes('zh-CN') ? 'zh-CN' : 'en'}"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Agent-Friendly Services — local review</title><style>${css}</style><main>${body}</main></html>`);
}
console.log(path.join(out, 'index.html'));
