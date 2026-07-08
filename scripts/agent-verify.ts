/**
 * Agent-verification runner — layers × routes. Method: docs/agent-verification.md.
 *
 * Usage:
 *   npm run agent-verify -- --provider=<id> [--layer=recon|dry-fire|real]
 *     [--route=http|cli|mcp] [--model=sonnet] [--max-turns=40] [--reps=1]
 *
 * Credentials & provisioning live OUTSIDE the repo in $AFS_CRED_DIR
 * (default ~/.afs/credentials) and are never committed:
 *   <id>.curlrc          http credential as a curl config file (used via -K);
 *                        also used by the runner's own verification step
 *   <id>.env             cli-route env vars, KEY=VALUE lines (e.g. GH_TOKEN=...)
 *   <id>.mcp.json        mcp-route config; the server key MUST equal <id>
 *   <id>.provision.yaml  task resources referenced as {{provision.*}}
 *                        (repo: ..., cli_bin: ..., channel: ...)
 *
 * Results go to data/experiments/results/<id>/ — gitignored until the
 * publication protocol (ToS review, dispute/rerun rules) is settled.
 */
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import * as yaml from 'js-yaml';
import { ROOT, loadProviders } from './lib.ts';

const args = Object.fromEntries(
  process.argv.slice(2).filter((a) => a.startsWith('--')).map((a) => {
    const [k, v] = a.replace(/^--/, '').split('=');
    return [k, v ?? 'true'];
  }),
);

const id = args.provider;
if (!id) throw new Error('Usage: npm run agent-verify -- --provider=<id> [--layer=recon|dry-fire|real] [--route=http|cli|mcp]');
const layer = (args.layer ?? 'recon') as 'recon' | 'dry-fire' | 'real';
const route = (args.route ?? 'http') as 'http' | 'cli' | 'mcp';
const model = args.model ?? 'sonnet';
const maxTurns = Number(args['max-turns'] ?? 40);
const reps = Number(args.reps ?? 1);
if (!['recon', 'dry-fire', 'real'].includes(layer)) throw new Error(`Unknown layer: ${layer}`);
if (!['http', 'cli', 'mcp'].includes(route)) throw new Error(`Unknown route: ${route}`);
if (layer !== 'real' && route !== 'http') throw new Error('Routes only apply to --layer=real');

const provider = loadProviders().map((p) => p.data).find((p) => p.id === id);
if (!provider) throw new Error(`Unknown provider id: ${id}`);

const CRED_DIR = process.env.AFS_CRED_DIR ?? path.join(os.homedir(), '.afs/credentials');
const cred = (ext: string) => path.join(CRED_DIR, `${id}.${ext}`);
function requireFile(p: string, why: string): string {
  if (!fs.existsSync(p)) throw new Error(`Missing ${p} — ${why}`);
  return p;
}

const entrypoints = Object.entries(provider.entrypoints)
  .map(([k, v]) => `- ${k}: ${Array.isArray(v) ? v.join(', ') : v}`)
  .join('\n');

const HARD_RULES = `HARD RULES:
- Do NOT create accounts, do NOT attempt signup, and do NOT try to get past any human-verification mechanism (CAPTCHA, phone, card, KYC).
- Use ONLY official sources for claims (the provider's own domains and repos).
- Never print any credential value in your output.
- No human is available; never ask questions. If information is missing, say "unknown" — never guess.`;

// ---------------- layer prompts ----------------

const RECON_TASK = `TASK (layer: recon — documentation reconnaissance, no credentials):
1. Starting from the docs entry point, determine the exact path a brand-new user must walk to reach their first successful authenticated API call.
2. List every step on that path that REQUIRES a human (CAPTCHA, email confirmation, phone verification, credit card, KYC, dashboard-only key creation, ...). Give the official evidence URL for each.
3. Write the exact curl command for the canonical first call — the simplest documented authenticated read (list models/resources or equivalent) — using $API_KEY as placeholder.

End your reply with exactly one fenced \`\`\`json block:
{"human_gates":[{"step":"...","evidence":"https://..."}],"first_call_command":"curl ...","confidence":"high|medium|low","notes":"..."}`;

