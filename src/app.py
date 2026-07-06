from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to AI Fake News Detection API"

@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "status": "Server Running"
    })

@app.route("/api/predict", methods=["POST"])
def predict():
    data = request.get_json()

    news = data.get("news", "")

    prediction = "Fake"

    return jsonify({
        "news": news,
        "prediction": prediction
    })

if __name__ == "__main__":
    app.run(debug=True)
