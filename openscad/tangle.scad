$fn = 100;
module tangle(hc, rc) {
        cylinder(h=2*hc, r = rc, center = true);
        rotate([90, 0, 0])
        cylinder(h=hc, r = rc);
    }

hc = 6;
rc = 3;
th = 0.9;    
difference(){
    tangle(hc, rc);
    tangle(hc+th, rc-th);
}   