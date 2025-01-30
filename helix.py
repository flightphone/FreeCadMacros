import FreeCAD as App
import Part
import math
import Mesh


from CADUtils import make_bolt


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
    

def helix_old():
    doc = App.newDocument()
    hepart = doc.addObject("Part::Helix",f"Helix")
    hepart.Pitch= 3
    hepart.Height= 15
    hepart.Radius= 10
    hepart.Angle= 0
    hepart.LocalCoord=0
    hepart.Style=1
    
    sk = doc.addObject('Sketcher::SketchObject', 'Sketch')
    sk.Placement = App.Placement(App.Vector(0.000000, 0.000000, 0.000000), App.Rotation(0.707107, 0.000000, 0.000000, 0.707107))
    geoms = [Part.LineSegment(App.Vector(10, 1, 0),App.Vector(11, 0, 0)), Part.LineSegment(App.Vector(11, 0 ,0),App.Vector(10, -1, 0)), Part.LineSegment(App.Vector(10, -1 ,0),App.Vector(10, 1, 0))]
    
    for ge in geoms:
        sk.addGeometry(ge, False)
    '''
    sk.addGeometry(Part.LineSegment(App.Vector(10, 1, 0),App.Vector(11, 0, 0)),False)
    sk.addGeometry(Part.LineSegment(App.Vector(11, 0 ,0),App.Vector(10, -1, 0)),False)
    sk.addGeometry(Part.LineSegment(App.Vector(10, -1 ,0),App.Vector(10, 1, 0)),False)
    '''

    swe = doc.addObject('Part::Sweep','Sweep')
    swe.Sections=[sk]
    
    swe.Spine=(hepart, ['Edge1',])
    swe.Solid=True
    swe.Frenet=True
    doc.recompute()
    Mesh.export([swe], "stl/helix.stl")

	
	
	
	
	
	
	

helix()
print("ok")

