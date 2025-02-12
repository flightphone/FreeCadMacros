import FreeCAD as App
import Part
import math
import Mesh

from CADUtils import make_offset

def tadj_onion(r1, al):
    sp = Part.makeSphere(r1) 
    cn = Part.makeCone(r1*math.cos(al), 0, r1/math.cos(math.pi/2 - al) - r1*math.sin(al), App.Vector(0, 0, r1*math.sin(al)))
    res = sp.fuse(cn)
    return res

def shotglass():
    doc = App.newDocument()
    r = 1
    h = 1.2*r
    th = 0.001
    th2 = 0.01
    th3 = 0.01
    al = math.pi*0.08
    res = tadj_onion(r, al)
    mres = tadj_onion(r-th, al)
    top = Part.makeBox(10, 10, 10, App.Vector(-5, -5, h))
    res = res.cut(top)
    mres = mres.cut(top)
    res = res.cut(mres)
    res = make_offset(doc, res, th2, "vol1")

    h3 = 1.6*r
    r3 = 0.1
    h4 =0.1
    r4 = r + th2 + th3
    foot = Part.makeCylinder(r3, h3, App.Vector(0, 0, -h3-r))
    di = Part.makeCylinder(r4, h4, App.Vector(0, 0, -h3-r-h4))
    foot = foot.fuse(di)
    foot = foot.makeFillet(0.04, foot.Edges)

    
    res = res.fuse(foot)

    dl = h/4
    res2 = tadj_onion(r+th3, al)
    top.translate(App.Vector(0, 0, -dl))
    res2 = res2.cut(top)
    res2 = make_offset(doc, res2, th2, "vol2")
    res2 = res2.cut(mres)


    plane = Part.makeBox(0.1, 10, 20, App.Vector(r4, -5, -15))
    #res = res.fuse(plane)
    #res = res.fuse(res2)
    sps = [res, res2, plane]
    names = ["vol_res", "vol_res2", "plane"]
    for i, e in zip(names, sps):
        rf = doc.addObject("Part::Feature", f"{i}")
        rf.Shape = e
        doc.recompute()
        Mesh.export([rf], f"stl/shotglass/{i}.stl") 

    result = Part.makeCompound(sps)
    resf = doc.addObject("Part::Feature", "shotglass")
    resf.Shape = result
    Mesh.export([resf], "stl/shotglass.stl")
    return res

shotglass()
print("shot_ok")