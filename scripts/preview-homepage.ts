/** Local layout review only; does not modify README, source data or published artifacts. */
import fs from 'node:fs';
import path from 'node:path';
import {ROOT,loadProviders,loadCandidates,loadCategories} from './lib.ts';
import {buildBoards,renderBoardDetails,tokenLabel,moneyLabel} from './leaderboard.ts';
import {loadEvaluations} from './evaluations.ts';
import { serviceAccess } from './service-access.ts';
import {loadPrices,estimateModelCost} from './model-costs.ts';
const out=path.join(ROOT,'data/experiments/results/homepage-layout-preview');
fs.mkdirSync(path.join(out,'services'),{recursive:true});
const services=[...loadProviders(),...loadCandidates()].map(p=>p.data).sort((a,b)=>a.name.localeCompare(b.name));
const prices=loadPrices();
const runs=loadEvaluations().map(r=>({...r,model_cost:estimateModelCost(r,prices)}));
const boards=buildBoards(runs);
const names=new Map(services.map(p=>[p.id,p.name]));
const interfaces=new Map(services.flatMap(p=>(p.catalog?.routes??[]).map(r=>[`${p.id}/${r.id}`,r.interface] as [string,string])));
const repo='https://github.com/Olorinm/agent-friendly-services/blob/main/';
const esc=(v:unknown)=>String(v??'').replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
const link=(label:string,url:string)=>`<a href="${esc(url)}">${esc(label)}</a>`;
const css=`*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:24px}body{margin:0;color:#1f2328;background:#fff;font:16px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans SC",sans-serif}main{max-width:1120px;margin:48px auto;padding:0 36px 60px}h1{font-size:32px;line-height:1.25;margin:0 0 18px;letter-spacing:-.6px}h2{font-size:24px;margin:40px 0 18px;padding-bottom:8px;border-bottom:1px solid #d1d9e0}h3{font-size:19px;margin:24px 0 12px}p{margin:12px 0}a{color:#0969da;text-decoration:none}a:hover{text-decoration:underline}a:focus-visible,summary:focus-visible{outline:2px solid #0969da;outline-offset:4px}.muted,small{color:#59636e;font-size:14px}nav{display:flex;flex-wrap:wrap;gap:6px 22px;margin:20px 0 24px}.entry{display:flex;flex-wrap:wrap;gap:4px 8px;font-size:14px;min-width:100px}.table-wrap{overflow-x:auto}table{table-layout:fixed;border-collapse:collapse;width:100%;margin:12px 0 16px}th,td{padding:10px 14px;border:1px solid #d1d9e0;text-align:left;vertical-align:top;overflow-wrap:anywhere}th{background:#f6f8fa;font-weight:600;font-size:14px}td.num,th.num{text-align:right;white-space:nowrap;font-variant-numeric:tabular-nums}.name{font-weight:600}details{border:1px solid #d1d9e0;border-radius:6px;margin:18px 0 26px;padding:12px 16px}summary{cursor:pointer;font-weight:600}details[open] summary{margin-bottom:16px}details table{width:100%;table-layout:auto}details p{font-size:15px}.tag{font-weight:400;color:#59636e;font-size:14px;margin-left:12px}.lead{max-width:850px;font-size:17px}footer{border-top:1px solid #d1d9e0;margin-top:42px;padding-top:20px}.back{display:inline-block;margin-bottom:20px}.source-list{line-height:2}@media(max-width:650px){main{padding:0 18px;margin-top:24px}h1{font-size:27px}.entry{margin-left:0;display:flex}th,td{padding:8px 10px}.table-wrap{margin-right:-8px}table{min-width:580px}details{padding:12px}details table{min-width:480px}}`;
const shell=(title:string,body:string)=>`<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${esc(title)} · Agent-Friendly Services</title><style>${css}</style><main>${body}</main></html>`;
const table=(headers:string[],rows:string[][],numeric=false)=>`<div class="table-wrap"><table><thead><tr>${headers.map((h,i)=>`<th${numeric&&i>0&&i<5?' class="num"':''}${headers.length===(numeric?6:3)?` style="width:${(numeric?[26,12,12,12,12,26]:[26,48,26])[i]}%"`:''}>${esc(h)}</th>`).join('')}</tr></thead><tbody>${rows.map(row=>`<tr>${row.map((c,i)=>`<td${numeric&&i>0&&i<5?' class="num"':''}>${c}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`;
const entries=(p:any)=>serviceAccess(p, true).map(([n,u])=>link(n,u)).join(' · ');
const profile=(p:any)=>`<a class="name" href="services/${esc(p.id)}.html">${esc(p.name)}</a>`;
function inline(s:string){return esc(s).replace(/\[([^\]]+)\]\(([^)]+)\)/g,(_,n,u)=>`<a href="${u.startsWith('./')?repo+u.slice(2):u}">${n}</a>`).replace(/\*\*([^*]+)\*\*/g,'<strong>$1</strong>').replaceAll('&lt;br&gt;','<br>');}
function markdown(s:string){
 const blocks=s.split('\n\n');
 return blocks.map(b=>{
  if(b.startsWith('|')){const rows=b.split('\n').map(l=>l.replace(/^\||\|$/g,'').split(/(?<!\\)\|/).map(x=>x.trim()));return table(rows[0],rows.slice(2).map(r=>r.map(inline)));}
  return '<p>'+inline(b).replaceAll('\n','<br>')+'</p>';
 }).join('\n');
}
const availability:Record<string,string>={self_serve:'可自助接入',invite_only:'仅限邀请',application_required:'需提交申请',contact_sales:'需联系销售',unknown:'尚未核实',unavailable:'暂不可用'};
for(const p of services){
 const recorded=runs.filter(r=>r.service_id===p.id);
 const routes=p.catalog?.routes??[];
 const source=p.catalog?.sources??{};
 const publicSource=repo+(loadProviders().some(x=>x.data.id===p.id)?`generated/providers.md#${p.id}`:`data/candidates/${p.id}.yaml`);
 const routeRows=routes.map(r=>[link(r.interface==='web'?'网页':r.interface.toUpperCase(),r.entry_url),esc(r.id),esc(availability[r.availability?.value??'unknown']??r.availability?.value??'尚未核实'),r.docs?link('文档',r.docs):'—']);
 const signup=p.checks?.self_serve_signup;
 const admission=routeRows.length?table(['入口','路径','接入条件','文档'],routeRows):`<p>${signup?.status==='supported'?'资料记录支持自助注册。':'个人接入条件尚未完整核实。'} ${p.entrypoints.signup?link('注册入口',p.entrypoints.signup):''}</p>`;
 const profileRuns=recorded.length?table(['任务','实测入口','结果','日期'],recorded.map(r=>[esc(r.task.description),esc(r.route_id),link(r.status==='completed'?'完成':r.status==='invalid_run'?'环境无效':'未完成',repo+`data/experiments/evaluations/${r.run_id}.json`),esc(r.started_at.slice(0,10))])):'<p>尚未进行任务实测。</p>';
 const sources=Object.values(source).map((x:any)=>`<li>${link(x.kind??'来源',x.url)} <span class="muted">核对日期：${esc(x.checked_on??'未记录')}</span></li>`).join('');
 const body=`${link('← 返回服务目录','../index.html')}<h1 style="margin-top:22px">${esc(p.name)}</h1><p>${esc(p.summary)}</p><p>${link('官方网站',p.homepage)} · ${link('完整收录资料',publicSource)}</p><h2>文档与接入</h2><p class="source-list">${entries(p)||'尚未找到可确认的接入文档。'}</p><h2>个人接入条件</h2>${admission}<h2>服务价格</h2><p>${p.entrypoints.pricing?link('查看官方价格与免费额度',p.entrypoints.pricing):'完整价格和免费额度尚未核实，不能根据一次试跑的费用推断长期价格。'}</p><h2>实测记录</h2>${profileRuns}${sources?`<h2>资料来源</h2><ul>${sources}</ul>`:''}`;
 fs.writeFileSync(path.join(out,'services',p.id+'.html'),shell(p.name,body));
}
const labels:Record<string,string>={'travel':'旅行','databases':'数据库','web-search-data':'网页搜索与数据','productivity-storage':'协作办公与存储','ai-models':'AI 模型','agent-tooling':'Agent 工具','code-execution':'代码执行','developer-tools':'开发工具','cloud-hosting':'云服务与部署','payments-billing':'支付与账单','communication':'通信','observability-security':'监控与安全','commerce-marketing':'电商与营销'};
const priority=['travel','databases','web-search-data','productivity-storage'];
const categories=loadCategories().sort((a,b)=>(priority.indexOf(a.id)<0?99:priority.indexOf(a.id))-(priority.indexOf(b.id)<0?99:priority.indexOf(b.id)));
const taskClass=new Map<string,string>();const classNames=new Map<string,string>();
for(const b of boards){const s=fs.readFileSync(path.join(ROOT,b.task_file),'utf8');const label=s.match(/^分类：(.+)$/m)?.[1]??'';const id=label.match(/（([^）]+)）/)?.[1];if(id){taskClass.set(b.task_file,id);classNames.set(id,label.split('（')[0].split(' / ').at(-1)!.trim());}}
const sections:string[]=[];const navigation:string[]=[];
for(const c of categories){
 const members=services.filter(p=>p.category===c.id||p.catalog?.classifications.some(x=>x.startsWith(c.id+'/')));
 if(!members.length)continue;
 const title=labels[c.id]??c.name;navigation.push(link(`${title} ${members.length}`,'#'+c.id));
 const groupIds=[...new Set(members.flatMap(p=>(p.catalog?.classifications??[]).filter(x=>x.startsWith(c.id+'/'))))];
 const assigned=new Set(groupIds.flatMap(id=>members.filter(p=>p.catalog?.classifications.includes(id)).map(p=>p.id)));
 const groups=groupIds.map(id=>({id,name:classNames.get(id)??id.split('/')[1],members:members.filter(p=>p.catalog?.classifications.includes(id))}));
 if(assigned.size<members.length)groups.push({id:c.id,name:groupIds.length?'其他服务':'',members:members.filter(p=>!assigned.has(p.id))});
 const content=groups.map(g=>{
  const measuredBoards=boards.filter(b=>taskClass.get(b.task_file)===g.id);
  let main='';
  if(measuredBoards.length){
   const rows:string[][]=[];const measured=new Set<string>();
   for(const b of measuredBoards)for(const r of b.rows){const p=services.find(p=>p.id===r.service_id)!;measured.add(p.id);const count=measuredBoards.flatMap(b=>b.rows).filter(x=>x.service_id===p.id).length;rows.push([profile(p)+(count>1?' <small>'+esc(r.route_id)+'</small>':''),link(r.metrics.resolution_rate===null?'—':`${Math.round(r.metrics.resolution_rate*100)}%`,repo+`generated/evaluations.md#${b.id}`),tokenLabel(r.metrics.tokens),moneyLabel(r.metrics.model_cost_usd),moneyLabel(r.metrics.service_cost_usd),`<span class="entry">${entries(p)||'尚未确认'}</span>`]);}
   for(const p of g.members.filter(p=>!measured.has(p.id)))rows.push([profile(p),'<span class="muted">待实测</span>','—','—','—',`<span class="entry">${entries(p)||'尚未确认'}</span>`]);
   main=table(['服务','完成率','Token 用量','模型费用','服务费用','接入方式'],rows,true)+`<p class="muted">Token 用量与费用为每次有效试跑的均值，包含成功与失败；模型费用为估算，— 表示未知。${measuredBoards.length>1?'现有记录条件未统一，暂不排名。':''}</p><details><summary>测了什么，怎么测的</summary>${markdown(renderBoardDetails(measuredBoards,names,true,'./',interfaces))}</details>`;
  }else main=table(['服务','用途','接入方式'],g.members.map(p=>[profile(p),esc(p.summary),entries(p)||'尚未确认']));
  return `${g.name?`<h3>${esc(g.name)}${!measuredBoards.length?'<span class="tag">尚未实测</span>':''}</h3>`:(!measuredBoards.length?'<p class="muted">尚未实测</p>':'')}${main}`;
 }).join('');
 sections.push(`<section id="${esc(c.id)}"><h2>${esc(title)}<span class="tag">${members.length} 个服务</span></h2>${content}</section>`);
}
const body=`<h1>Agent-Friendly Services</h1><p class="lead">帮你找到能让 Agent 完成任务的服务，并用实测比较可靠性、接入成本和开销。</p><p class="muted">已收录 ${services.length} 个服务。点击服务名查看资料，文档、API、CLI、MCP 链接可直接使用。</p><nav aria-label="服务分类">${navigation.join('')}</nav>${sections.join('')}<footer><h3>给 Agent 的入口</h3><p>${link('查询指引',repo+'llms.txt')} · ${link('服务 JSON','https://raw.githubusercontent.com/Olorinm/agent-friendly-services/main/generated/catalog.json')} · ${link('实测 JSON','https://raw.githubusercontent.com/Olorinm/agent-friendly-services/main/generated/evaluations.json')} · ${link('MCP 使用方法',repo+'mcp/README.md')}</p><h3>方法与贡献</h3><p>${link('核心原则',repo+'AGENTS.md')} · ${link('任务设计',repo+'data/experiments/tasks/AGENTS.md')} · ${link('执行与验收',repo+'data/experiments/AGENTS.md')} · ${link('提交补充或纠错','https://github.com/Olorinm/agent-friendly-services/issues')}</p></footer>`;
fs.writeFileSync(path.join(out,'index.html'),shell('服务目录',body));
console.log(`Local HTML preview: ${out}/index.html (${services.length} service pages)`);
