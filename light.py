import FreeCAD as App
import Part
import math
import Mesh


from CADUtils import make_bolt, make_offset


def helix():
    doc = App.newDocument()
    pitch = 3
    height = pitch * 8
    radius = 10
    geoms = [Part.LineSegment(App.Vector(radius, pitch/3, 0),App.Vector(radius+1, 0, 0)), 
             Part.LineSegment(App.Vector(radius+1, 0 ,0),App.Vector(radius, -pitch/3, 0)), 
             Part.LineSegment(App.Vector(radius, -pitch/3 ,0),App.Vector(radius, pitch/3, 0))]
    
    #geoms = [Part.Circle(App.Vector(radius, 0, 0),App.Vector(0, 0, 1),pitch/2)]
    swe = make_bolt(doc, pitch+0.1, height, radius, geoms, "bolt")
    cy = Part.makeCylinder(radius, height)
    res = Part.makeCompound([swe.Shape, cy])
    #res = cy
    bx = Part.makeBox(50, 50, 100, App.Vector(-25, -25, height - 2*pitch))
    res = res.cut(bx)
    #bx.translate(App.Vector(0, 0, 100 + 12))
    #res = res.cut(bx)
    resf = doc.addObject("Part::Feature", "res")
    resf.Shape = res        
    doc.recompute()   
    Mesh.export([resf], "stl/helix3.stl")
    

def light():
    doc = App.newDocument()
    d0 = 1.35
    h0 = 0.95
    w = 0.2
    d1 = 3

    d0 += 2*w
    h0 += w
    d1 += 2*w

    alf = math.atan2(d1, d0)
    alf = 2*alf - math.pi /2
    r2 = d0/2 + d0/2*math.sin(alf)
    h2 = d0/2*math.cos(alf)
    
    
    d3 = 1.34
    h3 = 0.89
    w3 = 0.05
    

    d4 = 0.91
    h4 = 0.22
    
    r5 = 0.4
    d5 = 0.7
    c5 = math.sqrt(r5*r5 - d5*d5/4) - h3-h4 - w3

    cy1 = Part.makeCylinder(d0/2, h0)
    sp1 = Part.makeSphere(d1/2, App.Vector(0, 0, h0 + d1/2))
    
    
    cn1 = Part.makeCone(d0/2, r2, h2, App.Vector(0, 0, h0))
    glass = cy1.fuse(cn1)
    glass = glass.fuse(sp1)
    glass = glass.makeFillet(w, glass.Edges)
    #glass = make_offset(doc, glass, -w, "glass")
    
    base = Part.makeCylinder(d3/2, h3, App.Vector(0, 0, -h3))
    cn2 = Part.makeCone(d4/2, d3/2, h4, App.Vector(0, 0, -h3-h4))
    base = base.fuse(cn2)
    base = make_offset(doc, base, w3, "basetmp")
    #bolt
    pitch = h3/4
    height = pitch*7
    radius = d3/2
    wb = 0.2
    nn = 2
    geoms = [Part.LineSegment(App.Vector(radius, pitch/nn, 0),App.Vector(radius+wb, 0, 0)), 
             Part.LineSegment(App.Vector(radius+wb, 0 ,0),App.Vector(radius, -pitch/nn, 0)), 
             Part.LineSegment(App.Vector(radius, -pitch/nn ,0),App.Vector(radius, pitch/nn, 0))]
    
    #geoms = [Part.Circle(App.Vector(radius, 0, 0),App.Vector(0, 0, 1),pitch/2)]
    swe = make_bolt(doc, pitch, height, radius, geoms, "bolt")
    #cy = Part.makeCylinder(radius, height)
    bolt = Part.makeCompound([swe.Shape])
    #bolt = bolt.makeFillet(0.01, bolt.Edges)
    bx1 = Part.makeBox(10, 10, 10, App.Vector(-5, -5, -10 + 2*pitch))
    bolt = bolt.cut(bx1)
    bx2 = Part.makeBox(10, 10, 10, App.Vector(-5, -5, height - 2*pitch))
    bolt = bolt.cut(bx2)

    bolt.translate(App.Vector(0, 0, -h3-2*pitch))
    base = Part.makeCompound([base, bolt])
    #base = bolt


    
    #base = glass.makeFillet(w3, base.Edges)
    base2 = Part.makeSphere(r5, App.Vector(0, 0, c5))


    sps = [glass, base,  base2]
    names = ["glass", "base",  "base2"]
    for i, e in zip(names, sps):
        rf = doc.addObject("Part::Feature", f"{i}")
        rf.Shape = e
        doc.recompute()
        Mesh.export([rf], f"stl/light/{i}.stl") 

    res = Part.makeCompound(sps)
    resf = doc.addObject("Part::Feature", "res")
    resf.Shape = res        
    doc.recompute()   
    Mesh.export([resf], "stl/light.stl")

	
	

light()
print("ok")

