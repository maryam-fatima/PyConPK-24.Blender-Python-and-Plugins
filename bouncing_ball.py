import bpy

# Clean the scene
bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete()

# Add a surface for the ball to bounce
bpy.ops.mesh.primitive_plane_add(location=(0, 0, 0), scale=(2, 2, 2))
# Add physics
bpy.ops.rigidbody.object_add()
bpy.context.object.rigid_body.type = 'PASSIVE'
bpy.context.object.rigid_body.friction = 0
bpy.context.object.rigid_body.restitution = 1
bpy.context.object.data.materials.append(bpy.data.materials["Material.001"])

# Add ball and physics
bpy.ops.mesh.primitive_uv_sphere_add(location=(0,0,1.5), radius=0.1)
bpy.ops.object.shade_smooth()
bpy.ops.rigidbody.object_add()
bpy.context.object.rigid_body.type = 'ACTIVE'
bpy.context.object.rigid_body.friction = 0
bpy.context.object.rigid_body.restitution = 0.7
bpy.context.object.data.materials.append(bpy.data.materials["Material"])
