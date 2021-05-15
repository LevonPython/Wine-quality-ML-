# ds-template-structure
Template project structure for all data science projects.

## Business Background

Please provide link to confluence page or describe a project in few sentences. 


## Repo Structure 

- `notebooks` - a folder with jupyter notebooks
- `reports` - a folder with generated reports - HTML, PDF and etc. 
- `src` - the main folder with actual code, very often jupyter notebooks should import 
          functions - classes defined in this folder
    - `data` - a folder which contains code responsible for gathering raw data from data sources
    - `features` - a folder which contains code responsible for creating features based on raw data
    - `modeling` - a folder which contains code for running training and prediction
    - `utils` - a folder which contains various utility code   
    - `logger.py` - a logger
    
- `test` - a folder which contains unittests
- `scripts` - a folder which contains scripts for data, training and prediction, 
              it basically runs the code written in `src` folder, all the scripts must be run from the project directory


## Data 

TODO: 

Please describe technical steps for data gathering.
Write samples for running scripts.
For example: 

```shell script
python3 scripts/data.py make-dataset --arg-1 45 --arg-2 true ...
```

## Features 

TODO: 

Please describe technical steps for creating features.
Write samples for running scripts.
For example: 

```shell script
python3 scripts/data.py build-features --arg-1 45 --arg-2 true ...
```

## Training 


Please describe technical steps for running training.
Write samples for running scripts.
For example: 

```shell script
python -m scripts.train --pipe-path "results\pipe.pkl"
```

## Prediction 

TODO: 

Please describe technical steps for making prediction.
Write samples for running scripts.
For example: 

```shell script
python3 scripts/score.py --arg-1 45 --arg-2 true ...
```

## Tests / Deployement (Flask API)

TODO: 

Technical steps description for running tests.

Step 1: Please run deployment/app.py script for raising local flask API (by default debug=True, host='127.0.0.1', port='5000').
This API includes already saved (deployment/rand_forest_model.pkl) Best model's (Random Forest) object with necessary weights for prediction.
```shell script
python deployment/app.py
```
Step 2: Now please run the deployment/client.py to implement POST method to already raised API. 
In this py file is implemented Argparse functionality to help user give necessary inputs (TEST input in JSON file extension)
```shell script
python deployment/client.py instance.json
```
