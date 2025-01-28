import * as path from "node:path"

let fname = "./obj/www/rufobj.obj"
const ext = path.extname(fname)
const dir = path.dirname(fname)
const bname = path.basename(fname)

const fname2 = bname.replace(".obj", ".mtl");
const fullfname2 = dir + '/'+ fname2
console.log(dir)
console.log(fname2)
console.log(fullfname2)