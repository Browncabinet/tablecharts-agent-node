# TableCharts agent node

Drop-in LangGraph and CrewAI examples: send a table to TableCharts, get a live dashboard URL back.

**Job:** send JSON / CSV / a Notion, Google Sheets, or Salesforce URL → get `dashboard_url` + `embed_iframe` back in one hop.

- Site: https://tablecharts.co
- Agent card: https://tablecharts.co/.well-known/agent-card.json
- MCP: `npx -y @tablecharts/mcp-server`
- Demo: https://tablecharts.co/embed/4c17c69d-9663-4b64-bec9-d5b303e2dabd

## Repo layout

- README.md
- SKILL.md
- .env.example
- examples/langgraph_chart_node.py
- examples/crewai_chart_agent.py
- examples/sample_data.json

## Grok custom connector

https://xsbzchiryhqatvrzgyxm.supabase.co/functions/v1/mcp-grok

## Setup

Get an API key at https://tablecharts.co/api-keys then:

    export TABLECHARTS_API_KEY=tc_live_your_key

Do not commit the real key.

## LangGraph

    python3 examples/langgraph_chart_node.py

## CrewAI + MCP

    python3 examples/crewai_chart_agent.py

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

## When an agent should use this

Use TableCharts when you already have tabular data and need a shareable, live-updating chart.
