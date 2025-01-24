import FreeCAD as App
import Part
import math
import Mesh

from CADUtils import make_offset, make_rect

def grani(sp, r, n, h = 100, w = 10):
    res = sp
    a = 360/n
    box = Part.makeBox(w, 2*r*math.sin(math.pi/n), h, App.Vector(r*math.cos(math.pi/n), -r*math.sin(math.pi/n), 0))
    for i in range(n):
        box.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 360/n)
        res = res.cut(box)
    return res

def make_ring(r, h, w):
    res = Part.makeCylinder(r+w, h)
    cyl = Part.makeCylinder(r, h)
    res = res.cut(cyl)
    return res

def pensel():
    h = 3.71
    r = 0.92/2
    h2 = 0.65
    r2 = 0.29/2
    w = 0.001
    h3 = 0.74
    f = 0.1
    doc = App.newDocument()
    cyl = Part.makeCylinder(r, h)
    cone = Part.makeCone(r, r2, h2, App.Vector(0, 0, h))
    cone1 = Part.makeCone(r-w, r2-w, h2, App.Vector(0, 0, h))
    cyl = cyl.fuse(cone1)
    cyl = grani(cyl, r, 6)
    h4 = r2*h2/(r-r2)
    cone2 = Part.makeCone(r2, 0, h4, App.Vector(0, 0, h+h2))

    cone = cone.cut(cone1)
    cone = grani(cone, r, 6)
    #cone.translate(App.Vector(0, 0, 0.2))
    #plane = Part.makeBox(30, 30, 0.5, App.Vector(-15, -15, h + h2 + h4))
    #plane.rotate(App.Vector(0, 0, h + h2 + h4), App.Vector(1, 0, 0), 10)

    lst = Part.makeCylinder(r-f, h3, App.Vector(0, 0, -h3))
    lst = make_offset(doc, lst, f, "lastic")
    
    rings = []
    for i in range(6):
        rin = make_ring(r, 0.1, 0.01)
        rin.translate(App.Vector(0, 0, 0.3/2 - i*0.1/2))
        rings.append(rin)



    rings.extend([cyl, cone2, cone, lst])
    res = Part.makeCompound(rings)
    
    resfl = []
    for i, e in enumerate(rings):
        rf = doc.addObject("Part::Feature", f"res{i}")
        rf.Shape = e
        resfl.append(rf)
        doc.recompute()
        Mesh.export([rf], f"stl/pensil/res{i}.stl") 

    Mesh.export(resfl, "stl/pensel.stl")
      

    
    #Секретный код 100!!!!
    #resall = doc.addObject("Part::Feature", "allc")
    #resall.Shape = res        
    #doc.recompute()   
    
    return res     

r = pensel()    
#r.exportStl("stl/pensel.stl")