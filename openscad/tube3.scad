$fn=100;
union() {
import("tube.stl", convexity=3);
cylinder(h=1.2, r1=1.75, r2 = 0.8);
cylinder(h=2.2, r1=0.8, r2 = 0.8);
}