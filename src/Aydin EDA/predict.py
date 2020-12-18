import pandas as pd
import numpy as np
import pickle
from model import get_transform_data

def get_model(filepath='rf.pkl'):
    "Unpickles and returns model"
    return pickle.load(open('rf.pkl','rb'))

def mypred(filepath, modelpath):
    X, y = get_transform_data(filepath)
    X = X.fillna(0)
    model = get_model(modelpath)
    y_rf = model.predict(X)
    y_rf_proba = model.predict_proba(X)
    return y_rf, y_rf_proba

if __name__ == '__main__':
    # X, y = get_transform_data('test_script_examples.json')
    # X = X.fillna(0)
    # model = get_model('rf.pkl')
    # y_rf = model.predict(X)
    # y_rf_proba = model.predict_proba(X)
    # print(y_rf)
    # print(y_rf_proba)
    y_rf, y_rf_proba=mypred('test_script_examples.json', 'rf.pkl')
    print(y_rf)
    print(y_rf_proba)