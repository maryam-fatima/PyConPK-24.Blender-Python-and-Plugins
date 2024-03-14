# Get access to Blender's functionality
import bpy

# Extend python's math functionality
import math

# Create variables used in loop
radius_step = 0.1
current_radius = 0.1
number_traingles = 30

z_step = 10

for i in range(1, number_traingles):
    #current_radius = current_radius + radius_step
    current_radius = i * radius_step
    bpy.ops.mesh.primitive_circle_add(vertices=3, radius=current_radius)
    # Get reference to currently active object
    triangle_mesh = bpy.context.active_object

    # Rotate mesh aroyund x-axis
    degrees = 90
    radians = math.radians(degrees)
    triangle_mesh.rotation_euler.x = radians

    # Rotate mesh aroyund z-axis
    degrees = z_step * i
    radians = math.radians(degrees)
    triangle_mesh.rotation_euler.z = radians

    # Convert mesh into a curve
    bpy.ops.object.convert(target='CURVE')

    # Add bevel to curve
    triangle_mesh.data.bevel_depth = 0.03
#    triangle_mesh.data.bevel_resolution = 16

    # shade smooth
    bpy.ops.object.shade_smooth()
