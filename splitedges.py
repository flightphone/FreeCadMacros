import FreeCAD as App
import Part
import math
import Mesh

mesh = Mesh.Mesh("stl/prism.stl")

doc = App.newDocument() # Get a reference to the actie document
resf = doc.addObject("Mesh::Feature", "Mesh") # Create a mesh feature
resf.Mesh = mesh # Assign the mesh object to the internal property
doc.recompute()
Mesh.export([resf], "stl/prism_test.obj")