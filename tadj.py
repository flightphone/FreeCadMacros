import FreeCAD as App
import Part
import math
import Mesh

from CADUtils import  make_revolve, make_offset
baseh = 0.532
basew0 = 0.98
basew1 = 0.234

def shpil(bash):
    
    h1 = 0.035
    h2 = 0.030
    h3 = 0.025
    r1 = 0.015
    r2 = 0.013

    r3 = 0.007
    h_3 = 0.045

    c1 = math.sqrt(h_3*h_3 - r3*r3)
    cosa = c1/h_3
    sina = r3/h_3
    hcon = c1 * cosa
    rcon = c1 *sina
    h = h1 + h2 + h3 + h_3
    pcon = h - hcon

    r4 = 0.003
    res = Part.makeCylinder(r4, h1 + h2+ h3 + r3)
    sh0 = Part.makeSphere(r1)
    res = res.fuse(sh0)

    sh1 = Part.makeSphere(r1, App.Vector(0, 0, h1))
    res = res.fuse(sh1)
    
    sh2 = Part.makeSphere(r2, App.Vector(0, 0, h1 + h2))
    res = res.fuse(sh2)
    
    sh3 = Part.makeSphere(r3, App.Vector(0, 0, h1 + h2+ h3))
    res = res.fuse(sh3)

    con = Part.makeCone(rcon, 0, hcon, App.Vector(0, 0, pcon))
    res = res.fuse(con)

    k = bash/h
    myMat = App.Matrix()
    myMat.scale(k, k, k)
    res=res.transformGeometry(myMat)
    return res



def prism(r, h, n = 8):
    a = math.pi*2/n
    l = r*math.sin(a/2)*2
    points = [(r*math.cos(-a/2 + t*a), r*math.sin(-a/2 + t*a), 0) for t in range(n+1)]
    bot = Part.makePolygon(points)
    botw = Part.Wire(bot)
    botf = Part.Face(botw)
    pri=botf.extrude(App.Vector(0, 0, h))
    return pri


def tadj_minaret1(r, h):
    n = 8
    a = math.pi*2/n
    l = r*math.sin(a/2)*2 *0.6
    
    pri0 = prism(r, h)
    rs = r*math.cos(a/2)*0.98
    al = 53/180*math.pi
    sp = tadj_onion(rs, al)
    sp.translate(App.Vector(0, 0, h))
    pri0 = pri0.fuse(sp)
    
    sph = 0.1
    sh = shpil(sph)
    sh.translate(App.Vector(0, 0, h + rs/math.cos(math.pi/2 - al)))
    pri0 = pri0.fuse(sh)
    
    r1 = 0.85*r
    h1 = 0.75*h

    r2 = 0.97*r
    h2 = 0.25*h

    pri1 = prism(r1, h1)
    res = pri0.cut(pri1)

    
    
    boxm = Part.makeBox(10, l, h1, App.Vector(0, -l/2, 0))
    for _ in range(n):
        boxm.rotate(App.Vector(0, 0, 0),App.Vector(0, 0, 1), a*180/math.pi)
        res = res.cut(boxm)

    pri2 = prism(r2, h2)
    pri2 = pri2.cut(pri1)
    cy = Part.makeCylinder(l/2, 10, App.Vector(0, 0, 0), App.Vector(1, 0, 0), 360)
    for _ in range(n):
        cy.rotate(App.Vector(0, 0, 0),App.Vector(0, 0, 1), a*180/math.pi)
        pri2 = pri2.cut(cy)
    
    pri2.translate(App.Vector(0, 0, h*0.5))
    res = res.fuse(pri2)


    return res


def tadj_onion(r1, al):
    sp = Part.makeSphere(r1) 
    cn = Part.makeCone(r1*math.cos(al), 0, r1/math.cos(math.pi/2 - al) - r1*math.sin(al), App.Vector(0, 0, r1*math.sin(al)))
    res = sp.fuse(cn)
    return res




def tadj_cupol():
    
    h0 = 0.25
    w0 = 0.98
    w1 = 0.234
    rc = (w0 - 2*w1)/2*1.2
    r1 = rc*1.1
    dz = math.sqrt(r1*r1 - rc*rc)
    h1 = baseh + h0 + dz
    al = 53/180*math.pi
    #sp = Part.makeSphere(r1, App.Vector(0, 0, h1)) 
    sp = tadj_onion(r1, al)
    sp.translate(App.Vector(0, 0, h1))
    res = Part.makeCylinder(rc, h0, App.Vector(0, 0, baseh)) 
    res = res.fuse(sp)

    sph = 0.173
    sh = shpil(sph)
    sh.translate(App.Vector(0, 0, h1 + r1/math.cos(math.pi/2 - al)))
    res = res.fuse(sh)
    return res

def tadj_cyl(w1, h1):
    r1 = w1/2
    al = 67/180*math.pi
    res = Part.makeCylinder(r1, h1)
    sp = tadj_onion(r1, al)
    sp.translate(App.Vector(0, 0, h1))
    res = res.fuse(sp)
    return res

