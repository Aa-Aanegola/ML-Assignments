import numpy as np
import random
import pandas as pd
from sklearn.datasets import make_regression

features, output, coef = make_regression(n_samples = 1000,
                                         n_features = 10,
                                         n_informative = 9,
                                         n_targets = 1,
                                         bias = 0.5,
                                         noise = 0.2,
                                         coef = True)

features = pd.DataFrame(features, columns = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
output = pd.DataFrame(output, columns = ['OUT'])
coef = pd.DataFrame(coef, columns=['Coefficient Values'])

train = features.head(900)
test = features.tail(100)

train['OUT'] = output.head(900)['OUT']
test['OUT'] = output.tail(100)['OUT']

train_csv = train.to_csv(r'./train.csv', header=True)
test_csv = test.to_csv(r'./test.csv', header=True)