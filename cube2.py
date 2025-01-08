import FreeCAD as App
import Part
import math
import Mesh


from CADUtils import make_offset

def cube2():
    h = 10
    doc = App.newDocument()
    #res = Part.makePlane(10, 10, App.Vector(-5, -5, 0))
    res = Part.makeBox(h, h, h)

    for i in range(2):
        for j in range(2):
            for k in range(2):
                x = i*h
                y = j*h
                z = k*h
                v0 = App.Vector(h/2, y, z)
                v1 = App.Vector(x, h/2, z)
                v2 = App.Vector(x, y, h/2)
                nor = App.Vector(x, y, z) - App.Vector(h/2, h/2, h/2)

                vects = [v0, v1, v2, v0]
                points = []
                for v in vects:
                    points.append((v.x, v.y, v.z))
                bot = Part.makePolygon(points)
                botw = Part.Wire(bot)
                botf = Part.Face(botw)
                botp=botf.extrude(nor)
                res = res.cut(botp)

    res = make_offset(doc, res, 1, "res")
    resf = doc.addObject("Part::Feature", "res")
    resf.Shape = res        
    doc.recompute()   
    Mesh.export([resf], "stl/cube2.stl")
    return res  

cube2()

