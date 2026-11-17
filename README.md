# AI Design - Rhino 9 + GitHub Copilot MCP Integration

This repository integrates **Rhinoceros 9** with **GitHub Copilot** using the Model Context Protocol (MCP). This allows you to use Copilot to generate, analyze, and automate Rhino scripts directly from VS Code.

## Prerequisites

- **Rhinoceros 9** (WIP/BETA or later)
- **VS Code 1.99+** with:
  - GitHub Copilot extension
  - GitHub Copilot Chat extension
  - Both extensions signed in with your GitHub account
- **Node.js** (for running the MCP router)

## Setup Instructions

### Step 1: Install the Rhino MCP Plugin

1. Open **Rhinoceros 9**
2. Run the `PackageManager` command
3. Search for and install **Rhino-MCP-Platform**
4. Restart Rhino to complete installation

### Step 2: Get the MCP Connection Command

1. In Rhino 9, run the `MCPConnect` command
2. This will output the MCP server configuration details needed for Copilot
3. The command output should include something like:
   ```
   rhino-mcp-router --default-version 9
   ```

### Step 3: MCP Configuration Already Set Up ✅

The file [`.vscode/mcp.json`](.vscode/mcp.json) is already configured in this repository:

```json
{
  "servers": {
    "rhino": {
      "command": "rhino-mcp-router",
      "args": ["--default-version", "9"]
    }
  }
}
```

### Step 4: Activate Agent Mode in VS Code

1. Open **Copilot Chat** in VS Code
   - If not visible, press `Ctrl+Shift+I` (Windows) or `Cmd+Shift+I` (Mac)
2. Look for the **mode selector** at the top of the chat panel
3. Switch from **Ask** mode to **Agent** mode
4. You should now see the `rhino` server and its tools listed

### Step 5: Reload VS Code

Press `Ctrl+Shift+P` and select "Reload Window" to ensure the MCP configuration is loaded.

---

## Testing the Connection

Once everything is set up, try these test prompts in **Agent mode** to verify the connection:

### Test 1: Simple Geometry Query
```
What objects are currently in the Rhino document?
```

### Test 2: Create a Basic Shape
```
Create a sphere with radius 5 at the origin in Rhino.
```

### Test 3: Get Document Info
```
What is the current unit system in Rhino?
```

### Test 4: Analyze Geometry
```
Create a 10x10 rectangle and tell me its area.
```

### Test 5: Advanced Scripting
```
In Rhino, create a grid of spheres (3x3x3) with 2 units spacing between them.
```

---

## Project Structure

```
ai_design/
├── .vscode/
│   └── mcp.json              # MCP configuration for Rhino 9
├── .git/                     # Git repository
└── README.md                 # This file
```

---

## How to Use Copilot with Rhino

### Basic Workflow

1. **Open Copilot Chat** in Agent mode
2. **Ask a question or request** related to Rhino geometry/scripting
3. **Copilot will:**
   - Access Rhino's MCP tools
   - Execute commands in Rhino
   - Query document state
   - Return results with Rhino geometry/data

### Example Interactions

**Request:** "Draw a spiral curve with 10 turns"
**Copilot will:** Execute Rhino commands to create the spiral

**Request:** "List all curves in the document and their lengths"
**Copilot will:** Query Rhino objects and report back

**Request:** "Create a parametric design with 100 random spheres between z=0 and z=10"
**Copilot will:** Generate and execute the script

---

## Troubleshooting

### "Rhino server not found in tool picker"

1. ✅ Verify `.vscode/mcp.json` exists and contains the correct configuration
2. ✅ Confirm you're in **Agent mode** (not Ask mode)
3. ✅ Reload VS Code: `Ctrl+Shift+P` → "Reload Window"
4. ✅ Verify `rhino-mcp-router` is installed/accessible in your PATH

### "MCPConnect command not found in Rhino"

1. ✅ Confirm Rhino 9 is running
2. ✅ Verify the **Rhino-MCP-Platform** plugin is installed
3. ✅ Restart Rhino after installation

### Copilot says "No tools available"

1. ✅ Make sure Rhino 9 is running (MCP server must be active)
2. ✅ Check that you're using Rhino 9, not Rhino 8
3. ✅ Verify `args` in `.vscode/mcp.json` has `"--default-version", "9"`

### Connection Issues

If Copilot can't connect to Rhino:

1. Check VS Code Output panel: Look for "MCP" or "rhino" logs
2. Verify Rhino is running and responsive
3. Try reloading the VS Code window
4. Restart Rhino and reload VS Code in that order

---

## Documentation

- [Rhino MCP Documentation](https://mcneel.github.io/RhinoAI/docs/getting-started/copilot/)
- [GitHub Copilot Docs](https://github.com/features/copilot)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)

---

## Next Steps

After verifying the connection:

1. **Create Rhino scripts** using Copilot
2. **Store custom tools** in this repository
3. **Document design workflows** that use Copilot + Rhino
4. **Build automated design systems** leveraging both platforms

---

## Questions or Issues?

Refer to the [official Rhino MCP documentation](https://mcneel.github.io/RhinoAI/docs/) or check the VS Code MCP server logs in the Output panel.
