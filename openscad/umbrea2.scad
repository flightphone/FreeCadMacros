$fn=100;
n = 8;
a = 360/n;

module umbr()
{
    difference(){    
        hull() 
        {
            for (i=[1:n])
            {
                rotate([-a/2 + i*a, 90, 0])
                linear_extrude(height=0.01) 
                circle(r = 1);
            }    
        }
        translate([-1, -1, 0])
        cube([2, 2, 5]);
    }
}
difference(){ 
    umbr();
    translate([0, 0, 0.1])
    umbr();
}
translate([0, 0, -1.1])
cylinder(2.5, 0.05, 0.05);