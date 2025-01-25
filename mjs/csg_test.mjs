import { ImplicitGeometry } from '../js/ImplicitGeometry.js';
import {SurfGeometry} from '../js/SurfGeometry.js';
import { CurveGeometry } from '../js/CurveGeometry.js';
import { MathCurve } from '../js/MathCurve2.js';
import * as MCF from '../js/mathcurve.js'
import * as THREE from 'three';
import { savegeom, edgeSplit } from '../js/nodeExport.mjs';
import { SUBTRACTION, ADDITION, DIFFERENCE, INTERSECTION, REVERSE_SUBTRACTION, Brush, Evaluator } from 'three-bvh-csg';
//https://github.com/gkjohnson/three-bvh-csg?tab=readme-ov-file
//const geom1 = new ImplicitGeometry(MCF.isf, -2, 2, -2, 2, -2, 2, 100)
//const geom1 = new SurfGeometry(MCF.sine, 0, 2 * Math.PI, 0, 2 * Math.PI, 100, 100)
//const geom1 = new CurveGeometry(MCF.trefoil, 0, 2 * Math.PI, 0.65, 200, 50)
const geom1 = new THREE.SphereGeometry(3, 100, 100)



//const geom2 = new SurfGeometry(MCF.romanp, 0, Math.PI, 0, Math.PI, 100, 100)
//const geom2 = new SurfGeometry(MCF.klein, 2 * Math.PI, 0, 0, 2 * Math.PI, 100, 100)
//const geom2 = new THREE.SphereGeometry(3, 100, 100)
//const geom2 = new CurveGeometry(MCF.circ, 0,  2 * Math.PI, 1., 100, 100)
//const geom2 = new ImplicitGeometry(MathCurve.chair, -2, 2, -2, 2, -2, 2, 100)
const geom2 = new SurfGeometry(MathCurve.hyperboloid, 0, 2 * Math.PI,  -2,  2,  200,  100)

//savegeom(geom2, "./stl/chair.stl");


const brush1 = new Brush( geom1 );
brush1.updateMatrixWorld();

const brush2 = new Brush( geom2 );
brush2.updateMatrixWorld();

const evaluator = new Evaluator();
const result = evaluator.evaluate( brush1, brush2, INTERSECTION);



savegeom(result.geometry, "./stl/csg.stl");
//savegeom(result.geometry, "./obj/csg.obj");

console.log("ok");
