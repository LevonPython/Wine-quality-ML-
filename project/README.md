![wine_background](https://github.com/LevonPython/Wine-quality-ML-/blob/main/deployment/static/images/grapes_and_wines.jpg)
# Project structure
Project: Predicting Wine Quality using Wine Quality Dataset.

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


## Data , Features, Training, Prediction

TODO: 

Please run (via Jupyter) the following files by steps:
- `1_EDA.ipynb` - Exploratory Data Analysis: understand the data by EDA and derive simple models with Pandas as baseline, Data wrangling: fill nan, convert categorical to numerical, create train and test data for ML algorithms
- `2_Getting_best_dataframe.ipynb` - Pipline for data correcting, oversampling, wrangling, scaling
- `3_Winequallity_Modelling.ipynb` - cross validation and Hyperparameters, </br>Comparison of Model results use metrics like confusion_matrix, classification_report, accuracy_score and implement k fold cross validation for comparison of test score

As a result of run of  these 3 Juiter files, it autimatically generates and saves the folowwing files for deployement's use:
- `Dataframe_final.csv` - already developed data ready for modeling
- `instance.json` - in this file are saved dataframe instance for simulating prediction during API server
- `rand_forest_model.pkl` - in this file are saved Random Forest (best model for this dataset) model's object for further prediction use

## Tests / Deployement (Flask API)



Project development structure
http://local_ip_address:5000/</br> where local_ip is for example 192.168.0.134</br>
├── /main</br>
│── /raw_data</br>
├── /input</br>
│── /wranglered_input</br>
├── /result</br>
│── /about</br>

TODO: 
Technical steps description for running API and implement tests.


Step 1: Please run deployment/app.py file for raising local flask API (by default debug=True, host=local ip address, port='5000').
This API includes already saved (deployment/rand_forest_model.pkl) Best model's (Random Forest) object with necessary weights for prediction.
```shell script
python deployment/app.py
```
Step 2: Now please run the deployment/client.py to implement POST method to already raised API. 
In this py file is implemented Argparse functionality to help user give necessary inputs (TEST input in JSON file extension)
```shell script
python deployment/client.py data/instance_raw.json
```
Step 3: You can see Web-server side on the local ip address (host=local ip address, port='5000')
to see main page
```shell script
http://local_ip_address:5000/main
```
to see raw data
```shell script
http://local_ip_address:5000/raw_data
```
to see input csv data
```shell script
http://local_ip_address:5000/input
```
to see predicted results
```shell script
http://local_ip_address:5000/result
```
to read about project
```shell script
http://local_ip_address:5000/about
```
