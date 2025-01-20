import numpy
from stl import mesh

# Using an existing stl file:
mm = mesh.Mesh.from_file('stl/kipr.stl')

mm.save('stl/kipr2.stl')