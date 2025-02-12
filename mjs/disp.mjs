import { ImplicitGeometry } from '../js/ImplicitGeometry.js';
import { CurveGeometry } from '../js/CurveGeometry.js'
import { SurfGeometry } from '../js/SurfGeometry.js';
import { MathCurve } from '../js/MathCurve2.js';
import * as MCF from '../js/mathcurve.js'
import * as THREE from 'three';
import { savegeom, edgeSplit } from '../js/nodeExport.mjs';
import {
    abs, sign, sin, cos, atan, sqrt, floor, vec3, vec2, clamp, length, dot, dot2, cross,
    mod, vec3s, vec3m, rotz, max, min, pxy, mix, smin, smin_out, PI, TAU, vec3a
} from '../js/CommonGLSL.js'
import { NormalUtils } from '../js/NormalUtils.js';
import * as BufferGeometryUtils from 'three/examples/jsm/utils/BufferGeometryUtils.js';

let charge = [];
const n = 5;
const r = 4
function render(time) {
    //time *= 2;
    charge = [];
    for (let i = 0; i < n; i++) {
        let x = Math.sin(i + 0.62 * time * (1.03 + 0.5 * Math.cos(1.51 * i)))*0.3;
        let y = (Math.cos(i + 1.17 * time * Math.cos(1.22 + 1.1424 * i)))*0.8; // dip into the floor //Math.abs
        let z = Math.cos(i + 0.51 * time * 0.1 * Math.sin((0.92 + 1.43 * i)))*0.3;
        charge.push({ x: r*x, y: r*y, z: r*z, q: 0.55 });
    }
}

function stoun() {
    const geom = new ImplicitGeometry((x, y, z) => {
        
            let res = 0;
            let v = new THREE.Vector3(x, y, z);
            charge.forEach((a) => {
                let d = v.distanceTo(new THREE.Vector3(a.x, a.y, a.z));
                res += a.q / d;
            });
            return 1.5 - res;
        
    },
     -r, r + 1,  -r - 1, r + 1,  -r - 1, r + 1, 30)
    return geom;
}
function sp()
{
    const geom = new SurfGeometry((u, v) => {
        let r = 1.1
        //r = r + 0.03*(Math.sin(30*(u+PI)*(v+PI)))
        r = r + 0.03*(Math.sin(35*u + 35*v))
        const z = r*cos(v)
        const r2 = r*sin(v)
        const x = r2*cos(u)
        const y = r2*sin(u)
        return new THREE.Vector3(x, y, z)
    }, 0, Math.PI*2, 0, Math.PI, 100, 100, 1)
    return geom
}

/*
let r = 1.1
    return (x * x + y * y + z * z - r*r + 0.06*(Math.sin(35*x)+Math.sin(20*y)+Math.sin(25*z)));
*/

//render(214);
const me = sp() 
savegeom(me, "./stl/sp.stl");

console.log("ok");

