import { ImplicitGeometry } from '../js/ImplicitGeometry.js';
import { SurfGeometry } from '../js/SurfGeometry.js';
import { NormalUtils } from '../js/NormalUtils.js';
import { CurveGeometry } from '../js/CurveGeometry.js';
import { MathCurve } from '../js/MathCurve2.js';
import * as MCF from '../js/mathcurve.js'
import * as THREE from 'three';
import { savegeom, edgeSplit } from '../js/nodeExport.mjs';
import { SUBTRACTION, ADDITION, DIFFERENCE, INTERSECTION, REVERSE_SUBTRACTION, Brush, Evaluator } from 'three-bvh-csg';
//https://github.com/gkjohnson/three-bvh-csg?tab=readme-ov-file
function offsets(fun = (u, v) => {
    return THREE.Vector3(0, 0, 0);
}, u = 0, v = 0, width = 0.1) {
    let result = fun(u, v);
    let norm = NormalUtils.surf_normal(fun, u, v);
    norm.multiplyScalar(width);
    result.add(norm)
    return result;
}
function hyper(u, v) {
    return offsets(MathCurve.hyperboloid, u, v, 0.2)
}

const geom1 = new SurfGeometry(MathCurve.hyperboloid, 0, 2 * Math.PI, -2, 2, 100, 100)
//const geom2 = new SurfGeometry(hyper, 0, 2 * Math.PI, 2, -2, 100, 100);
let geom2 = new SurfGeometry(MathCurve.hyperboloid, 0, 2 * Math.PI, 2, -2, 100, 100)
geom2 = NormalUtils.make_offset(geom2, 0.1);
const geom3 = NormalUtils.addGeom([geom1, geom2]);
//savegeom(geom1, "./stl/hyper_width1.stl");
//savegeom(geom2, "./stl/hyper_width2.stl");


const geom4 = new THREE.BoxGeometry(3.5, 3.5, 3.5, 100, 100, 100);



const brush1 = new Brush(geom1);
brush1.updateMatrixWorld();

const brush2 = new Brush(geom2);
brush2.updateMatrixWorld();

const brush3 = new Brush(geom3);
brush3.updateMatrixWorld();

const brush4 = new Brush(geom4);
brush4.updateMatrixWorld();

const evaluator1 = new Evaluator();
const result = evaluator1.evaluate(brush3, brush4, INTERSECTION);
/*
const h1 = evaluator1.evaluate( brush1, brush3, INTERSECTION);
h1.updateMatrixWorld();

const evaluator2 = new Evaluator();
const h2 = evaluator2.evaluate( brush2, brush3, INTERSECTION);
h2.updateMatrixWorld();

const evaluator3 = new Evaluator();
const result = evaluator3.evaluate( h2, h1, SUBTRACTION);
*/

savegeom(result.geometry, "./public/stl/render.stl");


console.log("ok");
