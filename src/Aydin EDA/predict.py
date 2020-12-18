import pandas as pd
import numpy as np
import pickle
from model import get_transform_data
from pymongo import MongoClient

def get_model(modelpath='rf.pkl'):
    "Unpickles and returns model"
    return pickle.load(open(modelpath,'rb'))

def mypred(X, y, modelpath='rf.pkl'):
    
    X = X.fillna(0)
    model = get_model(modelpath)
    y_rf = model.predict(X)
    y_rf_proba = model.predict_proba(X)
    return y_rf, y_rf_proba

def db_add(data, y_prob):
    
    data['fraud_prob']=y_prob[1]
    client = MongoClient()
    db = client['test_database']
    test_collection = db['test_collection']
    df = pd.DataFrame.from_dict([data])
    d=df.to_dict('records')[0]
    test_collection.insert_one(d)
    client.close()

if __name__ == '__main__':
    # X, y = get_transform_data('test_script_examples.json')
    # X = X.fillna(0)
    # model = get_model('rf.pkl')
    # y_rf = model.predict(X)
    # y_rf_proba = model.predict_proba(X)
    # print(y_rf)
    # print(y_rf_proba)
    X, y = get_transform_data('test_script_examples.json')
    y_rf, y_rf_proba=mypred(X,y, 'rf.pkl')
    print(y_rf)
    print(y_rf_proba)