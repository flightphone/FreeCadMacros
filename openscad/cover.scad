$fn = 100;


module tor(R, r)
{
    
    rotate([0, 0, 90])
    rotate_extrude()
    translate([R-r, 0, 0])
        circle(r, $fn = 10);   
}


module rcyl(h, R, r)
{
    
    cylinder(h = h, r = R, center = true);
    translate([0, 0, h/2])
    cylinder(2*r, r = R-r, center=true);
    translate([0, 0, h/2])
    tor(R, r);
    
    
}

r = 5;
h = 2;
r2 = 0.3;
n = 100;
w = 0.2;

difference(){
color(c=[0, 1, 0], alpha = 1.0)    
rcyl(h, r, r2);
color(c=[1, 1, 0], alpha = 1.0)
translate([0, 0, -0.5])    
rcyl(h, r-0.5, r2); 
for (i=[0:n-1])
{   
color(c=[0, 1, 0], alpha = 1.0)    
rotate([0, 0, i*360/n])
translate([r+0.4, 0, 0.1])  
cube([1, w, h], center=true);
}
}
