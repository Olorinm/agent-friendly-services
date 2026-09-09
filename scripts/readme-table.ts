const escape = (value: string) => value.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;');
const inline = (value: string) => escape(value.replaceAll('\\|', '|'))
  .replace(/\[([^\]]+)\]\(([^\s]+)\)/g, '<a href="$2">$1</a>');

/** GitHub-compatible HTML width hints; use the same name/access widths in both table types. */
export function readmeTable(markdown: string, measured: boolean): string {
  const rows = markdown.trim().split('\n').map(line => line.replace(/^\|\s*|\s*\|$/g, '').split(/(?<!\\)\|/).map(cell => cell.trim()));
  const widths = measured ? [26, 12, 11, 11, 11, 9, 20] : [26, 54, 20];
  const render = (row: string[], header: boolean) => '<tr>' + row.map((cell, i) => {
    const tag = header ? 'th' : 'td';
    return `<${tag}${header ? ` width="${widths[i]}%"` : ''} align="${measured && i > 0 && i < 5 ? 'right' : 'left'}">${inline(cell)}</${tag}>`;
  }).join('') + '</tr>';
  return `<table width="100%">\n<thead>${render(rows[0], true)}</thead>\n<tbody>\n${rows.slice(2).map(row => render(row, false)).join('\n')}\n</tbody>\n</table>`;
}
