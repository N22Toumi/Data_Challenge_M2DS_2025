import rampwf as rw

import pandas as pd
from pathlib import Path
from sklearn.model_selection import TimeSeriesSplit

problem_title = 'Template RAMP kit to create data challenges'

# _prediction_label_names = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# # A type (class) which will be used to create wrapper objects for y_pred
# Predictions = rw.prediction_types.make_multiclass(
#     label_names=_prediction_label_names
# )

Predictions = rw.prediction_types.make_regression()

# An object implementing the workflow
workflow = rw.workflows.Estimator()

score_types = [
    rw.score_types.RMSE(name='rmse', precision=4),  # A modifier
]


# def get_cv(X, y):
#     print('get_cv')
#     cv = StratifiedShuffleSplit(n_splits=8, test_size=0.2, random_state=57)
#     return cv.split(X, y)


def get_cv(X, y):
    n_samples = len(X)
    test_size = int(0.2 * n_samples)
    cv = TimeSeriesSplit(n_splits=5)
    return cv.split(X, y)


def load_data(path='.', file='X_train.csv'):
    path = Path(path) / "data"
    X_df = pd.read_csv(path / file, index_col='date')

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
