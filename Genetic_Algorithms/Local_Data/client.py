import pandas as pd
import numpy as np

train = None
X = None
y = None

def load_data():
    global X
    global y
    train = pd.read_csv('./train.csv')
    X = train.to_numpy()
    np.set_printoptions(suppress = True)
    X = X[:, :-1]
    X[:, 0] = np.ones(X.shape[0])
    np.insert(X, 0, 1, axis=1)
    y = X[:, -1]
    
def get_errors(id, vector):
    global X
    global y
    vector = np.array(vector)
    for i in vector:
        assert 0 <= abs(i) <= 10
    assert len(vector) == 11
    
    if train == None:
        load_data()
    pred = np.dot(X, vector.T)
    
    return np.mean((y - pred)**2)