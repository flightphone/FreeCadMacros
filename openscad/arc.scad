$fn = 100;

module prisma(n, r, h)
{
    a = 360/n;
    points = [for (t = [1:n])[r*cos(-a/2 + t*a), r*sin(-a/2 + t*a)]];
    linear_extrude(height=h)        
    polygon(points);        
}
module archinv(r, h, w)
{
    {
        cube([w, 2*r, h], center=true);
        translate([0, 0, h/2])
        rotate([0, 90, 0])
        cylinder(h=w, r = r, center=true);
    }
}

module arch(n, r1, h1, r2, h2)
{
    difference(){
        prisma(n, r1, h1);
        for (i=[0:n-1])
        {
            rotate([0, 0, i*360/n])
            archinv(r2, h2*2, r1*2);
        }
      }
}
module horse()
{
    translate([4, 0, 0])   
    rotate([0, -90, 0])
    rotate([0, 0, -45])
    difference(){
        cube([0.1, 0.1, 8]);
        cylinder(9, 0.1, 0.1, $fn=20);
    }
}

module ruf(w, h, l)
{
    points = [[0,-w], [0, w], [h, 0]];
   
    rotate([0, -90, 0])
    translate([0, 0, -l/2])
    linear_extrude(height=l)        
    polygon(points);        
}

module conus(n, h4, h2)
{
    cylinder(h = h4, r1 = h2, r2 = 0, center=true, $fn = 8);     
}

r1 = 2;
h = 3.5;
h2 = 0.9;
h3 = 0.5*h;
h4 = 2;


module rafover() {
rafpoints = [
             [-r1/sqrt(2), -r1/sqrt(2), h-0.1], 
             [-r1/sqrt(2), -h2 + 0.0414, h - 0.1], 
             [-r1/sqrt(2), 0, h + h2 - 0.1414], 
             [-r1/sqrt(2), h2 - 0.0414, h - 0.1],
             [-r1/sqrt(2), r1/sqrt(2), h-0.1],
             [r1/sqrt(2), r1/sqrt(2), h-0.1]
    ];
nr = 5;

for (i=[0:nr-2])
{
    hull(){
        translate(rafpoints[i])
        sphere(r = 0.1, $fn=20);
        translate(rafpoints[i+1])
        sphere(r = 0.1, $fn=20);
        }
}
}

translate([0, 0, -(h+h2+h3+h4)/2])
union()
{
    

color( c = [1., 0.1, 0.1], alpha = 1.0 ){    


for (i=[0:3])    
{    
    rotate([0, 0, i*90])
    rafover();    
}
    
    
arch(4, r1, h, 0.7, 2.);
}  
color( c = [0.9, 0.9, 0.1], alpha = 1.0 ){

difference(){
translate([0, 0, h])
ruf(h2, h2, r1*sqrt(2));
translate([0, 0, h2+h - 0.1*sqrt(2)])
horse();    
}
rotate([0, 0, 90])
difference(){
translate([0, 0, h])
ruf(h2, h2, r1*sqrt(2));
translate([0, 0, h2+h - 0.1*sqrt(2)])
horse();    
}

translate([0, 0, h+h2/2])
cube([2*h2, 2*h2, h2], center=true);
}
color( c = [0.1, 0.9, 0.1], alpha = 1.0 ){
rotate([0, 0, 360/16])
translate([0, 0, h+h2])
arch(8, h2, h3, 0.2, h3*0.7);
}    
color( c = [0.9, 0.9, 0.1], alpha = 1.0 ){
translate([0, 0, h+h2+h3+h4/4])
conus(8, h4/2, h2);
}    
}

