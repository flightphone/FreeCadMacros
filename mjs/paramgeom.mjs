import { ImplicitGeometry } from '../js/ImplicitGeometry.js';
import { CurveGeometry } from '../js/CurveGeometry.js'
import { SurfGeometry } from '../js/SurfGeometry.js';
import { MathCurve } from '../js/MathCurve2.js';
import * as MCF from '../js/mathcurve.js'
import * as THREE from 'three';
import { savegeom, edgeSplit } from '../js/nodeExport.mjs';
import { NormalUtils } from '../js/NormalUtils.js';
import {imageFromBuffer} from '@canvas/image';
import * as fs from "node:fs";

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

async function testimage()
{

}

function shell()
{
    const geom = new SurfGeometry(MCF.shell, 0, 14 * Math.PI, 0, 2 * Math.PI, 1000,  100, 10);
    const geom2 = NormalUtils.make_offset(geom, 0.05);
    
    const materialGeom = new THREE.MeshStandardMaterial({
        roughness: 0.6,
        side: THREE.DoubleSide
    });
    materialGeom.extMap = {map_Kd: "perlamutr.jpg", map_Pd: "perlamutr.jpg"}
    materialGeom.name = "mat1";

    const materialGeom2 = new THREE.MeshStandardMaterial({
        roughness: 0.5,
        color: 0xDD1212,
        side: THREE.DoubleSide,
        //vertexColors: false
    });
    materialGeom2.name = "mat2";
    materialGeom2.extMap = {map_Kd: "wood.jpg" }
    const res = new THREE.Object3D();
    const me0 = new THREE.Mesh(geom, materialGeom)
    const me1 = new THREE.Mesh(geom2, materialGeom2)
    me0.name = "mesh_1"
    me1.name = "mesh_2"
    res.add(me0);
    res.add(me1);
    res.name = "model"
    savegeom(res, "./obj/shell40.obj");
    return res;
    //return geom;
}
shell()
//const geom = ch1()
//savegeom(geom, "./stl/shell25.stl");
//savegeom(geom, "./obj/render.obj");
console.log("shell");

