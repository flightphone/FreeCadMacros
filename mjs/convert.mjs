import { edgeSplit, savegeom, mergeDirSTL } from '../js/nodeExport.mjs';
import * as path from "node:path"
/*
const src = "./stl/pensil/res0.stl";
const dst = "./obj/res0.obj"
edgeSplit(src, dst);
console.log("sucessfull")
*/
//const dir = './stl/pensil';
//const dir = './stl/tube';
//const dir = './stl/royal';
const dir = './stl/light';
const fname = path.basename(dir)
const mesh = mergeDirSTL(dir)
savegeom(mesh, `./obj/${fname}.obj`)
console.log(fname)