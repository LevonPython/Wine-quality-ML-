import pandas as pd
import numpy as np
from flask import Flask
from flask import request, jsonify
import requests
from sklearn import metrics
import pickle
import json
from decision_tree import RandomForest

app = Flask(__name__)

global content


def score(data: list):
    input_arr = np.array(data)
    print(f"Json: {input_arr}")
    model = RandomForest.load("md", "rand_forest_model.pkl")
    print(f"Pickle: {model}")

    X = [list(i.values())[:-1] for i in input_arr]
    y = [list(i.values())[-1:] for i in input_arr]
    print(f"X is: {X}")
    print(f"y is: {y}")
    print(f"y is: {type(y)}")

    # in case of 1 row input
    # X = [value for key, value in input_arr[0].items()]
    # print(f"X is: {[X]}")
    # result = model.predict([X])
    # print(f"result: {result}")
    # print(f"type result: {type(result)}")

    # calculate prediction
    # predict_list = []
    # for i in X:
    #     predict_list.append(model.predict([i]))
    # predicted_np = np.array([i[0] for i in predict_list])
    # print(f"predicted: {predicted_np}")

    # calculate prediction with manually written model
    predict_list = []
    for i in X:
        predict_list.append(RandomForest.predict("", [i]))
    predicted_np = np.array([i[0] for i in predict_list])
    print(f"RF predicted: {predicted_np}")

    # calculate accuracy
    accuracy_list = []
    for i in range(len(input_arr)):
        print(f"X{i}: {X[i]} {type(X[i])}")
        print(f"y{i}: {y[i]} {type(y[i])}")
        accuracy_list.append(metrics.accuracy_score(np.array([i]), np.array([i])))
    print(f"accuracy_list: {accuracy_list}")

    return predicted_np


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    global content
    if request.method == 'POST':
        try:
            content = request.get_json()
            print(f"content is {content}")

            prediction = score(content["data"])
        except Exception as e:
            return {"message": str(e)}
        return json.dumps({"prediction": prediction.tolist()})
    return jsonify(content)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='5000')
