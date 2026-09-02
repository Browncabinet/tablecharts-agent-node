# TableCharts agent node

Drop-in examples: send a table to TableCharts, get a live dashboard URL back.

**Job:** JSON / CSV / Notion / Google Sheets / Salesforce URL → `dashboard_url` + `embed_iframe` in one hop.

- Site: https://tablecharts.co
- Agent card: https://tablecharts.co/.well-known/agent-card.json
- MCP: `npx -y @tablecharts/mcp-server`
- Demo: https://tablecharts.co/embed/4c17c69d-9663-4b64-bec9-d5b303e2dabd
- Health: https://xsbzchiryhqatvrzgyxm.supabase.co/functions/v1/health

## Grok (fastest path)

No local install.

1. Open https://grok.com/connectors
2. **New Connector → Custom**
3. Name: `Table Charts`
4. Server URL:

https://xsbzchiryhqatvrzgyxm.supabase.co/functions/v1/mcp-grok

5. Start a **new** chat and enable **Table Charts**
6. Paste the prompt in **Try it**.

Custom connectors need a public HTTPS MCP URL. On Grok Business/Enterprise an admin may have to allow custom MCP first.

## Try it

Use Table Charts. Return a live dashboard URL, not a screenshot.

month,revenue
Jan,42000
Feb,48000
Mar,56000

Title: Q1 Revenue

You should get a link like https://tablecharts.co/embed/...

## Cursor / Claude Desktop MCP

{
  "mcpServers": {
    "tablecharts": {
      "command": "npx",
      "args": ["-y", "@tablecharts/mcp-server"],
      "env": {
        "TABLECHARTS_API_KEY": "tc_live_your_key"
      }
    }
  }
}

Get a key at https://tablecharts.co/api-keys. Do not commit it.

## API key (LangGraph / CrewAI / REST)

export TABLECHARTS_API_KEY=tc_live_your_key

python3 examples/langgraph_chart_node.py
python3 examples/crewai_chart_agent.py

## Repo layout

- README.md
- SKILL.md
- .env.example
- examples/langgraph_chart_node.py
- examples/crewai_chart_agent.py
- examples/sample_data.json

## When an agent should use this

Use TableCharts when you already have tabular data and need a shareable, live-updating chart URL instead of a screenshot.
