import bpy

# Clean the scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()


# Create sphere to place cloth on
bpy.ops.mesh.primitive_uv_sphere_add(location=(0,0,0), radius=0.7)
# Subdivide to add geometry for better interaction with cloth
bpy.ops.object.modifier_add(type='SUBSURF')
bpy.context.object.modifiers["Subdivision"].levels = 2
bpy.ops.object.modifier_add(type='COLLISION')

bpy.ops.object.shade_smooth()
bpy.context.object.data.materials.append(bpy.data.materials["Material"])

# Add a plane for cloth
bpy.ops.mesh.primitive_plane_add(location=(0, 0, 1), size=2)
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.subdivide(number_cuts=20)
bpy.ops.object.mode_set(mode='OBJECT')

# Add cloth modifier and configure
bpy.ops.object.modifier_add(type='CLOTH')
bpy.context.object.modifiers["Cloth"].collision_settings.distance_min = 0.0001
bpy.context.object.modifiers["Cloth"].collision_settings.use_self_collision = True
bpy.context.object.modifiers["Cloth"].collision_settings.self_distance_min = 0.0015
bpy.context.object.modifiers["Cloth"].settings.quality = 8
bpy.context.object.modifiers["Cloth"].collision_settings.collision_quality = 4
bpy.context.object.modifiers["Cloth"].point_cache.frame_end = 60

# Add thickness to cloth using solidify and smoothen it using subdivide
bpy.ops.object.modifier_add(type='SOLIDIFY')
bpy.context.object.modifiers["Solidify"].thickness = 0.001
bpy.ops.object.modifier_add(type='SUBSURF')
bpy.context.object.data.materials.append(bpy.data.materials["Material.001"])
bpy.ops.object.shade_smooth()

# Go to start frame
bpy.context.scene.frame_current = 1