const DRY_FIRE_TASK = `TASK (layer: dry-fire — no credentials available):
1. Using ONLY official documentation (start from the docs entry point), determine the canonical first API call for this provider: the simplest documented authenticated read (list models/resources/objects, or the documented auth/token endpoint if that must come first).
2. Construct the exact command and EXECUTE it with an obviously-fake credential (e.g. "sk-agent-pilot-dummy-key", or the provider's documented credential format with dummy values).
3. PASS means: the response is the provider's DOCUMENTED authentication-failure for an invalid credential (e.g. 401/403 with the documented JSON error shape) coming from the CORRECT endpoint — proving your endpoint, method, headers and request shape are right. A 404, an HTML error page, a routing error, or a connection failure is a FAIL.
4. If the endpoint cannot even be constructed without a per-account resource (a store domain, a cluster URL, a tenant id, ...), record that explicitly — result "blocked".
5. Also list every step a brand-new user must have a human perform to get a real working credential, each with an official evidence URL.

End your reply with exactly one fenced \`\`\`json block:
{"result":"pass|fail|blocked","http_status":401,"final_command":"curl ...","error_body_excerpt":"...","wrong_attempts":0,"friction_notes":["each dead end or ambiguity you hit, one line each"],"human_gates":[{"step":"...","evidence":"https://..."}],"confidence":"high|medium|low"}`;

const REAL_REPORT = `End your reply with exactly one fenced \`\`\`json block:
{"result":"pass|fail","resource_id":"id/number/url of what you created or produced","final_command":"the exact final command or tool call that completed the task (credentials redacted)","wrong_attempts":0,"friction_notes":["each dead end or ambiguity you hit, one line each"],"docs_pages_used":["https://..."],"confidence":"high|medium|low"}`;

// ---------------- assemble per layer/route ----------------

interface TaskDef {
  category: string; task: string; scenario: string;
  provisioning: { element: string; delivery: string }[];
  verification: { method: string; how: string };
  verify_commands?: Record<string, string>; cleanup: string;
  provider_overrides?: Record<string, string>;
}

function interpolate(tpl: string, vars: Record<string, string>): string {
  return tpl.replace(/\{\{([\w.]+)\}\}/g, (_, k) => {
    if (vars[k] == null) throw new Error(`No value for {{${k}}} — add "${k.replace('provision.', '')}" to ${cred('provision.yaml')}`);
    return vars[k];
  });
}

const date = new Date().toISOString().slice(0, 10);
let taskDef: TaskDef | null = null;
let provisionVars: Record<string, string> = {};
if (layer === 'real') {
  const taskFile = path.join(ROOT, `data/experiments/tasks/${provider.category}.yaml`);
  taskDef = yaml.load(fs.readFileSync(requireFile(taskFile, 'no task definition for this category yet'), 'utf8')) as TaskDef;
  if (fs.existsSync(cred('provision.yaml'))) {
    const prov = yaml.load(fs.readFileSync(cred('provision.yaml'), 'utf8')) as Record<string, unknown>;
    for (const [k, v] of Object.entries(prov)) provisionVars[`provision.${k}`] = String(v);
  }
}

