import { OBJExporter } from 'three/examples/jsm/exporters/OBJExporter.js';
import { EdgeSplitModifier } from 'three/examples/jsm/modifiers/EdgeSplitModifier.js'
import * as fs from "node:fs";
import * as THREE from 'three';
import { STLLoader } from 'three/examples/jsm/loaders/STLLoader.js';

function savegeom(geom, filename) {
    const me = new THREE.Mesh(geom)
    const exporter = new OBJExporter();
    const result = exporter.parse(me)
    fs.writeFileSync(filename, result)
}

function toArrayBuffer(buffer) {
    const arrayBuffer = new ArrayBuffer(buffer.length);
    const view = new Uint8Array(arrayBuffer);
    for (let i = 0; i < buffer.length; ++i) {
        view[i] = buffer[i];
    }
    return arrayBuffer;
}

function edgeSplit(srcstl, dstobj) {
    const loader = new STLLoader()
    const buffer = fs.readFileSync(srcstl);
    const blobArray = toArrayBuffer(buffer);
    const geom = loader.parse(blobArray)
    const modifier = new EdgeSplitModifier();
    const cutOffAngle = 20 * Math.PI / 180;
    const tryKeepNormals = false;
    const geometry = modifier.modify(geom, cutOffAngle, tryKeepNormals);
    geometry.computeVertexNormals();
    savegeom(geometry, dstobj)
    //console.log("ok")
}

export { savegeom, edgeSplit }