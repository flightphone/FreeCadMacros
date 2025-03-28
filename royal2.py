import FreeCAD as App
import Part
import math
import Mesh

from CADUtils import make_offset

def royal():
    body = [(73.6, 48.6), (55.2, 78), (17, 75.8), (0, 50.4)]
    spout = [(14.5, 37.6, 90, 26.), (15.1, 36.0, 90, 38.8), (52.3, 12.7, 34.2, 57.6), (61.6, 9.6, 34.2, 64.2), (70, 15.9, 16.1, 75.3)]
    th = -4
    loft = []
    loftsp = []
    doc = App.newDocument()
    for v in body:
        c = Part.makeCircle(v[1]/2, App.Vector(0, 0, v[0]))
        loft.append(c)
    
    botf = None
    topf = None

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
        if (i == len(spout)-1):
            botf = Part.makeBox(100, 100, 100)
            botf.translate(App.Vector(-50, -50, -4))
            botf.transformShape(mat2)

        
        
    spoutt = Part.makeLoft(loftsp, True, False)
    spoutt1 = make_offset(doc, spoutt, -0.7, "spoutt")
    spoutt2 = make_offset(doc, spoutt1, -0.7, "spoutt1")
    
    
    
        
   
    bott = Part.makeLoft(loft, True, False)
    bott1 = make_offset(doc, bott, th/2, "bott")
    bott2 = make_offset(doc, bott, th, "bott1")
    
    tor1 = Part.makeTorus(body[0][1]/2, 2, App.Vector(0, 0, body[0][0]))
    tor2 = Part.makeTorus(25, 4, App.Vector(-35, 0, 40), App.Vector(0, 1, 0))

    #bott = bott.fuse(spoutt)
    bott = bott.fuse(tor1)
    #bott = bott.fuse(tor2)

    bott = bott.cut(bott1)
    bott = bott.cut(spoutt1)
    
    spoutt = spoutt.cut(bott1)
    spoutt = spoutt.cut(spoutt1)
    spoutt = spoutt.cut(botf)

    tor2 = tor2.cut(bott1)

    doc.recompute()


    bottI = bott1.cut(bott2)
    bottI = bottI.cut(spoutt2)
    
    spouttI = spoutt1.cut(bott2)
    spouttI = spouttI.cut(spoutt2)
    spouttI = spouttI.cut(botf)
    
    
    
    cy3 = Part.makeCylinder(body[0][1]/2 + th, 50, App.Vector(0, 0, body[0][0]-25), App.Vector(0, 0, 1), 360)
    bott = bott.cut(cy3)
    bottI = bottI.cut(cy3)
    
    inner =  bottI.fuse(spouttI)

    '''
    fi = [13, 19, 21, 25, 31]
    fil = [res.Edges[i-1] for i in fi]
    res = res.makeFillet(1, fil)
    '''
    sps = [bott, spoutt, tor2, inner]
    names = ["bott_res", "spoutt_res", "tor2_res", "inner_res"]
    for i, e in zip(names, sps):
        rf = doc.addObject("Part::Feature", f"{i}")
        rf.Shape = e
        doc.recompute()
        Mesh.export([rf], f"stl/royal/{i}.stl") 

    res = Part.makeCompound(sps)
    resf = doc.addObject("Part::Feature", "res")
    resf.Shape = res        
    doc.recompute()   
    Mesh.export([resf], "public/stl/render.stl")
    return res     

r = royal()    
#r.exportStl("stl/royal2.stl")
print("ok")