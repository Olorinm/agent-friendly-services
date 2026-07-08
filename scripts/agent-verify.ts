/**
 * Runs the standardized agent-verification task against one provider.
 * See docs/agent-verification.md. Usage:
 *   npm run agent-verify -- --provider=<id> [--tier=t0|t1] [--model=sonnet] [--max-turns=25]
 * T1 expects the API key in AFS_KEY_<ID> (id uppercased, dashes → underscores).
 */
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { ROOT, loadProviders } from './lib.ts';

const args = Object.fromEntries(
  process.argv.slice(2).filter((a) => a.startsWith('--')).map((a) => {
    const [k, v] = a.replace(/^--/, '').split('=');
    return [k, v ?? 'true'];
  }),
);

const id = args.provider;
if (!id) throw new Error('Usage: npm run agent-verify -- --provider=<id> [--tier=t0|t1]');
const tier = (args.tier ?? 't0') as 't0' | 't1';
const model = args.model ?? 'sonnet';
const maxTurns = Number(args['max-turns'] ?? 25);

const provider = loadProviders().map((p) => p.data).find((p) => p.id === id);
if (!provider) throw new Error(`Unknown provider id: ${id}`);

const envKeyName = `AFS_KEY_${id.toUpperCase().replace(/-/g, '_')}`;
if (tier === 't1' && !process.env[envKeyName]) throw new Error(`T1 needs an API key in ${envKeyName}`);

const entrypoints = Object.entries(provider.entrypoints)
  .map(([k, v]) => `- ${k}: ${Array.isArray(v) ? v.join(', ') : v}`)
  .join('\n');

const HARD_RULES = `HARD RULES:
- Do NOT create accounts, do NOT attempt signup, and do NOT try to get past any human-verification mechanism (CAPTCHA, phone, card, KYC).
- Use ONLY official sources for claims (the provider's own domains and repos).
- No human is available; never ask questions. If information is missing, say "unknown" — never guess.`;

const T0_TASK = `TASK (tier T0 — documentation reconnaissance, no credentials):
1. Starting from the docs entry point, determine the exact path a brand-new user must walk to reach their first successful authenticated API call.
2. List every step on that path that REQUIRES a human (CAPTCHA, email confirmation, phone verification, credit card, KYC, dashboard-only key creation, ...). Give the official evidence URL for each.
3. Write the exact curl command for the canonical first call — the simplest documented authenticated read (list models/resources or equivalent) — using $API_KEY as placeholder.

End your reply with exactly one fenced \`\`\`json block:
{"tier":"t0","human_gates":[{"step":"...","evidence":"https://..."}],"first_call_command":"curl ...","confidence":"high|medium|low","notes":"..."}`;

const T1_TASK = `TASK (tier T1 — live verification):
A valid API key is in the environment variable ${envKeyName}.
1. Using ONLY official documentation (start from the docs entry point), make the canonical first call: the simplest documented authenticated read (list models/resources or equivalent). Run it with Bash/curl.
2. You pass only when you receive a documented 2xx response. Show the final command (redact the key) and the HTTP status.
3. If you cannot get a 2xx, record exactly where the documentation failed you.

End your reply with exactly one fenced \`\`\`json block:
{"tier":"t1","result":"pass|fail","http_status":200,"final_command":"curl ... (key redacted)","steps_taken":3,"failure_point":null,"notes":"..."}`;

const prompt = `You are running a standardized, unattended verification task for the Agent-Friendly Services Index (github.com/Olorinm/agent-friendly-services). Your transcript becomes public evidence — be precise and cite URLs.

Provider: ${provider.name} (${id})
Known official entry points:
${entrypoints}

${tier === 't0' ? T0_TASK : T1_TASK}

${HARD_RULES}`;

console.log(`Running ${tier.toUpperCase()} for ${id} (model: ${model}, max ${maxTurns} turns)...`);
const out = execFileSync(
  'claude',
  ['-p', prompt, '--model', model, '--max-turns', String(maxTurns), '--allowedTools', 'WebFetch WebSearch Bash(curl:*)'],
  { encoding: 'utf8', timeout: 15 * 60_000, maxBuffer: 16 * 1024 * 1024, env: process.env },
);

const jsonMatch = out.match(/```json\s*([\s\S]*?)```/);
if (!jsonMatch) {
  console.error(out);
  throw new Error('Agent did not end with the required ```json block — transcript above.');
}
const result = JSON.parse(jsonMatch[1]);

const date = new Date().toISOString().slice(0, 10);
const dir = path.join(ROOT, 'data/experiments/first-call');
fs.mkdirSync(path.join(dir, 'transcripts'), { recursive: true });

const transcriptRel = `transcripts/${id}-${date}.md`;
fs.writeFileSync(path.join(dir, transcriptRel), `# ${provider.name} — agent verification (${tier.toUpperCase()}, ${date})\n\nModel: ${model} · max turns: ${maxTurns} · runner: scripts/agent-verify.ts\n\n---\n\n${out}\n`);

// Latest result per provider; JSON is valid YAML, so keep it simple and parse-safe.
const record = {
  provider: id,
  task: 'first_call',
  tier,
  ...(tier === 't1' ? { result: result.result, http_status: result.http_status } : {}),
  model,
  date,
  transcript: transcriptRel,
  summary: result,
};
fs.writeFileSync(path.join(dir, `${id}.yaml`), JSON.stringify(record, null, 2) + '\n');

console.log(`✓ ${id}: ${tier === 't1' ? result.result : `${result.human_gates?.length ?? '?'} human gates found`}`);
console.log(`  result → data/experiments/first-call/${id}.yaml`);
console.log(`  transcript → data/experiments/first-call/${transcriptRel}`);
