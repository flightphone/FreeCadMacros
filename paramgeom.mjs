import { ImplicitGeometry } from './js/ImplicitGeometry.js';
import {SurfGeometry} from './js/SurfGeometry.js'
import { MathCurve } from './js/MathCurve2.js';
import * as MCF from './js/mathcurve.js'
import * as THREE from 'three';
import { savegeom, edgeSplit } from './js/nodeExport.mjs';

/*
const geom = new ImplicitGeometry(MCF.gayley, -3, 3, -3, 3, -3, 3);
savegeom(geom, "./obj/garley2.obj");
console.log("ok");
*/
const r = 10;
const geom = new SurfGeometry((u, v)=> {
    const x = r*Math.cos(u);
    const y = r*Math.sin(u);
    const z = v;
    return new THREE.Vector3(y, z, x);
}, 0, Math.PI/2, r*3, 0, 50, 2);
savegeom(geom, "./obj/cyl2.obj");
console.log("ok");

//edgeSplit("./stl/kipr.stl", "./obj/kipr10.obj");