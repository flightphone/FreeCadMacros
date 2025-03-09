
import * as THREE from 'three';
import { savegeom } from '../js/nodeExport.mjs';
import { STLLoader } from 'three/examples/jsm/loaders/STLLoader.js';
import { NormalUtils } from '../js/NormalUtils.js';
import * as fs from "node:fs";

function toArrayBuffer(buffer) {
    const arrayBuffer = new ArrayBuffer(buffer.length);
    const view = new Uint8Array(arrayBuffer);
    for (let i = 0; i < buffer.length; ++i) {
        view[i] = buffer[i];
    }
    return arrayBuffer;
}

function tcube()
{
    const n = 10.;
    const k = 1.;
    const h1 = 0.3;
    const w1 = h1*k*5;
    const geom = new THREE.BoxGeometry(w1, h1, w1);
    return geom;
}

function tcube2()
{
    
    const geom = new THREE.BoxGeometry(0.3, 2., 0.3);
    return geom;
    
}

function tcone()
{
    const h = 1
    const r = 1.2
    const geom = new THREE.ConeGeometry(r, h, 50);
    return geom;
}
function twist()
{
    const srcstl = "./stl/Text-Extrude.stl";
    const loader = new STLLoader()
    const buffer = fs.readFileSync(srcstl);
    const blobArray = toArrayBuffer(buffer);
    const geom = loader.parse(blobArray)
    const res = NormalUtils.make_twist(geom);
    return res;
}
const cube = tcube2() 
savegeom(cube, "./obj/cube2.obj");

//const cone = tcone() 
//savegeom(cone, "./obj/cone.obj");

//const ring = twist() 
//savegeom(ring, "./stl/text_twist.stl");

console.log("ok_twist");

