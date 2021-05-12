import requests
import json

url = "http://localhost:5000/predict"


json_file_path = "preprocessing.json"

with open(json_file_path, 'r') as j:
    contents = json.loads(j.read())
    print(contents)
    r = requests.post(url, json=contents)
    print(r.text)
