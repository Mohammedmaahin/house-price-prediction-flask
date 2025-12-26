from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    area = float(request.form["area"])
    bedrooms = float(request.form["bedrooms"])
    age = float(request.form["age"])

    features = np.array([[area, bedrooms, age]])
    features_scaled = scaler.transform(features)

    prediction = model.predict(features_scaled)[0]

    return render_template(
        "index.html",
        prediction_text=f"Estimated House Price: ₹ {round(prediction, 2)}"
    )

if __name__ == "__main__":
    app.run(debug=True)