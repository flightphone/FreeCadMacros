$fn=100;
n = 8;
a = 360/n;
module prisma(n, r, h)
{
    a = 360/n;
    points = [for (t = [1:n])[r*cos(-a/2 + t*a), r*sin(-a/2 + t*a)]];
    linear_extrude(height=h)        
    polygon(points);        
}

hull() 
{
    for (i=[1:n])
    {
        rotate([-a/2 + i*a, 90, 0])
        linear_extrude(height=0.01) 
        circle(r = 1);
    }    
}

prisma(n, 0.8, 2);