import bpy
import random

spacing = 2.2

#bpy.ops.material.new()
#bpy.context.object.active_material.name = "glass"
#bpy.data.materials["glass"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.431693, 0.685809, 0.763284, 1)
#bpy.data.materials["glass"].node_tree.nodes["Principled BSDF"].inputs[6].default_value = 0.7
#bpy.data.materials["glas"].node_tree.nodes["Principled BSDF"].inputs[8].default_value = 0.3

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

for y in range(10):
    for x in range (10):
        location = (x * spacing, y * spacing, random.random() * 2)
        bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=location, scale=(1, 1, 1))
        
        item = bpy.context.object
        
        if random.random() < 0.2:
            item.data.materials.append(bpy.data.materials["Material"])
        else:
            item.data.materials.append(bpy.data.materials["glass"])
