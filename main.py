from flask import Flask
from flask import request
# from getScore import calculate_score

app = Flask(__name__)


@app.route('/', methods=['GET'])
# http://127.0.0.1:5000/?appId=450
def hello_world() -> dict:
    # applicationId = request.args.get('appId', type=int)
    # # return {"score": calculate_score(clientId, productId)}
    # return {applicationId: calculate_score(applicationId)}
    return {'Return': "nothing yet"}


# @app.route('/my-route')
# def my_route():
#   page = request.args.get('page', default=1, type=int)
#   filter = request.args.get('filter', default='*', type=str)
#
# @app.route('/login', methods=['GET'])
# def login():
#     username = request.args.get('username')
#     print(username)
#     password= request.args.get('password')
#     print(password)
#     return {username: password}

if __name__ == '__main__':
    app.run(host='127.0.0.1', port="5000", debug=True)
