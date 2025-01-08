$fn = 100;
//$fa = 1;
//$fs = 0.1;
module angle(hc, rc) {
        cylinder(h=hc, r = rc);
        rotate([90, 0, 0])
        cylinder(h=hc, r = rc);
        sphere(r = rc); 
    }
    
/*
hc = 2;
rc = 1;    
th = 0.3;
*/
hc = 6;
rc = 3;
th = 0.9;    
difference(){
    angle(hc, rc);
    angle(hc+th, rc-th);
}
    