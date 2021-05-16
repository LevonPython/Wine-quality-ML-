# Deployement-structure
Project: Predicting Wine Quality using Wine Quality Dataset.

## Business Background

Please provide link to confluence page or describe a project in few sentences. 


## Repo Structure 

- `data` - a folder with working files for API GET/POST functionality
- `result` - a folder with generated result - Json. 
- `templates` - a folder with API structure files - html, jpg
- `app.py` - a main API file for creating API server (run 1st)
- `client.py` - py file for creating POST request to API, reading, wrangling, saving raw data (run 2nd)
- `data_wrangler.py` - py file for wrangling raw data (automatically works while client.py running)
- `decision_tree.py` - py file for implementing Random Forest algorithm (automatically works while client.py running)



## Tests / Deployement (Flask API)



Project development structure
http://localhost:5000/</br>
├── /main</br>
│── /raw_data</br>
├── /input</br>
│── /wranglered_input</br>
├── /result</br>
│── /about</br>

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
.. image:: https://github.com/LevonPython/Wine-quality-ML-/blob/main/deployment/templates/main_page.PNG
   :align: left
   :target: https://github.com/LevonPython/Wine-quality-ML-/blob/main/deployment/templates/main_page.PNG
   :alt: Main
to see raw data
```shell script
http://localhost:5000/raw_data
```
.. image:: https://github.com/LevonPython/Wine-quality-ML-/blob/main/deployment/templates/Raw%20data.PNG
   :align: left
   :target: https://github.com/LevonPython/Wine-quality-ML-/blob/main/deployment/templates/Raw%20data.PNG
   :alt: Raw data
to see input csv data
```shell script
http://localhost:5000/input
```
to see wranglered data
```shell script
http://localhost:5000/wranglered_input
```
.. image:: https://github.com/LevonPython/Wine-quality-ML-/blob/main/deployment/templates/Wranglered%20data.PNG
   :align: left
   :target: https://github.com/LevonPython/Wine-quality-ML-/blob/main/deployment/templates/Wranglered%20data.PNG
   :alt: Wramglered
to see predicted results
```shell script
http://localhost:5000/result
```
.. image:: https://github.com/LevonPython/Wine-quality-ML-/blob/main/deployment/templates/Result%20page.PNG
   :align: left
   :target: https://github.com/LevonPython/Wine-quality-ML-/blob/main/deployment/templates/Result%20page.PNG
   :alt: Result
to read about project
```shell script
http://localhost:5000/about
```
.. image:: https://github.com/LevonPython/Wine-quality-ML-/blob/main/deployment/templates/About.PNG
   :align: left
   :target: https://github.com/LevonPython/Wine-quality-ML-/blob/main/deployment/templates/About.PNG
   :alt: About
   
to read  first page
```shell script
http://localhost:5000/
```
.. image:: https://github.com/LevonPython/Wine-quality-ML-/blob/main/deployment/templates/First_page.PNG
   :align: left
   :target: https://github.com/LevonPython/Wine-quality-ML-/blob/main/deployment/templates/First_page.PNG
   :alt: First
