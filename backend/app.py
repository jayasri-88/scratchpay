from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import random
import os
import uuid
from database import init_db, create_scratch_link, update_scratch, get_all_links

# set frontend folder path
app = Flask(__name__, static_folder="../frontend", static_url_path="")
CORS(app)

# Initialize database
init_db()

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
    
    code = str(uuid.uuid4())
    create_scratch_link(code)
    update_scratch(code, reward)

    return jsonify({
        "reward": reward,
        "code": code
    })

# Cards list for admin dashboard
@app.route("/cards", methods=["GET"])
def get_cards():
    cards = get_all_links()
    cards_list = []
    for card in cards:
        cards_list.append({
            "id": card[0],
            "reward": card[2],
            "claimed": card[3] == 1
        })
    return jsonify(cards_list)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)