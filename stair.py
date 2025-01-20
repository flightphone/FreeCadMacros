import FreeCAD as App
import Part
import math
import Mesh

from CADUtils import make_offset, make_rect



def stair():
    r = 11
    r2 = 2
    h = 36
    w = 2
    n = 12
    nr = 1
    doc = App.newDocument()
    points0 = [(0, 0, 0), (0, 0, w), (r, 0, w), (r, 0, 0), (0, 0, 0)]
    points1 = [(0, 0, -h), (0, 0, 0), (2*r, 0, 0), (2*r, 0, -h), (0, 0, -h)]
    loft = []
    loftm = []
    for i in range(2):
        prom = Part.makePolygon(points1)
        prom.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), i*nr*360 / n )
        prom.translate(App.Vector(0, 0, h*i/n))
        loftm.append(prom)

    stricut = Part.makeLoft(loftm, True, False)

    for i in range(n+1):
        pro = Part.makePolygon(points0)
        pro.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), i*nr*360 / n )
        pro.translate(App.Vector(0, 0, h*i/n))
        loft.append(pro)

    res = Part.makeLoft(loft, True, False)
    
    #res = res.fuse(stris)
    st = [res]
    for i in range(n):
        stris = Part.makeCylinder(r, h/n, App.Vector(0, 0, 0), App.Vector(0, 0, 1), nr*360 / n)
        stris.translate(App.Vector(0, 0, w))
        stris = stris.cut(stricut)
        stris.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), i*nr*360 / n)
        stris.translate(App.Vector(0, 0, i*h/n))
        st.append(stris)

    ci = Part.makeCylinder(r2, h + w)   
    st.append(ci)
    res = Part.makeCompound(st)     
    
    
    
    resf = doc.addObject("Part::Feature", "res")
    resf.Shape = res        
    doc.recompute()   
    Mesh.export([resf], "stl/stair2.stl")
    return res     

r = stair()    
#r.exportStl("stl/stair.stl")