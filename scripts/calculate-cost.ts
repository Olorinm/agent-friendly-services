/** Local JSON interface to the same cost function used by generated pages. */
import fs from 'node:fs';
import { estimateModelCost } from './model-costs.ts';
const [runFile, priceFile] = process.argv.slice(2);
if (!runFile || !priceFile) throw new Error('Usage: calculate-cost.ts run.json pricing.json');
const run = JSON.parse(fs.readFileSync(runFile, 'utf8'));
const prices = JSON.parse(fs.readFileSync(priceFile, 'utf8'));
console.log(JSON.stringify(estimateModelCost({ ...run, pricing_snapshot: prices }, null)));
