from flask import Flask, request, render_template
from server_utils import load
import numpy as np

ct = load("model/ct.pkl")
sc = load("model/sc.pkl")
classifier = load("model/classifier.pkl")


app = Flask("app", static_url_path="/", static_folder="web/public", template_folder="web/templates")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/predict", methods=["POST"])
def predict():
    try:
        body = request.get_json()
        test = np.array(ct.transform(np.array([list(body.values())], dtype="object")))
        test[:, [3,6]] = sc.transform(test[:, [3, 6]])
        prediction = classifier.predict(test)
        return { "prediction": int(prediction[0]) }
    except Exception as e: 
        print("couldn't predict oof")
        print(e)
        return { "prediction": 0 }

app.run(host="localhost", port="5500", debug=True)