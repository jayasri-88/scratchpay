from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)   # allow frontend requests


# Home route (prevents 404 on Render root URL)
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "ScratchPay Backend Running 🚀"
    })


# Scratch reward generator API
@app.route("/generate", methods=["POST"])
def generate():

    rewards = [
        "₹10 Cashback",
        "₹20 Cashback",
        "₹50 Amazon Voucher",
        "₹100 Gift Card",
        "Better Luck Next Time"
    ]

    reward = random.choice(rewards)

    return jsonify({
        "reward": reward
    })


# Health check route (optional but good for deployment)
@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "Server is healthy"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)