function buildRun(rep: number) {
  const nonce = `afs-${id}-${route}-r${rep}-${Date.now().toString(36)}`;
  let taskBlock: string;
  let allowedTools = 'WebFetch WebSearch Bash(curl:*)';
  const extraArgs: string[] = [];
  const env: Record<string, string> = {};

  if (layer === 'recon') taskBlock = RECON_TASK;
  else if (layer === 'dry-fire') taskBlock = DRY_FIRE_TASK;
  else {
    const scenario = interpolate(taskDef!.scenario.trim(), { NONCE: nonce, ...provisionVars });
    const override = taskDef!.provider_overrides?.[id];
    let resources: string;
    if (route === 'http') {
      const curlrc = requireFile(cred('curlrc'), 'http route needs the credential as a curl config file');
      resources = `RESOURCES PROVIDED (provisioning manifest):
- A curl config file containing valid auth headers for this provider is at:
  ${curlrc}
  Use it by passing \`-K ${curlrc}\` to curl — auth is applied automatically.
- Never read, print, or copy that file's contents; only reference it via -K.

METHOD: discover how from the provider's OFFICIAL documentation; execute with curl (always with -K). No SDKs, no CLIs.`;
    } else if (route === 'cli') {
      const envFile = requireFile(cred('env'), 'cli route needs KEY=VALUE env lines for the CLI');
      for (const line of fs.readFileSync(envFile, 'utf8').split('\n')) {
        const m = line.match(/^([A-Z0-9_]+)=(.*)$/);
        if (m) env[m[1]] = m[2];
      }
      const cliBin = provisionVars['provision.cli_bin'];
      if (!cliBin) throw new Error(`cli route needs "cli_bin" in ${cred('provision.yaml')}`);
      allowedTools = `WebFetch WebSearch Bash(${cliBin}:*)`;
      resources = `RESOURCES PROVIDED (provisioning manifest):
- The provider's OFFICIAL CLI ("${cliBin}") is installed and on PATH.
- A valid credential is provisioned in the environment; the CLI picks it up automatically — you do NOT need to run any auth/login command or reference any variable yourself.

METHOD: use ONLY the official CLI ("${cliBin}" commands). No curl, no raw REST calls. Discover usage from the CLI's own help output and the provider's official CLI documentation.`;
    } else {
      const mcpConf = requireFile(cred('mcp.json'), `mcp route needs an MCP config whose server key is "${id}"`);
      extraArgs.push('--mcp-config', mcpConf, '--strict-mcp-config');
      allowedTools = `WebFetch WebSearch mcp__${id}`;
      resources = `RESOURCES PROVIDED (provisioning manifest):
- The provider's OFFICIAL MCP server ("${id}") is already connected and authenticated; its tools are available to you directly.

METHOD: use ONLY the ${id} MCP server's tools. No shell, no curl, no CLI. If the MCP tools are insufficient for any part of the task, report that honestly as the failure reason — do not work around it by other means.`;
    }
    taskBlock = `USER TASK (real scenario, category: ${provider.category}):
${scenario}
${override ? `\nPROVIDER-SPECIFIC PINNED TARGET: ${override}\n` : ''}
${resources}

Additional hard rule: only mutate the resources designated above; create AT MOST one ${taskDef!.task.split('-')[1] ?? 'resource'}; no other writes anywhere.

${REAL_REPORT}`;
  }

  const prompt = `You are running a standardized, unattended verification task for the Agent-Friendly Services Index (github.com/Olorinm/agent-friendly-services). You are an autonomous agent; no human is available. Your transcript becomes evidence — be precise and cite URLs.

Provider: ${provider.name} (${id})
Known official entry points:
${entrypoints}

${taskBlock}

${HARD_RULES}`;

  return { nonce, prompt, allowedTools, extraArgs, env };
}

// ---------------- execute ----------------

const outDir = path.join(ROOT, 'data/experiments/results', id);
fs.mkdirSync(outDir, { recursive: true });
const slug = layer === 'real' ? `${layer}-${route}` : layer;

