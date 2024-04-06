document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('generate-dungeon').addEventListener('click', function() {
        const container = document.getElementById('3d-container');
        container.innerHTML = '';

        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, container.offsetWidth / container.offsetHeight, 0.1, 1000);

        const renderer = new THREE.WebGLRenderer();
        renderer.setSize(container.offsetWidth, container.offsetHeight);
        container.appendChild(renderer.domElement);

        const ambientLight = new THREE.AmbientLight(0xcccccc, 2.4);
        scene.add(ambientLight);
        const directionalLight = new THREE.DirectionalLight(0xffffff, 2.8);
        directionalLight.position.set(0, 1, 0);
        scene.add(directionalLight);

        const loader = new THREE.GLTFLoader();
        loader.load('/generate_dungeon', function(gltf) {
            scene.add(gltf.scene);
            // Adjust the camera position as needed
            camera.position.set(0, 20, 30);
            
            // Add OrbitControls
            const controls = new THREE.OrbitControls(camera, renderer.domElement);
            controls.target.set(0, 0, 0); // Adjust based on the position of your object
            controls.update();

            animate();
        }, undefined, function(error) {
            console.error('An error happened', error);
        });

        function animate() {
            requestAnimationFrame(animate);
            // controls.update(); // only required if controls.enableDamping = true, or if controls.autoRotate = true
            renderer.render(scene, camera);
        }
    });
});
