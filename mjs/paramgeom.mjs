import { ImplicitGeometry } from '../js/ImplicitGeometry.js';
import {SurfGeometry} from '../js/SurfGeometry.js'
import { MathCurve } from '../js/MathCurve2.js';
import * as MCF from '../js/mathcurve.js'
import * as THREE from 'three';
import { savegeom, edgeSplit } from '../js/nodeExport.mjs';

/*
const geom = new ImplicitGeometry(MCF.gayley, -3, 3, -3, 3, -3, 3);
savegeom(geom, "./obj/garley2.obj");
console.log("ok");
*/
/*
const r = 10;
const geom = new SurfGeometry((u, v)=> {
    const x = r*Math.cos(u);
    const y = r*Math.sin(u);
    const z = v;
    return new THREE.Vector3(y, z, x);
}, 0, 2*Math.PI, r*3, 0, 50, 2);
savegeom(geom, "./obj/cyl4.stl");
*/
//const geom = new ImplicitGeometry(MCF.sphere,  -2,   2,   -2,   2,   -2,   2,  100,  10);
//savegeom(geom, "./obj/sphere111a.obj");
// 
const geom = new SurfGeometry(MCF.boys, 0, Math.PI,  0,  Math.PI, 100, 100);
savegeom(geom, "./public/stl/render.stl");

//const geom = new ImplicitGeometry(MathCurve.chair, -2, 2, -2, 2, -2, 2, 100)
//savegeom(geom, "./obj/chair.obj");
console.log("ok");

//edgeSplit("./stl/kipr.stl", "./obj/kipr10.obj");