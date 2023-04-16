# Dynamic Risk Assessment System
The fourth project for [ML DevOps Engineer Nanodegree](https://www.udacity.com/course/machine-learning-dev-ops-engineer-nanodegree--nd0821) by Udacity.

## Description
As part of Unit 5: Machine Learning Model Scoring and Monitoring, the goal of this project is to develop a machine learning model that can assess the risk of attrition for each client of the company. This will involve creating, deploying, and monitoring the model, as well as establishing processes for re-training, re-deploying, monitoring, and reporting on its performance.

## Prerequisites
- Python 3.8 required
- Linux environment may be needed

## Dependencies
The dependencies required for this project can be found in the ```requirements.txt``` file.

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies from the ```requirements.txt```. Its recommended to install it in a separate virtual environment.

```bash
pip install -r requirements.txt
```

## Steps Overview
1. **Data ingestion:** Automate the process of checking for new data that can be used for training the model. Compile all relevant training data into a dataset and save it to a designated folder.
2. **Training, scoring, and deploying:** Develop scripts for training an ML model that can predict attrition risk and scoring the model. Save both the model and scoring metrics.
3. **Diagnostics:** Analyze and save summary statistics related to the dataset. Time the performance of some functions. Check for dependency changes and package updates.
4. **Reporting:** Automatically generate plots and a txt file that report on model metrics and diagnostics. Provide an API endpoint for accessing model predictions and metrics.
5. **Process Automation:** Create a script and cron job that automatically run all previous steps at regular intervals.


## Usage

### 1- Edit config.json file to use practice data

```bash
"input_folder_path": "practicedata",
"output_folder_path": "ingesteddata", 
"test_data_path": "testdata", 
"output_model_path": "practicemodels", 
"prod_deployment_path": "production_deployment"
```

### 2- Run data ingestion
```python
python src/ingestion.py
```
Artifacts output:
```
ingesteddata/finaldata.csv
ingesteddata/ingestedfiles.txt
```

### 3- Model training
```python
python src/training.py
```
Artifacts output:
```
practicemodels/trainedmodel.pkl
```

###  4- Model scoring 
```python
python src/scoring.py
```
Artifacts output: 
```
models/practicemodels/latestscore.txt
``` 

### 5- Model deployment
```python
python src/deployment.py
```
Artifacts output:
```
production_deployment/ingestedfiles.txt
production_deployment/trainedmodel.pkl
production_deployment/latestscore.txt
``` 

### 6- Run diagnostics
```python
python src/diagnostics.py
```

### 7- Run reporting
```python
python src/reporting.py
```
Artifacts output:
```
confusionmatrix.png
```

### 8- Run Flask App
```python
python src/app.py
```


### 9- Run API endpoints
```python
python src/apicalls.py
```
Artifacts output:
```
models/apireturns.txt
```


### 11- Edit config.json file to use production data

```bash
"input_folder_path": "sourcedata",
"output_folder_path": "ingesteddata", 
"test_data_path": "testdata", 
"output_model_path": "models", 
"prod_deployment_path": "production_deployment"
```

### 10- Full process automation
```python
python src/fullprocess.py
```
### 11- Cron job

Start cron service
```bash
sudo service cron start
```

Edit crontab file
```bash
sudo crontab -e
```
   - Write the cron job in ```cronjob.txt``` which runs ```fullprocces.py``` every 10 mins
  
View crontab file
```bash
sudo crontab -l
```