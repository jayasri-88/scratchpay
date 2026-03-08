from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import random
import os

# set frontend folder path
app = Flask(__name__, static_folder="../frontend", static_url_path="")
CORS(app)


# Serve the frontend app
@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")


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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)