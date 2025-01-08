use <simple_wheel.scad>
//$fa = 1;
//$fs = 0.8;
//$fn = 15;
base_height = 10; 
top_height = 14; 
track = 35; 
body_roll = 0; 
wheels_turn = 0; 
rotate([body_roll,0,0]) {
    // Car body base
    cube([60,20,base_height],center=true);
    // Car body top
    translate([5,0,base_height/2+top_height/2 - 0.001])
        cube([30,20,top_height],center=true); 
} 
// Front left wheel 
translate([-20,-track/2,0])
    rotate([0,0,wheels_turn])
    wheel(wheel_radius=10, side_spheres_radius=50, hub_thickness=4, cylinder_radius=2);
 // Front right wheel 
translate([-20,track/2,0])
    rotate([0,0,wheels_turn])
    wheel(wheel_radius=10, side_spheres_radius=50, hub_thickness=4, cylinder_radius=2);
// Rear left wheel 
translate([20,-track/2,0])
    rotate([0,0,0])
    wheel(wheel_radius=10, side_spheres_radius=50, hub_thickness=4, cylinder_radius=2);
// Rear right wheel 
translate([20,track/2,0])
    rotate([0,0,0])
    wheel(wheel_radius=10, side_spheres_radius=50, hub_thickness=4, cylinder_radius=2);
// Front axle 
translate([-20,0,0])
    rotate([90,0,0])
    cylinder(h=track,r=2,center=true); 
// Rear axle 
translate([20,0,0])
    rotate([90,0,0])
    cylinder(h=track,r=2,center=true);