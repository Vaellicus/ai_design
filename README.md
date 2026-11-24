# Rhino 9 and GitHub Copilot MCP

GitHub Copilot can act as an MCP client for Rhino 9 from VS Code. The previous
setup in this repository was incorrect: the router was not on `PATH`, and it
incorrectly told Rhino 9 users to install the Rhino 8-only Yak package.

## What Rhino 9 includes

On this Windows installation, Rhino 9 already contains:

- `C:\Program Files\Rhino 9\Plug-ins\RhinoAI\net8.0\RhinoAI.rhp`
- `C:\Program Files\Rhino 9\Plug-ins\RhinoAI\router\win-x64\rhino-mcp-router.exe`
- A staged copy under
  `%APPDATA%\McNeel\Rhinoceros\ai\bin\rhino-mcp-router.exe`

The Rhino 9 build is bundled with Rhino, so do **not** install
`Rhino-MCP-Platform` in Rhino 9. The official project's build packages that
Yak package only for Rhino 8; the Rhino 9 version is shipped inside Rhino.

The configured router was tested locally and identified itself as
`rhino-mcp-router Rhino 9.1` during an MCP `initialize` exchange. This verifies
the executable and protocol handshake, but it is not an end-to-end test of
geometry operations while Rhino is running.

## VS Code configuration

The workspace configuration is [`.vscode/mcp.json`](.vscode/mcp.json):

```json
{
  "servers": {
    "rhino": {
      "type": "stdio",
      "command": "C:\\Users\\marco\\AppData\\Roaming\\McNeel\\Rhinoceros\\ai\\bin\\rhino-mcp-router.exe",
      "env": {
        "RHINO_MCP_DEFAULT_VERSION": "9"
      }
    }
  }
}
```

This is the exact configuration printed by `MCPConnect` on this machine. The
router is staged in Rhino's app-data directory so it remains reachable outside
the Rhino installation directory. Do not manually substitute another user's
profile path when moving this workspace to a different computer; rerun
`MCPConnect` there and copy its output.

## Connect

1. Start Rhino 9 and open a document.
2. In Rhino, run `MCPConnect`.
   - If `MCPConnect` prints a different router command, update
     [`.vscode/mcp.json`](.vscode/mcp.json) with that output.
   - In builds that expose `MCPStart` instead, run it to start the MCP listener.
3. Reload VS Code with **Developer: Reload Window**.
4. Open GitHub Copilot Chat and select **Agent** mode.
5. Open the tool picker and confirm that the `rhino` server and its tools are
   available.

`RHINO_MCP_DEFAULT_VERSION=9` selects Rhino 9. The router is a client-side
bridge; it does not replace the listener running in Rhino.

## Verify end to end

Use a small, reversible prompt first:

```text
Report the unit system and object count in the current Rhino document.
Do not modify the document.
```

Then test a write:

```text
Create one point at (0, 0, 0) in the current Rhino document.
```

Delete the point after confirming it appears. If the tools are listed but
calls fail, keep Rhino open and inspect the Copilot Chat MCP log and Rhino's
command history. Verify that Rhino's MCP listener is active.

## Troubleshooting

### `rhino-mcp-router` not found

The executable is not on `PATH`. Use its full path as shown in
`.vscode/mcp.json`, or use the command printed by Rhino's `MCPConnect` command.

### The server starts but Rhino tools cannot be called

Rhino may not have an active MCP listener:

1. Run `MCPConnect` or `MCPStart` in Rhino.
2. Keep the Rhino 9 process and the target document open.
3. Reload VS Code after Rhino starts.
4. Retry the read-only verification prompt.

### Rhino 9 versus Rhino 8

- **Rhino 9:** RhinoAI and the router ship inside Rhino.
- **Rhino 8:** install the `Rhino-MCP-Platform` Yak package and use
  `RHINO_MCP_DEFAULT_VERSION=8` or the equivalent `--default-version 8` option.

Do not use the Rhino 8 package as a Rhino 9 installation procedure.

## Official references

- [McNeel Copilot instructions](https://mcneel.github.io/RhinoAI/docs/getting-started/copilot/)
- [RhinoAI source repository](https://github.com/mcneel/RhinoAI)
- [Current RhinoAI release](https://github.com/mcneel/RhinoAI/releases/latest)

The official Copilot page currently has potentially confusing wording: its
plugin-install section is marked “Rhino 8 only,” while its later note mentions
`--default-version 9` for Rhino 9. The RhinoAI build configuration resolves
that contradiction: Rhino 9 is bundled with Rhino and is not packaged as a Yak
plugin.

## Blender control from VS Code

This workspace also includes a task-based Blender scripting workflow:

- [`.vscode/tasks.json`](.vscode/tasks.json)
- [`scripts/blender_sample_sphere.py`](scripts/blender_sample_sphere.py)

Configured Blender launcher:

`C:\Program Files\Blender Foundation\Blender 5.3\blender-launcher.exe`

Available tasks:

- **Blender: Run active script** (runs the currently open Python file)
- **Blender: Run sample sphere script** (creates a 10 mm radius sphere at origin)
