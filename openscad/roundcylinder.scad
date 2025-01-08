//$fa = 1;
//$fs = 0.4;
$fn=100;


module tor(R, r)
{
    rotate([0, 0, 90])
    rotate_extrude()
    translate([R-r, 0, 0])
        circle(r); 
              
}


module rcyl(h, R, r)
{
    difference()
    {
    union() {
    cylinder(h = h, r = R, center = true);
    cylinder(h+2*r, r = R-r, center=true);
    translate([0, 0, h/2])
    tor(R, r);
    
    translate([0, 0, -h/2])
    tor(R, r);
    }    
        cylinder(h = h+10, r = R/3, center = true);
    translate([0, 0, h/2+r])    
    cylinder(h = 2*r, r = R/3+r, center = true);
    translate([0, 0, -h/2-r])    
    cylinder(h = 2*r, r = R/3+r, center = true);
    }
    translate([0, 0, h/2])
    tor(R/3+ 2*r, r); 
    translate([0, 0, -h/2])
    tor(R/3+ 2*r, r);     
}

h = 10;
R = 2;
r = 0.2;
difference(){
union(){
rcyl(h, R, r);
rotate([90, 0, 0])
rcyl(h, R, r);
rotate([0, 90, 0])
rcyl(h, R, r);
}  
cylinder(h=2*R+1, r = R/3, center = true);
rotate([90, 0, 0])
cylinder(h=2*R+1, r = R/3, center = true);
rotate([0, 90, 0])
cylinder(h=2*R+1, r = R/3, center = true);
}
