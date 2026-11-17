# Rhino 9 + GitHub Copilot MCP Setup Checklist

Use this checklist to verify your setup is complete and working.

## ✅ Prerequisites Check

- [ ] Rhinoceros 9 is installed and working
- [ ] VS Code 1.99 or newer is installed
- [ ] GitHub Copilot extension is installed in VS Code
- [ ] GitHub Copilot Chat extension is installed in VS Code
- [ ] You are signed into both Copilot extensions with your GitHub account
- [ ] Node.js is installed (for running rhino-mcp-router)

**If any of these are unchecked, complete them before proceeding.**

---

## 🔧 Installation Steps

### In Rhinoceros 9

- [ ] Open Rhinoceros 9
- [ ] Run `PackageManager` command
- [ ] Search for "Rhino-MCP-Platform"
- [ ] Install the package
- [ ] Restart Rhinoceros to complete installation
- [ ] Run `MCPConnect` command to verify MCP is available
- [ ] Note the output from MCPConnect (should show `rhino-mcp-router --default-version 9`)

### In VS Code

- [ ] Navigate to your project folder: `F:\DISEÑO\AI Rhino and Blender\ai_design`
- [ ] Verify `.vscode/mcp.json` exists (it should - we created it)
- [ ] Open `.vscode/mcp.json` and verify it contains:
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
- [ ] Press `Ctrl+Shift+P` and select "Reload Window"
- [ ] Wait for VS Code to reload completely

---

## 🚀 Activation Steps

- [ ] Open Copilot Chat (Ctrl+Shift+I or Cmd+Shift+I)
- [ ] Look for the **mode selector** at the top of the chat panel
- [ ] Switch from "Ask" mode to "Agent" mode
- [ ] In the tool picker, you should see `rhino` server listed
- [ ] Verify Rhino 9 is running (keep it open in the background)

---

## 🧪 Connection Tests

### Quick Connection Test
- [ ] Open Copilot Chat in Agent mode
- [ ] Type: `What's in the current Rhino document?`
- [ ] Send and verify Copilot connects without errors
- [ ] Look for the Rhino icon in the tool indicator

### Create First Object
- [ ] In Agent mode, type: `Create a sphere with radius 10`
- [ ] Send the prompt
- [ ] Check the Rhino viewport - a sphere should appear
- [ ] ✅ **If the sphere appears, your setup is working!**

### Test a More Complex Command
- [ ] Type: `Create a 3x3 grid of boxes, each 5x5x5 units, spaced 10 units apart`
- [ ] Send and verify the boxes appear in Rhino
- [ ] ✅ **If this works, you're ready for advanced use!**

---

## 📋 Configuration Files Check

Verify these files exist in your project:

- [ ] `.vscode/mcp.json` - MCP server configuration
- [ ] `README.md` - Setup documentation
- [ ] `TEST_PROMPTS.md` - Test prompts and examples

**Location:** `F:\DISEÑO\AI Rhino and Blender\ai_design\`

---

## 🐛 Troubleshooting

### "Rhino server not found in tool picker"

**Checklist:**
- [ ] `.vscode/mcp.json` exists and has correct content
- [ ] You're in "Agent" mode (not "Ask" mode)
- [ ] Reloaded VS Code (Ctrl+Shift+P → Reload Window)
- [ ] Rhino 9 is running
- [ ] `rhino-mcp-router` command is available in PATH

**Action:** If still not working, restart both Rhino and VS Code in this order:
1. Close VS Code
2. Close Rhino
3. Open Rhino 9
4. Open VS Code
5. Open Copilot Chat in Agent mode

---

### "MCPConnect command not found in Rhino"

**Checklist:**
- [ ] Rhino-MCP-Platform package is installed
- [ ] Rhino was restarted after installation
- [ ] You're using Rhino 9 (not Rhino 8)

**Action:** Reinstall the Rhino-MCP-Platform package:
1. Open Rhino
2. Run `PackageManager`
3. Uninstall Rhino-MCP-Platform
4. Reinstall Rhino-MCP-Platform
5. Restart Rhino
6. Run `MCPConnect` again

---

### "Copilot says: No tools available"

**Checklist:**
- [ ] Rhino 9 is currently running
- [ ] MCP Connection is active in Rhino (run `MCPConnect` to check)
- [ ] `.vscode/mcp.json` has `"--default-version", "9"` (not "8")
- [ ] You're in Agent mode in Copilot Chat

**Action:** 
1. Verify Rhino is responding (try running a command in Rhino directly)
2. Restart the MCP router by reloading VS Code
3. If still stuck, restart Rhino and VS Code

---

### Connection timeout or no response

**Checklist:**
- [ ] Rhino is not frozen or in a dialog
- [ ] No other heavy processes are running
- [ ] VS Code Output panel shows no MCP errors (View → Output → select "MCP" from dropdown)

**Action:**
1. Click in the Rhino window to focus it
2. Press Escape to close any dialogs
3. Reload VS Code

---

## 📚 Next Steps

Once everything is working:

1. **Review TEST_PROMPTS.md** for example prompts
2. **Try the basic tests** to get familiar with the workflow
3. **Build your own scripts** using Copilot in Agent mode
4. **Store custom tools** and workflows in this repository
5. **Integrate with your design pipeline**

---

## 💡 Tips for Success

- **Keep Rhino running** in the background while using Copilot
- **Be specific** in your prompts (include coordinates, dimensions, colors)
- **Ask follow-up questions** after creating geometry
- **Request generated scripts** you can reuse
- **Check the VS Code Output panel** (View → Output → MCP) if something goes wrong

---

## Resources

- 📖 [Rhino MCP Documentation](https://mcneel.github.io/RhinoAI/docs/getting-started/copilot/)
- 🤖 [GitHub Copilot Docs](https://github.com/features/copilot)
- 🔌 [Model Context Protocol](https://modelcontextprotocol.io/)
- 📝 [README.md](./README.md) - Full setup guide
- ✏️ [TEST_PROMPTS.md](./TEST_PROMPTS.md) - Example prompts

---

## Done! ✨

When all checkboxes are complete, you're ready to use Rhino 9 with GitHub Copilot. Start with the basic tests in TEST_PROMPTS.md and work your way up!

**Happy designing with AI assistance!** 🎨
