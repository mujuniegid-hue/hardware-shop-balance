from flask import Flask, request, jsonify

app = Flask(__name__)

# The "notebook": customer name -> amount owed (in Uganda shillings)
customers = {
    "Joseph": 45000,
    "Grace": 120000,
    "Moses": 0,
    "Sarah": 87500,
    "David": 230000,
    "Esther": 15000,
}

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Ham Hardware - Balance Checker</title>
    </head>
    <body>
        <h1>Ham Hardware</h1>
        <p>Check a customer's credit balance.</p>

        <form action="/api/balance" method="get">
            <label for="name">Customer name:</label>
            <input type="text" id="name" name="name" placeholder="e.g. Joseph">
            <button type="submit">Check balance</button>
        </form>
    </body>
    </html>
    """

@app.route("/api/balance", methods=["GET"])
def balance():
    name = request.args.get("name", "").strip().title()

    if name == "":
        return jsonify({"error": "Please provide a name, e.g. /api/balance?name=Joseph"}), 400

    if name not in customers:
        return jsonify({"error": f"No customer found named {name}"}), 404

    return jsonify({"name": name, "balance": customers[name]})

if __name__ == "__main__":
    app.run(debug=True)