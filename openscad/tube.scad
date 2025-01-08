$fn=100;
include <plot_function.scad>
h = 5;
r = 2;
function v1(u) = [r*cos(u), r*sin(u), h];
function v0(u) = [r*cos(u), 0, 0];
function v3(z, u) = (v1(u) - v0(u))*z/h +  v0(u);
function v4(z, u) = [0, 0, z] - v3(z, u);
function AxialFunc1(z, u) = sqrt(v4(z,u)*v4(z,u));

function AxialFunc2(z, u) = 0.2*(1.5+(sin(z*360)));
//cube();
PlotAxialFunction(2, [0, h/50 , h]);