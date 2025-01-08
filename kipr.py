import FreeCAD as App
import Part
import math
import Mesh


from CADUtils import make_offset

def marc(r, h, l = 10):
    box = Part.makeBox(l, 2*r, h)
    box.translate(App.Vector(0, -r, 0))
    cy = Part.makeCylinder(r, l, App.Vector(0, 0, h), App.Vector(1, 0, 0))
    box = box.fuse(cy)
    return box

def kipr():
    h = 13.6
    w = 22.2
    h2 = 7.8
    h22 = h+h2 + 2
    d = 1.5
    w2 = 12.4
    d2 = 0.7
    h3 = 31
    l = w + 2*w2
    r0 = 0.9*w/2
    r = 1.3*r0

    doc = App.newDocument()
    aPnt1=App.Vector(- w / 2 - d, 0, h)
    aPnt2=App.Vector(- w / 2, 0, h)
    aPnt3=App.Vector(0, 0, h+h2)
    aPnt4=App.Vector(w/2, 0, h)
    aPnt5=App.Vector(w/2 + d, 0, h)

    aArcOfCircle = Part.Arc(aPnt2, aPnt3, aPnt4)
    aSegment1=Part.LineSegment(aPnt1, aPnt2)
    aSegment2=Part.LineSegment(aPnt4, aPnt5)

    aEdge1=aSegment1.toShape()
    aEdge2=aArcOfCircle.toShape()
    aEdge3=aSegment2.toShape()
    aWire=Part.Wire([aEdge1, aEdge2, aEdge3])

    aSegment6 = Part.LineSegment(aPnt2, aPnt4)
    aEdge6=aSegment6.toShape()
    aWire6 = Part.Wire([aEdge2, aEdge6])
    aFace=Part.Face(aWire6)
    aFace.translate(App.Vector(0, d2, 0))
    ruf2 = aFace.extrude(App.Vector(0, w2 - d2, 0))

    ruf = aWire
    ruf = make_offset(doc, ruf, 0.1, "ruf1", True)
    ruf = ruf.extrude(App.Vector(0, w2, 0))
    ruf = make_offset(doc, ruf, 0.4, "ruf2")
    box = Part.makeBox(w + 2*d2, w2 - d2, h, App.Vector(-w/2-d2, d2, 0))
    boxI = Part.makeBox(w + 2*d2-d*2, w2, h-d, App.Vector(-w/2-d2+d, d2+d, 0))
    box = box.cut(boxI)
    ruf = ruf.fuse(box)
    ruf = ruf.fuse(ruf2)
    ruf2.translate(App.Vector(0, d, -d2-d))
    ruf = ruf.cut(ruf2)
    #Arc
    ar1 = 3.9/2
    hr1 = 7.4
    arc1 = marc(ar1, hr1)
    arc1.rotate(App.Vector(0, 0, 0),App.Vector(0, 0, 1), -90)
    arc1.translate(App.Vector(0, d2+d, 0))
    ruf = ruf.cut(arc1)

    ar2 = 1.9/2
    hr2 = 3.9
    xr = 7
    arc2 = marc(ar2, hr2)
    arc2.rotate(App.Vector(0, 0, 0),App.Vector(0, 0, 1), -90)
    arc2.translate(App.Vector(0, d2+d, hr1+ar1 - hr2 - ar2))

    arc2.translate(App.Vector(-xr, 0, 0))
    ruf = ruf.cut(arc2)
    arc2.translate(App.Vector(xr*2, 0, 0))
    ruf = ruf.cut(arc2)

    ar3 = 1.7/2
    hr3 = 4
    arc3 = marc(ar3, hr3)
    arc3.rotate(App.Vector(0, 0, 0),App.Vector(0, 0, 1), -90)
    arc3.translate(App.Vector(0, d2+d, h))
    ruf = ruf.cut(arc3)

    ar4 = 1.4/2
    hr4 = 5.
    arc4 = marc(ar4, hr4, 40)
    arc4.translate(App.Vector(r0-d, 0, h22))


    ruf.translate(App.Vector(0, -w2-w/2, 0))
    
    res = Part.makeBox(w, w, h22-h, App.Vector(-w/2, -w/2, h))
    
    cy = Part.makeCylinder(r0, h3-h, App.Vector(0, 0, h))
    cyI = Part.makeCylinder(r0-d+0.1, h3+1)
    

    dl = math.sqrt(r*r - r0*r0)
    sp = Part.makeSphere(r)
    sp1 = Part.makeSphere(r-d)
    sp = sp.cut(sp1)
    mbox = Part.makeBox(100, 100, dl, App.Vector(-50, -50, 0))
    mbox2 = Part.makeBox(100, 100, 100, App.Vector(-50, -50, -100))
    sp = sp.cut(mbox)
    sp = sp.cut(mbox2)
    sp.translate(App.Vector(0, 0, h3-dl))
    cy = cy.fuse(sp)
    
    for i in range(4):
            ruf.rotate(App.Vector(0, 0, 0),App.Vector(0, 0, 1), 90)
            res = res.fuse(ruf)
            arc4.rotate(App.Vector(0, 0, 0),App.Vector(0, 0, 1), 90)
            cy = cy.cut(arc4)    
    
    res = res.fuse(cy)
    cy2 = Part.makeCylinder(r0+d2, 0.1, App.Vector(0, 0, h3))
    cy2 = make_offset(doc, cy2, 0.3, "cy2")

    res = res.fuse(cy2)
    res = res.cut(cyI)
    #res = make_offset(doc, res, -1, "res5")

    resf = doc.addObject("Part::Feature", "res")
    resf.Shape = res        
    doc.recompute()   
    Mesh.export([resf], "stl/kipr.stl")
    return res  

kipr()

