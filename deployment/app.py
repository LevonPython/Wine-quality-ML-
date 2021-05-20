import pandas as pd
import numpy as np
from flask import Flask, render_template
from flask import request, jsonify
from sklearn import metrics
import json
from decision_tree import RandomForest
from sklearn.preprocessing import StandardScaler
# from ensemble_methods import RandomForest
import socket


app = Flask(__name__, template_folder='templates')

global content


def score(data: list):
    print("SCORE!")
    input_arr = data
    print(f"Json: {input_arr}")
    model = RandomForest.load('', "data/rand_forest_model.pkl")
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
    accuracy = metrics.accuracy_score(np.array(y).reshape(-1, 1), predicted_np)
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
    html_string = '''
    <html>
      <head><title>HTML Pandas Dataframe with CSS</title></head>
      <link rel="stylesheet" type="text/css" href="df_style.css"/>
<body style="background: url('static/images/grapes_and_wines.jpg');   background-size: 100% 100%;
     height: 300px; background-size: cover;">
        <h3><a href="/main">Return to main page</a></h3></br>
      <h1>Results</h1><br/>
        <h2>Accuracy: {accuracy}</br>
        Prediction: </h2> {prediction}
      </body>
    </html>.
    '''
    # OUTPUT AN HTML FILE
    with open('templates/results.html', 'w') as f:
        f.write(html_string.format(accuracy=data['accuracy'], prediction=data['prediction']))
    return render_template('results.html')


@app.route('/raw_data', methods=['GET'])
def data():
    df = pd.read_csv(r"data\winequalityN.csv")
    table = df.head(20).to_html(classes="table table-striped")
    print(table)

    pd.set_option('colheader_justify', 'center')  # FOR TABLE <th>

    html_string = '''
    <html>
      <head><title>HTML Pandas Dataframe with CSS</title></head>
      <link rel="stylesheet" type="text/css" href="df_style.css"/>
<body style="background: url('static/images/grapes_and_wines.jpg');   background-size: 100% 100%;
     height: 300px; background-size: cover;">
    <h3><a href="/main">Return to main page</a></h3></br>
      <h1>Raw Data</h1><br/>
        {table}
      </body>
    </html>.
    '''

    # OUTPUT AN HTML FILE
    with open('templates/data.html', 'w') as f:
        f.write(html_string.format(table=table))
        print("WRITTEN")

    return render_template("data.html")


@app.route('/input', methods=['GET'])
def input_data():
    df = pd.read_csv(r"data\instance_raw.csv")
    table = df.head(20).to_html(classes="table table-striped")
    html_string = '''
    <html>
      <head><title>HTML Pandas Dataframe with CSS</title></head>
      <link rel="stylesheet" type="text/css" href="df_style.css"/>
<body style="background: url('static/images/grapes_and_wines.jpg');   background-size: 100% 100%;
     height: 300px; background-size: cover;">
    <h3><a href="/main">Return to main page</a></h3></br>
      <h1>Input test data</h1><br/>
        {table}
      </body>
    </html>.
    '''
    # OUTPUT AN HTML FILE
    with open('templates/input.html', 'w') as f:
        f.write(html_string.format(table=table))
    return render_template('input.html')


@app.route('/wrangler_input', methods=['GET'])
def input_wr_data():
    df = pd.read_csv(r"data\instance_wrangler.csv")
    table = df.head(20).to_html(classes="table table-striped")

    html_string = '''
    <html>
      <head><title>HTML Pandas Dataframe with CSS</title></head>
      <link rel="stylesheet" type="text/css" href="df_style.css"/>
<body style="background: url('static/images/grapes_and_wines.jpg');   background-size: 100% 100%;
     height: 300px; background-size: cover;">
        <h3><a href="/main">Return to main page</a></h3></br>
      <h1>Input test data (wrangler)</h1><br/>
        {table}
      </body>
    </html>.
    '''
    # OUTPUT AN HTML FILE
    with open('templates/wrangler_input.html', 'w') as f:
        f.write(html_string.format(table=table))
    return render_template('wrangler_input.html')


@app.route('/about', methods=['GET'])
def about():
    a_main = "ABOUT information"
    return render_template("about.html", a_main=a_main)


@app.route('/main', methods=['GET'])
def main():

    return render_template('main.html', ipaddress=local_ip)


@app.route('/', methods=['GET'])
def home():
    return render_template("home.html", ip_address=local_ip)


@app.route('/data_visualizing', methods=['GET'])
def reports():
    return render_template('reports.html')


if __name__ == '__main__':
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(f"Ip address: {local_ip}")
    app.run(debug=True, host=local_ip, port='5000')
