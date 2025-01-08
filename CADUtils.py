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