import FreeCAD as App
import Part
import math
import Mesh

from CADUtils import make_offset

def amf():
    body = [(0, 22.), (10, 22.6), (32.8, 66.2), (65.6, 79), (81, 37.6),
            (93.8, 30.2), (106.2, 38.6)]
    loft = []
    doc = App.newDocument()
    for v in body:
        c = Part.makeCircle(v[1]/2, App.Vector(0, 0, v[0]))
        loft.append(c)
    
        
   
    res = Part.makeLoft(loft, True, False)
    resf = doc.addObject("Part::Feature", "res")
    resf.Shape = res        
    doc.recompute()   
    Mesh.export([resf], "stl/amf.stl")
    return res     

amf()