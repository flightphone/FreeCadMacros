//import { OBJExporter } from 'three/examples/jsm/exporters/OBJExporter.js';
import { OBJExporter } from './OBJExporter.js';
import { STLExporter } from 'three/examples/jsm/exporters/STLExporter.js'
import { EdgeSplitModifier } from 'three/examples/jsm/modifiers/EdgeSplitModifier.js'
import * as fs from "node:fs";
import * as THREE from 'three';
import { STLLoader } from 'three/examples/jsm/loaders/STLLoader.js';
import * as path from "node:path"

function savegeom(geom, filename) {
    const me = (geom.isBufferGeometry) ? new THREE.Mesh(geom) : geom;
    if (!me.name)
        me.name = path.basename(filename);

    let ext = path.extname(filename)
    ext = ext.toLowerCase();

    const exporter = (ext == '.obj') ? new OBJExporter() : new STLExporter();
    if (ext == ".stl") {
        const result = exporter.parse(me);
        fs.writeFileSync(filename, result);
    }
    else {
        const dir = path.dirname(filename)
        const filemtl = path.basename(filename).toLowerCase().replace(".obj", ".mtl");
        const filename2 = dir + '/' + filemtl;
        const result = exporter.parse(me, filemtl);
        fs.writeFileSync(filename, result.obj);
        fs.writeFileSync(filename2, result.mtl);
    }
}



function toArrayBuffer(buffer) {
    const arrayBuffer = new ArrayBuffer(buffer.length);
    const view = new Uint8Array(arrayBuffer);
    for (let i = 0; i < buffer.length; ++i) {
        view[i] = buffer[i];
    }
    return arrayBuffer;
}
function calcNormal(geom) {
    const modifier = new EdgeSplitModifier();
    const cutOffAngle = 20 * Math.PI / 180;
    const tryKeepNormals = false;
    const geometry = modifier.modify(geom, cutOffAngle, tryKeepNormals);
    geometry.computeVertexNormals();
    return geometry;
}

function edgeSplit(srcstl, dstobj) {
    const loader = new STLLoader()
    const buffer = fs.readFileSync(srcstl);
    const blobArray = toArrayBuffer(buffer);
    const geom = loader.parse(blobArray)
    const geometry = calcNormal(geom)
    savegeom(geometry, dstobj)
    //console.log("ok")
}
function mergeSTL(srcstl = []) {
    const result = new THREE.Object3D()
    const loader = new STLLoader()
    srcstl.forEach((filename) => {
        const buffer = fs.readFileSync(filename);
        const blobArray = toArrayBuffer(buffer);
        const geom = loader.parse(blobArray);
        const geometry = calcNormal(geom);
        const mesh = new THREE.Mesh(geometry);
        mesh.name = path.basename(filename);
        result.add(mesh)
    });
    return result;
}

function mergeDirSTL(folderPath)
{
    const srcstl = fs.readdirSync(folderPath).map(fileName => {
        return folderPath + '/' + fileName;
      });
    return mergeSTL(srcstl);  
}

export { savegeom, edgeSplit, mergeSTL, mergeDirSTL }