def tadj_face(boxw, fw0, fw1, r2):
    w1 = 0.315
    h1 = 0.306
    dx = fw0/2 -fw1/2

    w2 = 0.132
    h2 = 0.125
    pz = 0.248
    arc0 = tadj_cyl(w1, h1)
    w22 = 0.045
    arc0.translate(App.Vector(0, boxw/2 + w22/2, 0)) 
    
    arc1 = tadj_cyl(w2, h2)
    arc1.translate(App.Vector(dx, boxw/2, pz))
    arc2 = tadj_cyl(w2, h2)
    arc2.translate(App.Vector(dx, boxw/2, 0))

    arc3 = tadj_cyl(w2, h2)
    arc3.translate(App.Vector(-dx, boxw/2, pz))
    arc4 = tadj_cyl(w2, h2)
    arc4.translate(App.Vector(-dx, boxw/2, 0))


    arc5 = tadj_cyl(w2, h2)
    arc5.translate(App.Vector(0, r2, pz))
    arc5.rotate(App.Vector(0, 0, 0),App.Vector(0, 0, 1), 45)


    arc6 = tadj_cyl(w2, h2)
    arc6.translate(App.Vector(0, r2, 0))
    arc6.rotate(App.Vector(0, 0, 0),App.Vector(0, 0, 1), 45)
    
    arcs = [arc0, arc1, arc2, arc3, arc4, arc5, arc6]
    res = Part.makeCompound(arcs)
    return res


def tadj_minaret2(boxw):
    r = 0.085
    h = baseh + 0.25
    con = Part.makeCone(r, r/1.5, h, App.Vector(boxw - r*1.1, boxw - r*1.1, 0))
    mi = tadj_minaret1(r/1.5, 0.095)
    mi.translate(App.Vector(boxw - r*1.1, boxw - r*1.1, h))
    con = con.fuse(mi)
    return con

def tadj_box(doc):
    w0 = basew0
    w1 = basew1
    w2 = 0.045
    h0 = baseh
    h1 = 0.029
    h2 = 0.647
    boxw = w0 + w1*math.sqrt(2)
    box = Part.makeBox(boxw, boxw, h0, App.Vector(-boxw/2, -boxw/2, 0))

    r1_2 = w0*w0/4 + boxw*boxw/4
    r2 = math.sqrt(r1_2 - w1*w1/4)
    boxm = Part.makeBox(w1, w1, h0, App.Vector(-w1/2, r2, 0))
    boxm.rotate(App.Vector(0, 0, 0),App.Vector(0, 0, 1), 45)

    wp = w0 - 2*w1
    boxp = Part.makeBox(wp, w2, h2, App.Vector(-wp/2, boxw/2 -  w2/2, 0))        
    tfase = tadj_face(boxw, w0, w1, r2)

    for _ in range(4):
        boxm.rotate(App.Vector(0, 0, 0),App.Vector(0, 0, 1), 90)
        box = box.cut(boxm)

    box2 = make_offset(doc, box, -w2/2, "box")
    box2 = Part.makeCompound([box2])
    box2.translate(App.Vector(0, 0, h0 - w2/2 - h1))    
    box = box.cut(box2)

    for _ in range(4):    
        boxp.rotate(App.Vector(0, 0, 0),App.Vector(0, 0, 1), 90)
        box = box.fuse(boxp)
    for _ in range(4):        
        tfase.rotate(App.Vector(0, 0, 0),App.Vector(0, 0, 1), 90)
        box = box.cut(tfase)
    
    boxbot = Part.makeBox(boxw*2, boxw*2, h0/4, App.Vector(-boxw, -boxw, -h0/4))
    box = box.fuse(boxbot)
    mi2 = tadj_minaret2(boxw)
    for _ in range(4):    
        mi2.rotate(App.Vector(0, 0, 0),App.Vector(0, 0, 1), 90)
        box = box.fuse(mi2)

    return box    

def tadj():
    doc = App.newDocument()
    h1 = 0.029

    box = tadj_box(doc)
    cupol = tadj_cupol()
    cupol.translate(App.Vector(0, 0, -h1))
    res = box.fuse(cupol)
    boxw = (basew0 + basew1*math.sqrt(2))*1.2
    rm = 0.14
    hm = 0.2
    m1 = tadj_minaret1(rm, hm)
    m1.translate(App.Vector(boxw/4, boxw/4, baseh))

    m1.translate(App.Vector(0, 0, -h1))
    res = res.fuse(m1)

    
    m1.translate(App.Vector(0, -boxw/2, 0))
    res = res.fuse(m1)

    
    m1.translate(App.Vector(-boxw/2, 0, 0))
    res = res.fuse(m1)

    
    m1.translate(App.Vector(0, boxw/2, 0))
    res = res.fuse(m1)

    #res = shpil(1)
    
    resf = doc.addObject("Part::Feature", "res")
    resf.Shape = res
    Mesh.export([resf], "stl/tadj.stl")
    return res
    #https://elima.ru/articles/?id=86

tadj()
print("ok")
#print(90 - 22.5)