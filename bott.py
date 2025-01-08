import FreeCAD as App
import Part, math



def testRev():
    points = [(1, 0, 0), (5, 0, 0), (5, 0, 1), (3, 0, 1), (2, 0, 4), (1, 0, 4), (1, 0, 0)]
    b = Part.makePolygon(points)
    doc = App.newDocument()
    shapeobj = doc.addObject("Part::Feature", "MyShape")
    shapeobj.Shape = b
    doc.addObject("Part::Revolution","Revolve")
    doc.Revolve.Source = shapeobj
    doc.Revolve.Axis = (0,0,1)
    doc.Revolve.Base = (0, 0, 0)
    doc.Revolve.Angle = 270
    doc.Revolve.Solid = True
    doc.Revolve.AxisLink = None
    doc.Revolve.Symmetric = False
      
    doc.addObject("Part::Fillet","Fillet")
    doc.Fillet.Base = doc.Revolve
    __fillets__ = []
    __fillets__.append((1, 0.3, 0.3))
    __fillets__.append((14, 0.2, 0.2))
    doc.Fillet.Edges = __fillets__
    doc.MyShape.Visibility = False
    doc.Revolve.Visibility = False
    doc.recompute()
    return doc.Fillet.Shape 

def makeBottleTut(myWidth = 10.0, myHeight = 10.0, myThickness = 3.0):
    aPnt1=App.Vector(-myWidth / 2., 0, 0)
    aPnt2=App.Vector(-myWidth / 2., -myThickness / 4., 0)
    aPnt3=App.Vector(0, -myThickness / 2., 0)
    aPnt4=App.Vector(myWidth / 2., -myThickness / 4., 0)
    aPnt5=App.Vector(myWidth / 2., 0, 0)

    aArcOfCircle = Part.Arc(aPnt2, aPnt3, aPnt4)
    aSegment1=Part.LineSegment(aPnt1, aPnt2)
    aSegment2=Part.LineSegment(aPnt4, aPnt5)

    aEdge1=aSegment1.toShape()
    aEdge2=aArcOfCircle.toShape()
    aEdge3=aSegment2.toShape()
    aWire=Part.Wire([aEdge1, aEdge2, aEdge3])
    
    aTrsf=App.Matrix()
    aTrsf.rotateZ(math.pi) # rotate around the z-axis

    aMirroredWire=aWire.copy()
    aMirroredWire.transformShape(aTrsf)
    myWireProfile=Part.Wire([aWire, aMirroredWire])

        

    myFaceProfile=Part.Face(myWireProfile)
    aPrismVec=App.Vector(0, 0, myHeight)
    myBody=myFaceProfile.extrude(aPrismVec)
    myBody=myBody.makeFillet(myThickness / 12.0, myBody.Edges)
    #myBody=myBody.makeFillet(myThickness / 12.0, [myBody.Edges[0]])


    neckLocation=App.Vector(0, 0, myHeight)
    neckNormal=App.Vector(0, 0, 1)

    myNeckRadius = myThickness / 4.
    myNeckHeight = myHeight / 10.
    myNeck = Part.makeCylinder(myNeckRadius, myNeckHeight, neckLocation, neckNormal)
    myBody = myBody.fuse(myNeck)

    return myBody

#el = makeBottleTut()
#el.exportStl("stl/bott.stl")
el = testRev()
el.exportStl("stl/testrev.stl")


#print(el)