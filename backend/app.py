from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route("/")

def home():
    return "Backend Running"

@app.route("/api/tank")

def tank():
    return jsonify({
        "level": random.randint(0,100),
        "temperature": random.randint(20,40),
        "status": "ONLINE"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
