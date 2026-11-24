import bpy

# Clean scene
bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete(use_global=False)

# Add sphere at origin with radius 10 mm (0.01 m in Blender default units)
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.01, location=(0.0, 0.0, 0.0))

obj = bpy.context.active_object
if obj:
    obj.name = "Sphere_10mm"

print("Created Sphere_10mm at origin with 10 mm radius.")
