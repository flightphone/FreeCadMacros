import FreeCAD as App
import Part
import math
import Mesh



def angle(rc, hc):
	cyl1 = Part.makeCylinder(rc, hc)
	cyl2 = Part.makeCylinder(rc, hc)
	myMat = App.Matrix()
	myMat.rotateX(math.pi/2)
	cyl2.transformShape(myMat)
	sphere = Part.makeSphere(rc)
	res = cyl1.fuse(sphere)
	res = res.fuse(cyl2)
	return res

hc = 6
rc = 3
th = 1.5
o1 = angle(rc, hc)
o2 = angle(rc-th, hc+th)
res = o1.cut(o2)
res = res.makeFillet(0.5, res.Edges)
doc = App.newDocument()
resf = doc.addObject("Part::Feature", "res")
resf.Shape = res        
doc.recompute()   
Mesh.export([resf], "stl/angle.stl")

#Part.show(res)
