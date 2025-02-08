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

function arc(u = 0, v = 0, R = 1, n = 5, i = 0) {

    let xl = R * Math.cos(v);
    let yl = R * Math.sin(v) * Math.sin(v / 2) * Math.sin(v / 2);
    yl = abs(yl);

    let twist = (Math.cos(v) + 1) / 4 * PI;

    R = yl;
    let al = Math.PI * 2 / n
    let r = R * sin(al / 2);
    let x = r * cos(u) + R * cos(al / 2);
    let y = r * sin(u);
    let z = xl * 0.9;
    let res = vec3(x, y, z);
    res = rotz(res, al * i + twist);
    return res;
}

function arc2(u = 0, v = 0, R = 1, n = 5, i = 0) {
    
    let p = PI/2 + 35/180*PI
    if (v > p)
    {
        R = R/Math.cos(v-p);
    }
    
    
    let xl = R * Math.cos(v);
    let yl = R * Math.sin(v);
    
    yl = abs(yl);

    let twist = (Math.cos(v) + 1) / 4 * PI;

    R = yl;
    let al = Math.PI * 2 / n
    let r = R * sin(al / 2);
    let x = r * cos(u) + R * cos(al / 2);
    let y = r * sin(u);
    let z = xl * 0.9;
    let res = vec3(x, y, z);
    res = rotz(res, al * i + twist);
    return res;
}

function ruf() {
    const geoms0 = []
    const geoms1 = []
    const n = 18;
    for (let i = 0; i < n; i++) {
        const geom = new SurfGeometry((u, v) => {
            //return arc(u, v, 1, n, i)
            return arc2(u, v, 1, n, i)
        }, -PI / 2, PI / 2, 0, Math.PI, 20, 50);
        if (i % 2 == 0)
            geoms0.push(geom);
        else
            geoms1.push(geom);
    }
    const geom0 = NormalUtils.addGeom(geoms0)
    const geom1 = NormalUtils.addGeom(geoms1)
    
    
    const materialFun = new THREE.MeshStandardMaterial({
        roughness: 0.1,
        color: 0x0606DD,
        emissive: 0x0606DD,
        emissiveIntensity: 0.5,
        side: THREE.DoubleSide,
        vertexColors: false,

    });
    materialFun.name = "mat1";

    const materialFunb = new THREE.MeshStandardMaterial({
        roughness: 0.1,
        color: 0xDD1212,
        emissiveIntensity : 0.5,
        emissive: 0xDD1212,
        side: THREE.DoubleSide,
        vertexColors: false
    });
    materialFunb.name = "mat2";
    const res = new THREE.Object3D();
    const rf = new THREE.Object3D();
    const me0 = new THREE.Mesh(geom0, materialFun)
    const me1 = new THREE.Mesh(geom1, materialFunb)
    me0.name = "mesh_1"
    me1.name = "mesh_2"
    res.add(me0);
    res.add(me1);
    res.name = "model"
    return res
}


function larme() {
    let a = 1
    const geom = new CurveGeometry((t) => {
        let n = 1
        
        let x = a * Math.cos(t);
        let y = a * Math.sin(t) * Math.pow(Math.sin(t / 2), n)
        let z = 0
        return new THREE.Vector3(x, y, 0);
    },
        Math.PI, 0, 0.05, 100, 40, 1, 2
    );
    return geom;
}

function onion() {
    
    const geom = new CurveGeometry((t) => {
        let p = PI/2 + 50/180*PI
        let a = 1
        if (t > p)
            a = a/Math.cos(t-p)
    
        let x = a * Math.cos(t);
        let y = a * Math.sin(t); 
        let z = 0
        return new THREE.Vector3(x, y, 0);
    },
        0, Math.PI, 0.05, 100, 40, 1, 2
    );
    return geom;
}


const me = ruf()
savegeom(me, "./obj/onion2.obj");
//const me = onion()
//savegeom(me, "./stl/onion.stl");
console.log("ok");

