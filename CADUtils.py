
def make_revolve(doc, shape, name, angle = 360, axis = (0, 0, 1), base = (0, 0, 0)):
    shapeobj = doc.addObject("Part::Feature", name)
    shapeobj.Shape = shape
    shapeobj.Visibility = False
    Revolve = doc.addObject("Part::Revolution", name + "_revolve")
    Revolve.Source = shapeobj
    Revolve.Axis = axis
    Revolve.Base = base
    Revolve.Angle = angle
    Revolve.Solid = True
    Revolve.AxisLink = None
    Revolve.Symmetric = False
    Revolve.Visibility = False
    doc.recompute()
    return Revolve.Shape


def make_offset(doc, bott, th, name, D2 = False):
    bottf = doc.addObject("Part::Feature", name)
    bottf.Shape = bott
    bottf.Visibility = False
    Offset = doc.addObject("Part::Offset2D", name + "_Offset") if D2 else doc.addObject("Part::Offset", name + "_Offset")
    
    Offset.Source = bottf
    Offset.Value = th
    Offset.Mode = "Pipe" if D2 else "Skin"
    Offset.Join = 0
    Offset.Intersection = True
    Offset.SelfIntersection = D2
    Offset.Fill = D2
    Offset.Visibility = False

    doc.recompute()
    return Offset.Shape