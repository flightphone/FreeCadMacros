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

function ruf() {
    const geoms0 = []
    const geoms1 = []
    const n = 14;
    for (let i = 0; i < n; i++) {
        const geom = new SurfGeometry((u, v) => {
            return arc(u, v, 1, n, i)
        }, -PI / 2, PI / 2, 0, Math.PI, 30, 50);
        if (i % 2 == 0)
            geoms0.push(geom);
        else
            geoms1.push(geom);
    }
    const geom0 = NormalUtils.addGeom(geoms0)
    const geom1 = NormalUtils.addGeom(geoms1)
    
    //savegeom(geom0, './obj/ruf00.obj');
    savegeom(geom1, './obj/ruf10.obj')
    savegeom(geom0, './stl/ruf_0new.stl');
    //savegeom(geom1, './stl/ruf10.stl')
    
    const materialFun = new THREE.MeshStandardMaterial({
        roughness: 0.1,
        color: 0x0606DD,
        side: THREE.DoubleSide,
        vertexColors: false,

    });
    materialFun.name = "mat1";

    const materialFunb = new THREE.MeshStandardMaterial({
        roughness: 0.1,
        color: 0xDD1212,
        side: THREE.DoubleSide,
        vertexColors: false
    });
    materialFunb.name = "mat2";
    const res = new THREE.Object3D();
    const me0 = new THREE.Mesh(geom0, materialFun)
    const me1 = new THREE.Mesh(geom1, materialFunb)
    me0.name = "mesh1"
    me1.name = "mesh2"
    res.add(me0);
    res.add(me1);
    res.name = "res"
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

//const geom = ruf()
//const geom = larme()
//savegeom(geom, "./stl/rufgroup.stl");
//savegeom(geom, "./obj/rufgroup.obj");
const me = ruf()
//savegeom(me, "./stl/rufobj.stl");
savegeom(me, "./obj/ruf_new.obj");
console.log("ok");

