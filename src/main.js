import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { STLLoader } from 'three/examples/jsm/loaders/STLLoader';
import { EdgeSplitModifier } from 'three/addons/modifiers/EdgeSplitModifier.js';


const stl_url = "./stl/render.stl";



const materialFun = new THREE.MeshStandardMaterial({
  roughness: 0.1,
  color: 0xDECA95,
  side: THREE.FrontSide,
  vertexColors: false
});

const materialFunb = new THREE.MeshStandardMaterial({
  roughness: 0.1,
  color: 0xDD1212,
  side: THREE.BackSide,
  vertexColors: false
});


//init scene
let renderer = new THREE.WebGLRenderer({ antialias: true, preserveDrawingBuffer: true });
renderer.setPixelRatio(window.devicePixelRatio);
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);



const camera = new THREE.PerspectiveCamera(75, 2, 0.1, 500);
const scene = new THREE.Scene();




//look
camera.position.set(0, 0, 10);
camera.up.set(0, 1, 0);
camera.lookAt(0, 0, 0);


{
  const hemiLight = new THREE.HemisphereLight(0xffffff, 0x444444, 2);
  hemiLight.position.set(0, 20, 0);
  scene.add(hemiLight);
}

{
  const hemiLight = new THREE.HemisphereLight(0xffffff, 0x444444, 1);
  hemiLight.position.set(0, -20, 0);
  scene.add(hemiLight);
}

{
  const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
  directionalLight.position.set(0, 0, 20);
  scene.add(directionalLight);
}

{
  const directionalLight = new THREE.DirectionalLight(0xffffff, 2);
  directionalLight.position.set(0, 0, -20);
  scene.add(directionalLight);
}

CreatePanel();

//=========================init object======================

let controls = new OrbitControls(camera, renderer.domElement);
controls.update();
window.addEventListener('resize', onWindowResize);
onWindowResize();
requestAnimationFrame(render);

function render(time) {
  controls.update();
  renderer.render(scene, camera);
  requestAnimationFrame(render);
}

function onWindowResize() {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
}

function CreatePanel(scale = true) {
  const loader = new STLLoader()
  loader.load(
    stl_url,
    function (geom) {
      const modifier = new EdgeSplitModifier();
      const cutOffAngle = 20 * Math.PI / 180;
      const tryKeepNormals = false;
      const geometry = modifier.modify(geom, cutOffAngle, tryKeepNormals);
      geometry.computeVertexNormals();
      geometry.computeBoundingSphere();
      let sc = 5.5 / geometry.boundingSphere.radius;
      geometry.scale(sc, sc, sc);
      const cnt = geometry.boundingSphere.center;

      const me = new THREE.Mesh(geometry, materialFun)
      me.translateX(-cnt.x)
      me.translateY(-cnt.y)
      me.translateZ(-cnt.z)
      me.material.flatShading = false;
      scene.add(me)

      const me2 = new THREE.Mesh(geometry, materialFunb)
      me2.translateX(-cnt.x)
      me2.translateY(-cnt.y)
      me2.translateZ(-cnt.z)
      me2.material.flatShading = false;
      scene.add(me2)

    },
    (xr) => {

    },
    (error) => {
      console.log(error)
    }
  )
}







