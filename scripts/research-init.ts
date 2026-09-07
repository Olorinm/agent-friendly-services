import { initializeResearch } from './research.ts';

const args = process.argv.slice(2);
if (args.length !== 1 || args[0] === '--help') {
  console.log('Usage: npm run research:init -- <category/subcategory>\nCreates a blank research brief; never overwrites existing research.');
  process.exit(args[0] === '--help' ? 0 : 1);
}
try {
  const file = initializeResearch(args[0]);
  console.log(`Created ${file}\nNext: see docs/contributing.md#research-user-needs and update this source record. This brief contains no research evidence yet.`);
} catch (error) {
  console.error(String(error));
  process.exitCode = 1;
}
