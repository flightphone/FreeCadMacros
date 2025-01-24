import FreeCAD as App
import Part
import math
import Mesh

from CADUtils import make_offset, make_rect
def conetop(r1, r2, h, d, w, n):
    h2 = h/2
    r3 = math.sqrt(h2*h2 + (r2-d)*(r2-d))
    res = Part.makeCone(r1, r2, h)
    box = Part.makeBox(r1+d, w, h, App.Vector(0, -w/2, 0))
    
    for i in range(n):
        box.rotate(App.Vector(0, 0, 0),App.Vector(0, 0, 1), 360/n)
        res = res.fuse(box)
    
    mcube = Part.makeBox(4*r1, 4*r1, h + d, App.Vector(-2*r1, -2*r1, 0))
    cone = Part.makeCone(r1+d, r2+d, h)
    mcube = mcube.cut(cone)
    res = res.cut(mcube)
    sp = Part.makeSphere(r3, App.Vector(0, 0, h + h2))
    res = res.cut(sp)
    return res


def tube():
    r = 3
    h = 12
    r2 = 1
    d = 0.25
    h2 = 3
    r3 = 0.7
    h3 = 1.5
    w = 0.05
    doc = App.newDocument()
    bot = make_rect(2*r, w)
    #bot = Part.makePlane(2*r, w, App.Vector(-r, -w/2, 0))
    cil = Part.makeCircle(r, App.Vector(0, 0, h))
    bodi = Part.makeLoft([bot, cil], True, False)
    
    cone = Part.makeCone(r, r2, h2, App.Vector(0, 0, h))
    
    #res = res.fuse(cone)
    cone2 = conetop(r2, r3, h3, 0.1, 0.15, 20)
    cone2.translate(App.Vector(0, 0, h+h2))
    #cone2 = Part.makeCone(r2, r3, h3, App.Vector(0, 0, h+h2))
    #res = res.fuse(cone2)

    sps = [bodi, cone, cone2]
    names = ["bodi", "cone", "top"]
    parts = []
    for i, e in zip(names, sps):
        rf = doc.addObject("Part::Feature", f"{i}")
        rf.Shape = e
        parts.append(rf)
        doc.recompute()
        #Mesh.export([rf], f"stl/tube/{i}.stl") 

    '''
    res = sps[0] 
    for i in range(1, len(sps)):
        res = res.fuse(sps[i])
    '''
    res = Part.makeCompound(sps)
    resf = doc.addObject("Part::Feature", "res")
    resf.Shape = res        
    doc.recompute()   
    Mesh.export([resf], "stl/tube.stl")
    return res     

r = tube()    
#r.exportStl("stl/royal2.stl")