import pandas as pd
import numpy as np
import pickle
from model import get_model, get_transform_data


if __name__ == '__main__':
    X, y = get_transform_data('test_script_examples.json')
    X = X.fillna(0)
    model = get_model('rf.pkl')
    y_rf = model.predict(X)
    print(y_rf)