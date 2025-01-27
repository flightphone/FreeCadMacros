import { ImplicitGeometry } from '../js/ImplicitGeometry.js';
import { CurveGeometry } from '../js/CurveGeometry.js'
import { SurfGeometry } from '../js/SurfGeometry.js';
import { MathCurve } from '../js/MathCurve2.js';
import * as MCF from '../js/mathcurve.js'
import * as THREE from 'three';
import { savegeom, edgeSplit } from '../js/nodeExport.mjs';


function garley() {
    const geom = new ImplicitGeometry(MCF.gayley, -3, 3, -3, 3, -3, 3);
    return geom;
}

function ch1() {
    const geom = new ImplicitGeometry((x, y, z) => {
        return x * x * x * x + y * y * y * y / 2 + z * z * z * z - y * y * y - x * x - z * z + x * x * z * z / 2 + x * x * y * y + y * y * z * z + 1 / 3.6
    }, -2, 2, -2, 2, -2, 2, 200)
    return geom;
}

function ch2() {
    const geom = new ImplicitGeometry((x, y, z) => {
        return x * x * x * x + y * y * y * y / 4 + z * z * z * z + x * x * z * z * 2 - 3 * y * (x * x + z * z) + 2 * y * y - 0.05
    },
        -2, 2, -2, 2, -2, 2, 100)
    return geom;
}
function larme() {
    let a = 1
    const geom = new CurveGeometry((t) => {
        let n = 1
        let x = a * Math.cos(t);
        let y = a * Math.sin(t)*Math.pow(Math.sin(t / 2), n)
        let z = 0
        return new THREE.Vector3(x, y, 0);
    },
     -Math.PI,  Math.PI,  0.05,  200,  40,  1,  2
    );
    return geom;
}

function shell()
{
    const geom = new SurfGeometry(MCF.shell, 0, 14 * Math.PI, 0, 2 * Math.PI, 1000,  100);
    return geom;
}
const geom = shell()
//const geom = ch1()
savegeom(geom, "./obj/shell25.obj");
savegeom(geom, "./stl/shell25.stl");
//savegeom(geom, "./obj/render.obj");
console.log("shell");

