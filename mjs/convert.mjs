import { edgeSplit } from '../js/nodeExport.mjs';
const src = "./stl/stair.stl";
const dst = "./obj/stair25.obj"
edgeSplit(src, dst);
console.log("sucessfull")