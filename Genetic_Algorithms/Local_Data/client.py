import pandas as pd
import numpy as np

train = None
train_X = None
train_y = None

test = None
test_X = None
text_y = None

def load_data():
    global test_X
    global test_y
    global train_X
    global train_y

    np.set_printoptions(suppress=True)
    
    train = pd.read_csv('./Local_Data/train.csv')
    train_X = train.to_numpy()
    train_y = train_X[:, -1]
    train_X = train_X[:, :-1]
    train_X[:, 0] = np.ones(train_X.shape[0])
    np.insert(train_X, 0, 1, axis=1)
    
    test = pd.read_csv('./Local_Data/test.csv')
    test_X = test.to_numpy()
    test_y = test_X[:, -1]
    test_X = test_X[:, :-1]
    test_X[:, 0] = np.ones(test_X.shape[0])
    np.insert(test_X, 0, 1, axis=1)
    
def get_errors(id, vector):
    global X
    global y
    vector = np.array(vector)
    # for i in vector:
    #     assert 0 <= abs(i) <= 10
    # assert len(vector) == 11
    
    if train == None:
        load_data()
    train_pred = np.dot(train_X, vector.T)
    test_pred = np.dot(test_X, vector.T)
    
    return (np.sum((train_y - train_pred)**2), np.sum((test_y - test_pred)**2))