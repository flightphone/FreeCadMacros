import FreeCAD as App
import Part
import math
import Mesh

from CADUtils import make_offset

def glass():
    h = 105
    r1 = 55/2
    r2 = 85/2
    htop = 25
    hbot = 10
    th = 2
    doc = App.newDocument()
    res = Part.makeCone(r1, r2, h)
    glm = Part.makeCone(r1, r2, h, App.Vector(0, 0, 0.1))
    res = res.cut(glm)
    res = make_offset(doc, res, th, "body")
    
    ha = h-htop-hbot
    k =  (r2-r1)/h
    ra1 = r1 + hbot*k + th-0.8
    ra2 = r1 + (h - htop)*k + th-0.8
    glm2 = Part.makeCone(ra1, ra2, ha, App.Vector(0, 0, hbot))
    box = Part.makeBox(100, 100, ha, App.Vector(-50, -50, hbot))
    box = box.cut(glm2)
    res = res.cut(box)

    re = 3
    eps = -2
    n = 10
    ae = math.atan2(r2-r1, h)
    he = ha/math.cos(ae) - 2*re
    edg = Part.makeBox(100, 2*re, he, App.Vector(-50, -re, 0))
    cy1 = Part.makeCylinder(re, 100, App.Vector(-50, 0, 0), App.Vector(1, 0, 0))
    edg = edg.fuse(cy1)
    cy1.translate(App.Vector(0, 0, he))
    edg = edg.fuse(cy1)
    edg.rotate(App.Vector(0, 0, 0),App.Vector(1, 0, 0), -ae*180/math.pi)
    edg.translate(App.Vector(0, ra1-eps, hbot + re*0.8))
    for i in range(n):
        edg.rotate(App.Vector(0, 0, 0),App.Vector(0, 0, 1), 360/n)
        res = res.cut(edg)

    
    resf = doc.addObject("Part::Feature", "glass")
    resf.Shape = res
    Mesh.export([resf], "public/stl/render.stl")
    return res

glass()