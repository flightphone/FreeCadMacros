h = 15;
w = 4;
h1 = 10;
difference(){
cube([w, w, h], center=true);
for (i=[0:3])
{    
rotate([0, 0, 45 + 90*i])
translate([w/sqrt(2), 0, 0])   
rotate([0, -30, 0])
translate([h1/2, 0, h1/2])    
cube([h1, h1, 2*h1], center=true);
}
}
