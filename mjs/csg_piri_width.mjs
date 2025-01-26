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

function piri() {
    const geom1 = new ImplicitGeometry(MathCurve.piri, -2, 2, -2, 2, -2, 2, 100);
    const geom2 = NormalUtils.make_offset(geom1, 0.05);
    const geom4 = new THREE.SphereGeometry(0.5, 100, 100);

    const brush1 = new Brush(geom1);
    brush1.updateMatrixWorld();

    const brush2 = new Brush(geom2);
    brush2.updateMatrixWorld();


    const evaluator = new Evaluator();
    const brush3 = evaluator.evaluate(brush2, brush1, SUBTRACTION);
    brush3.updateMatrixWorld();

    const brush4 = new Brush(geom4);
    brush4.updateMatrixWorld();

    const result = evaluator.evaluate(brush3, brush4, SUBTRACTION);

    savegeom(result.geometry, "./stl/piri.stl");
    savegeom(result.geometry, "./obj/piri.obj");

    console.log("ok");
}

function eggbox()
{
    
    let geom2 = new SurfGeometry(MCF.egg_box1, 8,  -8,  -8, 8,  200,  200);
    const geom4 = new THREE.BoxGeometry(6, 6, 4, 100, 100, 100)
    
    
    const brush2 = new Brush(geom2);
    brush2.updateMatrixWorld();

    const brush4 = new Brush(geom4);
    brush4.updateMatrixWorld();


    const evaluator = new Evaluator();
    const result = evaluator.evaluate(brush2, brush4, INTERSECTION);
    savegeom(result.geometry, "./stl/eggbox.stl");
    savegeom(result.geometry, "./obj/eggbox.obj");
    console.log("egg");

}

//piri();
eggbox();