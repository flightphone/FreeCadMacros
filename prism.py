import FreeCAD as App
import Part
import math
import Mesh

from CADUtils import make_offset

def marc(r, h, l = 10):
    th = -0.1*r
    box = Part.makeBox(l, 2*r, h)
    box.translate(App.Vector(th, -r, 0))
    cy = Part.makeCylinder(r, l, App.Vector(th, 0, h), App.Vector(1, 0, 0), 360)
    box = box.fuse(cy)
    return box

def prism(n, r, h):
    a = math.pi*2/n
    points = [(r*math.cos(-a/2 + t*a), r*math.sin(-a/2 + t*a), 0) for t in range(n+1)]

    bot = Part.makePolygon(points)
    botw = Part.Wire(bot)
    botf = Part.Face(botw)
    pri=botf.extrude(App.Vector(0, 0, h))
    
    faces = [botf]
    v = (0, 0, 2*h/3)
    
    for i in range(n):
        p = Part.makePolygon([points[i], points[i+1], v, points[i]])
        pw = Part.Wire(p)
        pf = Part.Face(pw)
        faces.append(pf)

    

    pri2 = Part.makeShell(faces)
    pri3 = Part.makeSolid(pri2)
    pri3.translate(App.Vector(0, 0, h-0.001))
    res = pri
    res = pri.fuse(pri3)
    ra = 0.5 * r*math.sin(a/2)
    ha = 0.5*h
    ma = marc(ra, ha)
    for i in range(n):
        ma.rotate(App.Vector(0, 0, 0),App.Vector(0, 0, 1), a*180/math.pi)
        res = res.cut(ma)

    '''
    fi = [2, 3, 4, 5, 23, 24, 25, 26, 34, 35, 36, 37, 50, 51, 52, 53, 81, 82, 83, 84, 95, 96, 97, 98, 126, 127, 128, 129, 138, 139, 140, 141]
    fil = [res.Edges[i] for i in fi]
    res = res.makeFillet(0.2, fil)
    '''
    doc = App.newDocument()
    resf = doc.addObject("Part::Feature", "res")
    resf.Shape = res
    Mesh.export([resf], "stl/prism.stl")
    return res


el = prism(5, 5, 8)

