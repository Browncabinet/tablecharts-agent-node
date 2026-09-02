# tablecharts-agent-node
Drop-in LangGraph and CrewAI examples: send a table to TableCharts, get a live dashboard URL back.
# TableCharts agent node

Drop-in examples so another agent can turn a table into a live dashboard URL.

**Job:** send JSON / CSV / a Notion, Google Sheets, or Salesforce URL → get `dashboard_url` + `embed_iframe` back in one hop.

- Site: https://tablecharts.co
- Agent card: https://tablecharts.co/.well-known/agent-card.json
- MCP: `npx -y @tablecharts/mcp-server`
- Demo: https://tablecharts.co/embed/4c17c69d-9663-4b64-bec9-d5b303e2dabd

## Repo layout

```text
README.md
SKILL.md
.env.example
examples/langgraph_chart_node.py
examples/crewai_chart_agent.py
examples/sample_data.json
