import FreeCAD as App
import Part
import math
import Mesh

from CADUtils import make_offset

def plane():
    body = [(73.6, 48.6), (55.2, 78), (17, 75.8), (0, 50.4)]
    spout = [(14.5, 37.6, 90, 26.), (15.1, 36.0, 90, 38.8), (52.3, 12.7, 34.2, 57.6), (61.6, 9.6, 34.2, 64.2), (70, 15.9, 16.1, 75.3)]
    th = -4
    loft = []
    loftsp = []
    doc = App.newDocument()
    res = Part.makePlane(10, 10, App.Vector(-5, -5, 0))
    for v in body:
        c = Part.makeCircle(v[1]/2, App.Vector(0, 0, v[0]))
        loft.append(c)
        pw = Part.Wire(c)
        pf = Part.Face(pw)
        res = res.fuse(pf)

    for i, v in enumerate(spout):
        r = v[1]/2
        h = v[0]
        x = v[3]
        a = v[2]/180
        mat = App.Matrix()
        mat.scale(1, 0.5, 1)
        
        mat2 = App.Matrix()
        mat2.rotateY(a*math.pi)
        mat2.move(App.Vector(x - r*math.cos(a), 0, h + r*math.sin(a)))
        e = Part.makeCircle(r)
                
        e.transformGeometry(mat)
        e.transformShape(mat2)
        loftsp.append(e)  

        pw = Part.Wire(e)
        pf = Part.Face(pw)
        res = res.fuse(pf)      

    #res = Part.makePlane(10, 10, App.Vector(-5, -5, 0))
    resf = doc.addObject("Part::Feature", "res")
    resf.Shape = res        
    doc.recompute()   
    Mesh.export([resf], "stl/plane.stl")
    return res             

plane()