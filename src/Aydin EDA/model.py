import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, f1_score, precision_score, recall_score, roc_curve, classification_report
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
import pickle

class Model():
    # Initialize Model, if model not provided use Random Forest
    def __init__(self, model=None, **kwargs):
        if model == None:
            self.model = RandomForestClassifier(n_estimators=687, max_depth=50, max_features=4)
        else:
            self.model = model(**kwargs)
    def fit(self, X, y):
        self.model.fit(X, y)
        return self

    def predict_proba(self, X):
        return self.model.predict_proba(X)

def get_model(filepath='rf.pkl'):
    "Unpickles and returns model"
    return pickle.load(open('rf.pkl','rb'))

def get_transform_data(data_path):
    data = pd.read_json(data_path)
    
    required_columns=['body_length', 'channels', 'delivery_method', 'event_published',
        'fb_published', 'has_analytics', 'has_logo',
        'name_length', 'num_order', 'num_payouts', 'org_facebook',
        'org_twitter', 'sale_duration', 'sale_duration2', 'show_map',
        'user_age', 'user_created', 'user_type']
    if 'acct_type' in data.columns:
        data['is_fraud'] = data['acct_type'].apply(lambda x: 1 if 'fraud' in x else 0)
    else:
        data['is_fraud']=data.iloc[:, 0].apply(lambda x: 'unknown')
    
    data_model=data[required_columns]
    y = data['is_fraud']
    X = data_model
    return X, y

if __name__ == '__main__':
    X, y = get_transform_data('../../data/data.json')
    X = X.fillna(0)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=15,test_size=0.2, stratify = y)
    model = get_model('rf.pkl')
    model.fit(X_train,y_train)
    y_rf = model.predict(X_test)
    print(classification_report(y_test, y_rf))