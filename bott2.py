import FreeCAD as App
import Part
import math
import Mesh
from BOPTools import BOPFeatures


def off_test():
    s1 = Part.makeSphere(3)
    s2 = Part.makeSphere(1.5)
    s2.translate(App.Vector(0, 0, 3))
    doc = App.newDocument()
    sp1 = doc.addObject("Part::Feature", "sp1")
    sp1.Shape = s1
    sp2 = doc.addObject("Part::Feature", "sp2")
    sp2.Shape = s2
    
    doc.addObject("Part::Offset","Offset")
    doc.Offset.Source = doc.sp1
    doc.Offset.Value = 0.2

    bp = BOPFeatures.BOPFeatures(doc)
    sph1 = bp.make_cut(["Offset", "sp1",])
    sph1Name = sph1.Name
    sph2 = bp.make_cut([sph1Name, "sp2",])
    sph2Name = sph2.Name
    doc.recompute()
    Mesh.export([sph2], "stl/offt.stl")
    return sph2.Shape

def off_test2():
    r = 50
    h = 100
    th = 10
    f = 2
    cy1 = Part.makeCylinder(r, h)
    s1 = Part.makeSphere(r)
    s1.translate(App.Vector(0, 0, h))
    bott = cy1.fuse(s1)
    cy2 = Part.makeCylinder(0.4*r, r + 0.4*h, App.Vector(0, 0, h), App.Vector(0, 0, 1), 360)
    
    bott = bott.fuse(cy2)
    doc = App.newDocument()
    bottf = doc.addObject("Part::Feature", "bottf")
    bottf.Shape = bott

    doc.addObject("Part::Offset","Offset")
    doc.Offset.Source = bottf
    doc.Offset.Value = th
    doc.recompute()
    bott1 = doc.Offset.Shape
    res = bott1.cut(bott) 
    cy3 = Part.makeCylinder(0.4*r, r + 0.5*h, App.Vector(0, 0, h), App.Vector(0, 0, 1), 360)
    res = res.cut(cy3)
    res = res.makeFillet(f, res.Edges)
    resf = doc.addObject("Part::Feature", "res")
    resf.Shape = res
    bottf.Visibility = False
    doc.Offset.Visibility = False

    

    Mesh.export([resf], "stl/bott2.stl")
    return res


res = off_test2()
#res.exportStl("stl/offt1.stl")