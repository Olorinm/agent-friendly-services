<!-- GENERATED — edit scripts/generate.ts; run npm run generate. -->

# Agent-Friendly Services

English | [简体中文](./README.zh-CN.md)

**Find services that let your Agent complete tasks, and use real tests to compare reliability, setup effort and cost.**

Finding a service is only the start. Before your Agent can use it, you may need to read the docs, create an account and work out whether the available API actually does what you need. We collect the options and test them on real tasks, so you and your Agent have less of that work to repeat. We focus on what an ordinary personal user can access, including the hurdles along the way.

## Browse the services

Pick a category below to see its candidates, the tasks we designed and the results we recorded.

| Category / subcategory | Candidates | Task definitions | Recorded runs | Services with runs |
| --- | ---: | --- | ---: | --- |
| Databases / Hosted Relational Databases | [6](./generated/catalog.md#databases-hosted-relational) | [Tasks](./data/experiments/tasks/databases.md) | [2](./generated/evaluations.md#databases-hosted-relational) | Neon, Turso |
| Productivity / Storage / Collaborative Tables | [8](./generated/catalog.md#productivity-storage-collaborative-tables) | [Tasks](./data/experiments/tasks/collaborative-tables.md) | [4](./generated/evaluations.md#productivity-storage-collaborative-tables) | Grist, Notion |
| Travel / Flights | [26](./generated/catalog.md#travel-flights) | [Tasks](./data/experiments/tasks/travel-flights.md) | [4](./generated/evaluations.md#travel-flights) | Ignav Flights, Kiwi.com |
| Web Search / Data / Web Search | [6](./generated/catalog.md#web-search-data-web-search) | [Tasks](./data/experiments/tasks/web-search.md) | [3](./generated/evaluations.md#web-search-data-web-search) | Exa, Firecrawl |

[All candidates and access routes](./generated/catalog.md) · [All task results and evidence](./generated/evaluations.md) · [Legacy provider index (76)](./generated/providers.md)

Open a result to see what the Agent accomplished, what it needed, and the tokens, time and service charges involved. Each run includes its task, model, date and supporting evidence so you can judge how closely it matches your situation.

This is a growing collection. Untested services and access restrictions stay visible, and run counts include earlier task versions and unsuccessful attempts. A successful run is useful evidence; it takes more comparable runs to recommend a service with confidence.

## Let your Agent use the directory

You can give your Agent the query guide below and ask it to find options for your task, check the access requirements and explain its choice using the available evidence.

[Query guide](./llms.txt) · [Catalog JSON](./generated/catalog.json) · [Results JSON](./generated/evaluations.json) · [MCP setup](./mcp/README.md)

Use `search_services` to filter by category/subcategory and access route, then `get_service` to inspect eligibility, costs and task evidence. Without MCP:

```sh
curl -s https://raw.githubusercontent.com/Olorinm/agent-friendly-services/main/generated/catalog.json
```

## Help us fill the gaps

Know a service we missed, have a task you would like tested, or found something that has changed? Issues and PRs are welcome. A useful lead or a correction is a contribution too.

[Principles](./AGENTS.md) · [Inclusion standards](./docs/catalog-standard.zh-CN.md) · [Task design](./data/experiments/tasks/AGENTS.md) · [Execution and review](./data/experiments/AGENTS.md) · [Contributing](./docs/contributing.md) · [Flight findings](./docs/flights.zh-CN.md)

Code: [MIT](./LICENSE) · Data: [CC BY 4.0](./LICENSE-DATA).
