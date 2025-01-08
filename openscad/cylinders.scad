$fn = 100;
r1 = 2;
r2 = 0.7;
difference(){
union(){
cylinder(h=10, r = r1, center = true);
rotate([90, 0, 0])
cylinder(h=10, r = r1, center = true);
rotate([0, 90, 0])
cylinder(h=10, r = r1, center = true);
}    
cylinder(h=15, r = r2, center = true);
rotate([90, 0, 0])
cylinder(h=15, r = r2, center = true);
rotate([0, 90, 0])
cylinder(h=15, r = r2, center = true);
}