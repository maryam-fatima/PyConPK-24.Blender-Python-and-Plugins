import bpy

bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete()

bpy.context.scene.frame_current = 1

# Add a cube
bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0), size=1)

# Rotate the cube at frame 1
bpy.context.object.rotation_euler = (0, 0, 0)
bpy.context.object.keyframe_insert(data_path="rotation_euler", frame=1)

bpy.context.scene.frame_current = 30

# Rotate the cube by 180 degrees at frame 30
bpy.context.object.rotation_euler = (0, 0, 3.1415)
bpy.context.object.keyframe_insert(data_path="rotation_euler", frame=30)

bpy.context.scene.frame_current = 60

# Rotate the cube by 360 degrees at frame 60
bpy.context.object.rotation_euler = (0, 6.2830, 0)
bpy.context.object.keyframe_insert(data_path="rotation_euler", frame=60)

# Reset the frame to 1
bpy.context.scene.frame_current = 1