for (let rep = 1; rep <= reps; rep++) {
  const base = path.join(outDir, `${date}-${slug}-rep${rep}`);
  if (fs.existsSync(`${base}.yaml`)) { console.log(`skip rep${rep} (exists: ${base}.yaml)`); continue; }
  const run = buildRun(rep);
  console.log(`[${id}] ${slug} rep ${rep}/${reps} (model: ${model}, max ${maxTurns} turns)...`);

  // Provider-side cleanliness assertion: if artifacts from earlier runs are
  // still visible through the verification API, later reps can imitate them
  // instead of working from docs — record the contamination loudly.
  const verifyCmdPre = taskDef?.verify_commands?.[id];
  let residue = false;
  if (layer === 'real' && verifyCmdPre) {
    try {
      const pre = execFileSync('bash', ['-c', interpolate(verifyCmdPre, { NONCE: run.nonce, CURLRC: requireFile(cred('curlrc'), 'verification runs over http'), ...provisionVars })], { encoding: 'utf8', timeout: 5 * 60_000 });
      residue = pre.includes(`afs-${id}-`);
      if (residue) console.warn(`  WARNING: artifacts from earlier runs are visible to the agent — clean the test resource for uncontaminated reps`);
    } catch { /* pre-check is best-effort */ }
  }

  // Machine-side cleanliness: each rep gets a fresh empty working directory,
  // so no CLAUDE.md, project memory, or files written by earlier reps leak in.
  // (Full isolation — no cached logins/config anywhere — is the fresh-machine
  // requirement in docs/agent-verification.md; this is the in-repo minimum.)
  const workDir = fs.mkdtempSync(path.join(os.tmpdir(), `afs-run-${id}-`));

  let meta: { result?: string; num_turns?: number; duration_ms?: number; total_cost_usd?: number };
  try {
    meta = JSON.parse(execFileSync(
      'claude',
      ['-p', run.prompt, '--model', model, '--max-turns', String(maxTurns), '--output-format', 'json', '--allowedTools', run.allowedTools, ...run.extraArgs],
      { encoding: 'utf8', timeout: 20 * 60_000, maxBuffer: 32 * 1024 * 1024, cwd: workDir, env: { ...process.env, ...run.env } },
    ));
  } catch (e) {
    fs.writeFileSync(`${base}.yaml`, yaml.dump({ provider: id, layer, route, rep, date, run_error: String(e).slice(0, 500) }));
    console.log(`  rep ${rep} RUN ERROR (recorded)`);
    continue;
  }

  const blocks = [...(meta.result ?? '').matchAll(/```json\s*([\s\S]*?)```/g)];
  let claims: Record<string, unknown> | null = null;
  for (const b of blocks.reverse()) {
    try { claims = JSON.parse(b[1]); break; } catch { /* try earlier block */ }
  }

  // Independent verification — the runner never trusts the agent's self-report.
  let verified: boolean | 'n/a' = 'n/a';
  const verifyCmd = taskDef?.verify_commands?.[id];
  if (layer === 'real' && verifyCmd) {
    verified = false;
    try {
      const cmd = interpolate(verifyCmd, { NONCE: run.nonce, CURLRC: requireFile(cred('curlrc'), 'verification runs over http'), ...provisionVars });
      verified = execFileSync('bash', ['-c', cmd], { encoding: 'utf8', timeout: 5 * 60_000 }).includes(run.nonce);
    } catch { /* verified stays false */ }
  }

  fs.writeFileSync(`${base}.md`, `# ${provider.name} — ${slug} rep ${rep} (${date})\n\nModel: ${model} · max turns: ${maxTurns} · runner: scripts/agent-verify.ts\n\n---\n\n${meta.result ?? ''}\n`);
  fs.writeFileSync(`${base}.yaml`, yaml.dump({
    provider: id, category: provider.category, layer, ...(layer === 'real' ? { route, task: taskDef!.task, nonce: run.nonce } : {}),
    rep, model, date,
    ...(residue ? { contaminated: 'artifacts from earlier runs were visible to the agent' } : {}),
    agent_claims: claims,
    verified_independently: verified,
    num_turns: meta.num_turns, duration_ms: meta.duration_ms, total_cost_usd: meta.total_cost_usd,
    transcript: path.basename(`${base}.md`),
  }, { lineWidth: 120 }));
  console.log(`  rep ${rep}: agent says ${String((claims as { result?: string } | null)?.result ?? claims?.confidence ?? 'UNPARSED')} | verified: ${verified} | ${meta.num_turns} turns, $${meta.total_cost_usd?.toFixed(2)}`);
}

if (layer === 'real' && taskDef) console.log(`Cleanup (manual until automated): ${taskDef.cleanup}`);
console.log(`Results → ${path.relative(ROOT, outDir)}/ (gitignored until the publication protocol is settled)`);
