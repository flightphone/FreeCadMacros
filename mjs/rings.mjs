
import * as THREE from 'three';
import { savegeom } from '../js/nodeExport.mjs';
import { STLLoader } from 'three/examples/jsm/loaders/STLLoader.js';
import { NormalUtils } from '../js/NormalUtils.js';
import * as fs from "node:fs";

const materialFun = new THREE.MeshStandardMaterial({ //new THREE.MeshLambertMaterial({
    color: 0xCCCCCC,
    roughness: 0.2,
    metalness: 0.95,
    side: THREE.FrontSide
});

const materialMid = new THREE.MeshBasicMaterial({ color: 0xFF00FF, side: THREE.DoubleSide })


function createComposite() {
    
    let d = 6.12, w = 0.44, h = 0.35;
    let res = new THREE.Object3D();
    const extrudeSettings = {
        curveSegments: 200,
        steps: 1,
        depth: h,
        bevelEnabled: true,
        bevelThickness: 0.04,
        bevelSize: 0.04,
        bevelOffset: 0,
        bevelSegments: 2,
    };

    const extrudeSettings2 = {
        curveSegments: 200,
        steps: 2,
        depth: h / 4,
        bevelEnabled: true,
        bevelThickness: 0.,
        bevelSize: 0.0,
        bevelOffset: 0,
        bevelSegments: 0,
    };
    let geom1 = createRing(d, w, h, extrudeSettings);
    let mesh1 = new THREE.Mesh(geom1, materialFun);
    mesh1.rotateX(Math.PI / 2.0);
    res.add(mesh1);

    let geom2 = new createRing(d + 0.1, w / 3, h / 4, extrudeSettings2);
    let mesh2 = new THREE.Mesh(geom2, materialMid);
    mesh2.rotateX(Math.PI / 2.0);
    res.add(mesh2);
    return res;

}

function createRing(d, w, h, sets) {
    let r1 = d / 2., r2 = (d - 2 * w) / 2.;
    let ringShape = new THREE.Shape();

    let path = new THREE.Path();
    path.arc(0, 0, r1, 0, Math.PI * 2, false);
    ringShape.add(path);

    let path2 = new THREE.Path();
    path2.arc(0, 0, r2, 0, Math.PI * 2, true);
    ringShape.add(path2);

    let geom1 = new THREE.ExtrudeGeometry(ringShape, sets);
    geom1.translate(0, 0, -h / 2.);
    return geom1;

}

const ring = createComposite() 
savegeom(ring, "./obj/ring.obj");


console.log("ok_ring");

