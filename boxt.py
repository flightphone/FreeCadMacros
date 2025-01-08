import FreeCAD as App
import Part
import math

h = 10
w = 5
l = 4
t = 0.5
box1 = Part.makeBox(h, w, l)
box2 = Part.makeBox(h-t, w-t, l-t)
res = box1.cut(box2)
res.exportStl("stl/box.stl")