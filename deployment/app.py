import pandas as pd
import numpy as np
from flask import Flask, render_template
from flask import request, jsonify
import requests
from sklearn import metrics
import pickle
import json
from decision_tree import RandomForest
from sklearn.preprocessing import StandardScaler
# from ensemble_methods import RandomForest

app = Flask(__name__)

global content

def score(data: list):
    print("SCORE!")
    input_arr = data
    print(f"Json: {input_arr}")
    model = RandomForest.load("md", "data/rand_forest_model.pkl")
    print(f"Pickle: {model}")

    X = StandardScaler().fit_transform([list(i[:-1]) for i in input_arr])
    y = [list(i[-1:]) for i in input_arr]
    print(f"X is: {X}")
    print(f"y is: {y}")

    # in case of 1 row input
    # X = [value for key, value in input_arr[0].items()]
    # print(f"X is: {[X]}")
    # result = model.predict([X])
    # print(f"result: {result}")
    # print(f"type result: {type(result)}")

    # calculate prediction
    predict_list = []
    for i in X:
        predict_list.append(model.predict([i]))
    predicted_np = np.array([i[0] for i in predict_list])
    print(f"predicted: {predicted_np}")

    # # calculate prediction with manually written model
    # predict_list = []
    # for i in X:
    #     predict_list.append(RandomForest.predict("", [i]))
    # predicted_np = np.array([i[0] for i in predict_list])
    # print(f"RF predicted: {predicted_np}")
    # calculate accuracy
    accuracy = metrics.accuracy_score(np.array(y).reshape(-1,1), predicted_np)
    print(f"accuracy: {accuracy}")

    with open('result/accuracy.json', 'w') as outfile:
        json.dump({"accuracy": accuracy, "prediction": predicted_np.tolist()}, outfile)
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

@app.route('/result', methods=['GET'])
def result():
    with open('result/accuracy.json') as json_file:
        data = json.load(json_file)
    return jsonify(data)


@app.route('/raw_data', methods=['GET'])
def data():
    df = pd.read_csv("data\winequalityN.csv")
    table = df.head(20).to_html(classes="table table-striped")
    """<h1>Raw Data</h1>"""
    return table

@app.route('/input', methods=['GET'])
def input_data():
    df = pd.read_csv("data\instance_raw.csv")
    table = df.head(20).to_html(classes="table table-striped")
    """<h1>Input test data (csv format)</h1>"""
    return table\

@app.route('/wranglered_input', methods=['GET'])
def input_wr_data():
    df = pd.read_csv("data\instance_wranglered.csv")
    table = df.head(20).to_html(classes="table table-striped")
    """<h1>Input test data (csv format)</h1>"""
    return table


@app.route('/about', methods=['GET'])
def about():
    return render_template("main.html")

@app.route('/main', methods=['GET'])
def main():
    return """
    <h1>Please choose any option below</h1></br>
    <h3>
    <a href="http://localhost:5000/">Return</a></br></br>
    <a href="http://localhost:5000/raw_data">Raw data sample</a></br>
    <a href="http://localhost:5000/input">Input test data (csv format)</a></br>
    <a href="http://localhost:5000/wranglered_input">Input test <b>wranglered</b> data -  (csv format)</a></br>
    <a href="http://localhost:5000/result">Result</a></br>
    <a href="http://localhost:5000/about">About</a></br>
    </h3>
    """

@app.route('/', methods=['GET'])
def first_page():
    return render_template("first_page.html")


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='5000')
