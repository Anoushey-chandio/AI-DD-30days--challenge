
# GitHub MCP Integration (Gemini CLI Agent)

I successfully added the **GitHub MCP Server** to my Gemini CLI Agent.

This integration allows me to interact with GitHub using natural language — including managing repositories, issues, pull requests, and workflows.

## Setup Summary

- Generated a GitHub Copilot (MCP TOKEN)
- Added it as an environment variable:

  ### setx GITHUB_MCP_PAT

- Configured the MCP server in `settings.json`:
```json
{
  "mcpServers": {
    "github": {
      "httpUrl": "https://api.githubcopilot.com/mcp/",
      "headers": {
        "Authorization": "Bearer ${GITHUB_MCP_PAT}"
      }
    }
  }
}




