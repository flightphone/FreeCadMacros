import FreeCAD as App
import Part
import math
import Mesh

from CADUtils import make_offset

def tpot():
    h = 10
    r = 4
    sr = 4.2
    th = 0.05
    th2 = 0.3
    doc = App.newDocument()
    res = Part.makeCylinder(r, h)
    cube = Part.makeBox(sr, sr, 3*sr, App.Vector(-sr/2, -sr/2, -1.5*sr), App.Vector(1, 1, 2.3))
    cube.translate(App.Vector(0, 0, h+0.7*sr))
    res = res.fuse(cube)
    cubem = Part.makeBox(200,200, 200, App.Vector(-100, -100, h))
    res = res.cut(cubem)
    inne = make_offset(doc, res, -th, "inne")
    res = res.cut(inne)
    
    tor = Part.makeTorus(h/3, 0.8, App.Vector(0,0, h/2), App.Vector(0, 1, 0))
    myMat = App.Matrix()
    myMat.scale(0.6, 1, 1)
    tor=tor.transformGeometry(myMat)
    tor.rotate(App.Vector(0, 0, 0),App.Vector(0, 0, 1), 45)
    tor.translate(App.Vector(-0.7*r, -0.7*r, 0))
    tor = tor.cut(inne)
    
    cubem2 = Part.makeBox(200,200, 200, App.Vector(-100, -100, h-th-0.01))
    res = res.cut(cubem2)
    res = make_offset(doc, res, th2, "oute")
    res = res.makeFillet(0.1, res.Edges)
    
    res = res.fuse(tor)

    resf = doc.addObject("Part::Feature", "res")
    resf.Shape = res        
    doc.recompute()   
    Mesh.export([resf], "stl/teapot.stl")
    return res  

tpot()