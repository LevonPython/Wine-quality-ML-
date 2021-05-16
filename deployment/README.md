# Deployement-structure
Project: Predicting Wine Quality using Wine Quality Dataset.

## Business Background

Please provide link to confluence page or describe a project in few sentences. 


## Repo Structure 

- `data` - a folder with working files for API GET/POST functionality
- `result` - a folder with generated result - Json. 
- `templates` - a folder with API structure files - html, jpg
    - `data` - a folder which contains code responsible for gathering raw data from data sources
    - `features` - a folder which contains code responsible for creating features based on raw data
    - `modeling` - a folder which contains code for running training and prediction
    - `utils` - a folder which contains various utility code   
    - `logger.py` - a logger
    
- `test` - a folder which contains unittests
- `scripts` - a folder which contains scripts for data, training and prediction, 
              it basically runs the code written in `src` folder, all the scripts must be run from the project directory


## Tests / Deployement (Flask API)



Project development structure
http://localhost:5000/
├── /main </br>
│── /raw_data
├── /input
│── /wranglered_input
├── /result
│── /about

TODO: 
Technical steps description for running API and implement tests.


Step 1: Please run deployment/app.py file for raising local flask API (by default debug=True, host='127.0.0.1', port='5000').
This API includes already saved (deployment/rand_forest_model.pkl) Best model's (Random Forest) object with necessary weights for prediction.
```shell script
python deployment/app.py
```
Step 2: Now please run the deployment/client.py to implement POST method to already raised API. 
In this py file is implemented Argparse functionality to help user give necessary inputs (TEST input in JSON file extension)
```shell script
python deployment/client.py data/instance_raw.json
```
Step 3: You can see Web-server side on the local host (host='127.0.0.1', port='5000')
to see main page
```shell script
http://localhost:5000/main
```
to see raw data
```shell script
http://localhost:5000/raw_data
```
to see input csv data
```shell script
http://localhost:5000/input
```
to see predicted results
```shell script
http://localhost:5000/result
```
to read about project
```shell script
http://localhost:5000/about
```
