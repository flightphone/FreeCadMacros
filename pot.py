import FreeCAD as App
import Part
import math
import Mesh

from CADUtils import make_offset

def pot():
    rp = 20
    th = 2.5
    sp = 12
    h1 = math.sqrt(rp*rp - sp*sp)
    d2 = th*h1/rp
    doc = App.newDocument()
    res = Part.makeSphere(rp)
    box = Part.makeBox(50, 50, 20)
    box.translate(App.Vector(-25, -25, -37))
    res = res.cut(box)
    res1 = make_offset(doc, res, -th, "pot")
    res = res.cut(res1)
    cy = Part.makeCylinder (sp, 30, App.Vector(0, 0, 10))
    res = res.cut(cy)

    tor = Part.makeTorus(sp, d2, App.Vector(0, 0, h1 - d2))
    res = res.fuse(tor)
    
    #res = res.makeFillet(1, [res.Edges[2], res.Edges[4]])
    resf = doc.addObject("Part::Feature", "res")
    resf.Shape = res        
    doc.recompute()   
    Mesh.export([resf], "stl/pot.stl")
    return res            


pot()