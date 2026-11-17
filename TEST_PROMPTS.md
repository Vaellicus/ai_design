# Rhino 9 + Copilot Test Prompts

This file contains example prompts to test your Rhino 9 + GitHub Copilot MCP connection.

## Quick Tests (Start Here)

### Test 1: Connection Status
**Prompt:**
```
What objects are currently in the Rhino document? Give me a summary.
```

**Expected Result:** Copilot connects to Rhino and reports document state.

---

### Test 2: Create Simple Geometry
**Prompt:**
```
Create a sphere with radius 10 at the origin.
```

**Expected Result:** A sphere appears in the Rhino viewport.

---

### Test 3: Get Document Information
**Prompt:**
```
What is the current unit system and modeling tolerance in Rhino?
```

**Expected Result:** Copilot queries Rhino settings and reports them.

---

## Intermediate Tests

### Test 4: Create Multiple Objects
**Prompt:**
```
Create three boxes arranged in a row. First box at (0,0,0), second at (15,0,0), third at (30,0,0). Each box should be 10x10x10.
```

**Expected Result:** Three boxes appear in the Rhino viewport, spaced 15 units apart.

---

### Test 5: Geometric Analysis
**Prompt:**
```
Create a circle with radius 5. What is its circumference and area?
```

**Expected Result:** Copilot creates the circle and calculates/reports the measurements.

---

### Test 6: Array/Grid Pattern
**Prompt:**
```
Create a 4x4 grid of spheres. Each sphere has radius 2, and they're spaced 8 units apart in both X and Y directions, centered at the origin.
```

**Expected Result:** 16 spheres arranged in a 4x4 grid pattern.

---

## Advanced Tests

### Test 7: Parametric Design
**Prompt:**
```
Create a spiral curve that:
- Starts at the origin
- Has 10 complete rotations (turns)
- Rises vertically by 50 units total
- Has a base radius of 10 units
```

**Expected Result:** A 3D spiral curve is created in Rhino.

---

### Test 8: Procedural Generation
**Prompt:**
```
Create 20 random spheres with:
- Random positions within a 50x50x50 cube centered at origin
- Random radii between 1 and 5 units
- Random colors

Then tell me:
- How many spheres were created
- The average radius
- The bounding box of all spheres
```

**Expected Result:** 20 colored spheres are created with random properties, and Copilot reports statistics.

---

### Test 9: Mesh Creation
**Prompt:**
```
Create a simple mesh surface that forms a saddle shape (hyperbolic paraboloid) over a 20x20 unit area with 10x10 grid resolution.
```

**Expected Result:** A saddle-shaped mesh surface appears in Rhino.

---

### Test 10: Boolean Operations
**Prompt:**
```
Create two overlapping spheres (both radius 8):
- First sphere at (0, 0, 0)
- Second sphere at (10, 0, 0)

Then perform a Boolean union to create a single combined shape.
```

**Expected Result:** Two spheres appear, then merge into one unified shape.

---

## Workflow Tests

### Test 11: Script Generation
**Prompt:**
```
Write me a Python script that I can use in Rhino to:
1. Ask the user for the number of sides (3-8)
2. Ask for the radius
3. Create a regular polygon with those parameters
4. Report the perimeter

Include comments explaining each step.
```

**Expected Result:** Copilot generates a complete, commented Python script ready to use in Rhino.

---

### Test 12: Design Iteration
**Prompt:**
```
Create a simple architectural form:
- Base: a 20x20 meter square
- Height: 15 meters
- Add a pitched roof with a 30-degree angle

Then ask: what changes would make this more interesting as a building design?
```

**Expected Result:** Copilot creates the basic form and suggests design improvements.

---

## Diagnostic Tests

### Test 13: Check Available Tools
**Prompt:**
```
What tools and capabilities do you have access to in Rhino? List them all.
```

**Expected Result:** Copilot lists all available MCP tools for Rhino.

---

### Test 14: Error Handling
**Prompt:**
```
Try to create a sphere with a negative radius. What happens?
```

**Expected Result:** Copilot attempts the operation and either handles the error gracefully or reports why it failed.

---

## Tips for Best Results

1. **Be specific:** "Create a sphere" works, but "Create a sphere with radius 10 centered at the origin" is better.

2. **Ask follow-ups:** After creating geometry, ask Copilot to analyze, modify, or report on it.

3. **Request scripts:** Ask Copilot to generate reusable Python or RhinoScript code.

4. **Use coordinates:** When positioning objects, use explicit coordinates like (x, y, z).

5. **Check results:** After each prompt, visually verify the result in the Rhino viewport.

---

## Troubleshooting Test Failures

| Issue | Solution |
|-------|----------|
| "No tools available" | Reload VS Code, ensure Rhino is running |
| "Command failed" | Check if Rhino is responsive; restart it |
| "Invalid input" | Be more specific with parameters and units |
| "Timeout" | Rhino MCP server may be unresponsive; restart Rhino |

---

## Next Level: Custom Workflows

Once tests pass, try:

1. **Design iteration loops:** Ask Copilot to create variations and compare
2. **Data-driven design:** Generate geometry from lists/arrays you provide
3. **Optimization:** Ask Copilot to modify designs for specific criteria
4. **Documentation:** Generate design reports from Rhino models
5. **Integration:** Combine Rhino geometry with other tools via Copilot

---

For more information, see [README.md](./README.md) or the [official documentation](https://mcneel.github.io/RhinoAI/docs/).
