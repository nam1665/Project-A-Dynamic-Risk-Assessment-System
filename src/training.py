import os
import sys
import pickle
import logging
import pandas as pd
from sklearn.linear_model import LogisticRegression
import json
import logging

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

# Load config.json
with open('config.json','r') as f:
    config = json.load(f) 

dataset_path = os.path.join(config['output_folder_path']) 
model_path = os.path.join(config['output_model_path']) 

def train_model():
    """
        Fit a logistic regression model to the ingested data and store the resulting model.
    """

    logging.info("Loading and preparing finaldata.csv")
    data_df = pd.read_csv(os.path.join(dataset_path, 'finaldata.csv'))
    y_df = data_df.pop('exited')
    X_df = data_df.drop(['corporation'], axis=1)

    #use this logistic regression for training
    model = LogisticRegression(C=1.0, 
                                class_weight=None, 
                                dual=False, 
                                fit_intercept=True,
                                intercept_scaling=1, 
                                l1_ratio=None, max_iter=100,
                                multi_class='auto', n_jobs=None, penalty='l2',
                                random_state=0, solver='liblinear', tol=0.0001, verbose=0,
                                warm_start=False)
    
    logging.info("Training model")
    model.fit(X_df, y_df)

    logging.info("Saving trained model")
    pickle.dump(model, open(os.path.join(model_path, 'trainedmodel.pkl'), 'wb'))


if __name__ == '__main__':
    train_model()