from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)   # allow frontend requests

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
    app.run(debug=True)