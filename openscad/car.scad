//$fa = 1;
//$fs = 0.4;
// Car body base
base_height = 10;
top_height = 10;
trak = 20;
rotate([0, 0, 5])
{
cube([60,20,base_height],center=true);
// Car body top
translate([5,0,(base_height + top_height)/2 - 0.001])
    cube([30,20,top_height],center=true);
// Front left wheel
translate([-20,-trak,0])
    rotate([90,0,15])
    cylinder(h=3,r=8,center=true);
// Front right wheel
translate([-20,trak,0])
    rotate([90,0,15])
    cylinder(h=3,r=8,center=true);
// Rear left wheel
translate([20,-15,0])
    rotate([90,0,0])
    cylinder(h=3,r=8,center=true);
// Rear right wheel
translate([20,15,0])
    rotate([90,0,0])
    cylinder(h=3,r=8,center=true);
// Front axle
translate([-20,0,0])
    rotate([90,0,0])
    cylinder(h=2*trak,r=2,center=true);
// Rear axle
translate([20,0,0])
    rotate([90,0,0])
    cylinder(h=30,r=2,center=true);
}