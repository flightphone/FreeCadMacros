
translate([-5, -10, 0])
{
cube([10,20,0.2]);
cube([0.2, 20, 2.5]);
translate([10-0.2, 0, 0])
    cube([0.2, 20, 2.5]);
cube([10, 0.2, 2.5]);
translate([0, 20, 0])
cube([10, 0.2, 2.5]);  
}