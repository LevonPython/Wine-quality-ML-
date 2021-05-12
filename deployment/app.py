import pickle
import pandas as pd
from flask import Flask
from flask import request, jsonify
import json
import numpy as np
from model_group1 import Model
import requests

app = Flask(__name__)

global content

def score(data: list):
    input = np.array(data)
    model = Model.load("model.pkl")
    return model.predict(input)


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    global content
    ap = {'features': "None"}
    if request.method == 'POST':

        content = request.get_json()
        print(f"content is {content}")

        pass
        # try:
        #     content = request.get_json(force=True)
        #     print(f"content is {content}")
        #
        #     prediction = score(content["data"])
        #
        # except Exception as e:
        #     return {"message": str(e)}
        # return json.dumps({"prediction": prediction[0].tolist()})
    return jsonify(content)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='5000')

# if __name__ == '__main__':
#     print(score([[0],
#                  [1],
#                  [2],
#                  [3]]))
