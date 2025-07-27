from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Dummy user data (in real use, connect with database)
user_data = {
    "username": "vansh",
    "balance": 38.76
}

@app.route("/")
def home():
    return render_template("index.html", username=user_data["username"], balance=user_data["balance"])

@app.route("/generate", methods=["POST"])
def generate():
    amount = float(request.form["amount"])
    message = request.form["message"]

    if amount <= 0 or amount > user_data["balance"]:
        return jsonify({"error": "Invalid amount"}), 400

    user_data["balance"] -= amount
    link = f"https://yourpanel.com/lifafa/ABC123?amt={amount}&msg={message}"

    return jsonify({
        "lifafa_link": link,
        "new_balance": user_data["balance"]
    })

@app.route("/claim", methods=["POST"])
def claim():
    claim_amount = float(request.form["claim_amount"])

    if claim_amount <= 0:
        return jsonify({"error": "Invalid claim amount"}), 400

    user_data["balance"] += claim_amount

    return jsonify({
        "message": f"₹{claim_amount} claimed successfully!",
        "new_balance": user_data["balance"]
    })

if __name__ == "__main__":
    app.run(debug=True)
