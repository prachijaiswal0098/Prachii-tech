from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/health')
def health():
    return jsonify({"status":"Running"})

@app.route('/api/predict', methods=['POST'])
def predict():
    return jsonify({"prediction":"Fake News"})

if __name__ == '__main__':
    app.run(debug=True)
