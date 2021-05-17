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
├── /main </br>
│── /raw_data </br>
├── /input </br>
│── /wranglered_input </br>
├── /result </br>
│── /about </br>

TODO: 
Technical steps description for running API and implement tests.


Step 1: Please run deployment/app.py file for raising local flask API (by default debug=True, host='127.0.0.1', port='5000').</br>
This API includes already saved (deployment/rand_forest_model.pkl) Best model's (Random Forest) object with necessary weights for prediction.</br>

```shell script
python deployment/app.py
```

</br>
Step 2: Now please run the deployment/client.py to implement POST method to already raised API. </br>
In this py file is implemented Argparse functionality to help user give necessary inputs (TEST input in JSON file extension)</br>

```shell script
python deployment/client.py data/instance_raw.json
```

</br>
Step 3: You can see Web-server side on the local host (host='127.0.0.1', port='5000')</br>
to see main page </br>

```shell script
http://localhost:5000/main</br>
```

![Main](https://github.com/LevonPython/Wine-quality-ML-/blob/main/deployment/templates/main_page.PNG)

to see raw data</br>

```shell script
http://localhost:5000/raw_data
```

</br>

![Raw data](https://github.com/LevonPython/Wine-quality-ML-/blob/main/deployment/templates/Raw%20data.PNG)
   
to see input csv data</br>

```shell script
http://localhost:5000/input
```

</br>
to see wranglered data</br>

```shell script
http://localhost:5000/wranglered_input
```

</br>


![Wramglered](https://github.com/LevonPython/Wine-quality-ML-/blob/main/deployment/templates/Wranglered%20data.PNG)
   
to see predicted results</br>

```shell script
http://localhost:5000/result
```

</br>


![Result](https://github.com/LevonPython/Wine-quality-ML-/blob/main/deployment/templates/Result%20page.PNG)

   
to read about project</br>

```shell script
http://localhost:5000/about
```

</br>

![About](https://github.com/LevonPython/Wine-quality-ML-/blob/main/deployment/templates/About.PNG)
  
   
to read  first page</br>

```shell script
http://localhost:5000/
```

</br>

![First](https://github.com/LevonPython/Wine-quality-ML-/blob/main/deployment/templates/First_page.PNG)
   
