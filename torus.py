import FreeCAD as App
import Part
import math
import Mesh

from CADUtils import  make_revolve, make_offset
doc = App.newDocument()
ci = Part.makeCircle(2, App.Vector(20, 0, 0), App.Vector(0, 1, 0))
res = make_revolve(doc, ci, "ci")
resf = doc.addObject("Part::Feature", "res")
resf.Shape = res        
doc.recompute()   
Mesh.export([resf], "stl/torus.stl")