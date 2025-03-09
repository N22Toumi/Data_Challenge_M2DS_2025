import rampwf as rw
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.model_selection import TimeSeriesSplit

problem_title = 'Predicting Energy Consumption in a Building'

Predictions = rw.prediction_types.make_regression()

# An object implementing the workflow
workflow = rw.workflows.Estimator()


class MAE(rw.score_types.BaseScoreType):
    is_lower_the_better = True
    minimum = 0.0
    maximum = float('inf')

    def __init__(self, name='mae', precision=4):
        self.name = name
        self.precision = precision

    def __call__(self, y_true, y_pred):
        mask = y_true != -1
        return np.mean(np.abs((y_true - y_pred)[mask]))


score_types = [
    MAE(name='mean_absolute_error', precision=5),  # A modifier
]


def get_cv(X, y):
    cv = TimeSeriesSplit(n_splits=5)
    return cv.split(X, y)


def load_data(path='.', file='X_train.csv'):
    path = Path(path) / "data"
    X_df = pd.read_csv(path / file, index_col='date')
    X_df.index = pd.to_datetime(X_df.index)

    y = X_df['Appliances']
    X_df = X_df.drop(columns=['Appliances'])

    return X_df, y


# READ DATA
def get_train_data(path='.'):
    file = 'X_train.csv'
    return load_data(path, file)


def get_test_data(path='.'):
    file = 'X_test.csv'
    return load_data(path, file)
