import pickle
import pandas as pd
from flask import Flask
from flask import request, jsonify
import json
import numpy as np
from decision_tree import RandomForest
import requests

app = Flask(__name__)

global content


def score(data: list):
    input_arr = np.array(data)
    print(f"Json: {input_arr}")
    model = RandomForest.load("", "model.pkl")
    print(f"Pickle: {model}")
    return model.predict(input_arr)


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    global content
    if request.method == 'POST':
        try:
            content = request.get_json()
            print(f"content is {content}")

            prediction = score(content["features"])
        except Exception as e:
            return {"message": str(e)}
        return json.dumps({"prediction": prediction[0].tolist()})
    return jsonify(content)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='5000')
