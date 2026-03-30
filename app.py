from flask import Flask, render_template_string, request, jsonify
import random
import os

app = Flask(__name__)

# 🧠 Dummy AI logic (replace later with real model)
def predict_next_word(text):
    emotions = {
        "happy": ["joy", "smile", "excited"],
        "sad": ["alone", "tired", "lost"],
        "angry": ["rage", "furious", "annoyed"],
        "neutral": ["okay", "fine", "normal"]
    }

    if "happy" in text.lower():
        emotion = "happy"
    elif "sad" in text.lower():
        emotion = "sad"
    elif "angry" in text.lower():
        emotion = "angry"
    else:
        emotion = "neutral"

    return random.choice(emotions[emotion]), emotion


# 🎬 FULL CINEMATIC HTML (3D + Animation)
HTML = """
<!DOCTYPE html>
<html>
<head>
<title>AURA Text AI</title>

<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>

<style>
body {
    margin: 0;
    overflow: hidden;
    font-family: 'Poppins', sans-serif;
    background: black;
    color: white;
}

#canvas {
    position: fixed;
    top: 0;
    left: 0;
}

.content {
    position: absolute;
    top: 40%;
    width: 100%;
    text-align: center;
}

h1 {
    font-size: 3.5em;
    background: linear-gradient(90deg, #a855f7, #3b82f6);
    -webkit-background-clip: text;
    color: transparent;
}

input {
    padding: 15px;
    width: 300px;
    border-radius: 10px;
    border: none;
    margin-top: 20px;
}

button {
    padding: 15px 25px;
    margin-left: 10px;
    border-radius: 10px;
    border: none;
    background: linear-gradient(90deg, #9333ea, #2563eb);
    color: white;
    cursor: pointer;
}

.result {
    margin-top: 30px;
    font-size: 24px;
}
</style>
</head>

<body>

<canvas id="canvas"></canvas>

<div class="content">
    <h1>AURA Text AI</h1>
    <p>Where Words Understand Emotions</p>

    <input id="text" placeholder="Type your feelings..." />
    <button onclick="predict()">Predict</button>

    <div class="result" id="result"></div>
</div>

<script>
// 🎥 THREE.JS 3D BACKGROUND
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({canvas: document.getElementById("canvas")});
renderer.setSize(window.innerWidth, window.innerHeight);

// 🌌 Particle stars
const geometry = new THREE.BufferGeometry();
const vertices = [];

for (let i = 0; i < 5000; i++) {
    vertices.push(
        THREE.MathUtils.randFloatSpread(2000),
        THREE.MathUtils.randFloatSpread(2000),
        THREE.MathUtils.randFloatSpread(2000)
    );
}

geometry.setAttribute('position', new THREE.Float32BufferAttribute(vertices, 3));
const material = new THREE.PointsMaterial({color: 0x8888ff});
const stars = new THREE.Points(geometry, material);
scene.add(stars);

// 🔮 AI Orb
const sphere = new THREE.Mesh(
    new THREE.SphereGeometry(2, 32, 32),
    new THREE.MeshBasicMaterial({color: 0x9333ea, wireframe: true})
);
scene.add(sphere);

camera.position.z = 10;

// 🎬 Animation loop
function animate() {
    requestAnimationFrame(animate);
    sphere.rotation.y += 0.01;
    stars.rotation.y += 0.0005;
    renderer.render(scene, camera);
}
animate();

// 🖱️ Mouse parallax
document.addEventListener("mousemove", (e) => {
    camera.position.x = (e.clientX / window.innerWidth - 0.5) * 5;
    camera.position.y = -(e.clientY / window.innerHeight - 0.5) * 5;
});

// 🚀 Prediction
async function predict() {
    let text = document.getElementById("text").value;

    let res = await fetch("/predict", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({text: text})
    });

    let data = await res.json();

    document.getElementById("result").innerHTML =
        "Next Word: <b>" + data.word + "</b><br>Emotion: " + data.emotion;

    gsap.from(".result", {opacity: 0, y: 50, duration: 1});
}
</script>

</body>
</html>
"""

# 🌐 Routes
@app.route("/")
def home():
    return render_template_string(HTML)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text", "")

    word, emotion = predict_next_word(text)

    return jsonify({"word": word, "emotion": emotion})


# 🚀 Run (Render compatible)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)