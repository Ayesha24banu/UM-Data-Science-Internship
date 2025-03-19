from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load model and scaler
model = joblib.load("models/mortality_model.pkl")
scaler = joblib.load("models/scaler.pkl")

@app.route("/", methods=["GET"])
def home():
    return render_template('index.html')

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Validate request content type
        if request.content_type != "application/json":
            return jsonify({"error": "Unsupported Media Type. Content-Type must be 'application/json'."}), 415

        data = request.get_json()
        features = ["Year", "Metric", "Tobacco Use Duration", "Affordability Index", "Population Percentage"]

        if not all(f in data for f in features):
            return jsonify({"error": "Missing required fields."}), 400

        input_data = np.array([[data[f] for f in features]])
        scaled_data = scaler.transform(input_data)
        prediction = model.predict(scaled_data)

        return jsonify({"prediction": prediction.tolist()})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
