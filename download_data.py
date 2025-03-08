"""
from pathlib import Path
import os
import pandas as pd
# from sklearn.datasets import load_digits
# from sklearn.model_selection import train_test_split

DATA_PATH = Path('data')


if __name__ == '__main__':
    if not DATA_PATH.exists():
        DATA_PATH.mkdir()

    # Load the data
    print('Loading the data...', end='', flush=True)

    X_df = pd.read_csv(os.path.join(DATA_PATH, 'energydata_complete.csv'),
                       index_col='date')
    X_df.index = pd.to_datetime(X_df.index)
    last_month = X_df.index.to_period("M").unique()[-1]
    private_test_set = X_df[X_df.index.to_period("M") == last_month]
    training_set = X_df[X_df.index.to_period("M") != last_month]

    # Save the data
    training_set.to_csv(DATA_PATH / 'X_train.csv', index=True)
    private_test_set.to_csv(DATA_PATH / 'X_test.csv', index=True)
    print('done')
"""
from pathlib import Path
import os
import pandas as pd

DATA_PATH = Path('data')
PUBLIC_PATH = DATA_PATH / 'public'

if __name__ == '__main__':
    # Create directories if not exist
    DATA_PATH.mkdir(exist_ok=True)
    PUBLIC_PATH.mkdir(exist_ok=True)

    # Load the initial dataset
    print('Loading the initial dataset...', end='', flush=True)
    X_df = pd.read_csv(DATA_PATH / 'energydata_complete.csv', index_col='date')
    X_df.index = pd.to_datetime(X_df.index)

    # Split initial data into train and private test
    last_month = X_df.index.to_period("M").unique()[-1]
    private_test_set = X_df[X_df.index.to_period("M") == last_month]
    training_set = X_df[X_df.index.to_period("M") != last_month]

    # Save initial split data
    training_set.to_csv(DATA_PATH / 'X_train.csv', index=True)
    private_test_set.to_csv(DATA_PATH / 'X_test.csv', index=True)
    print('Initial split done.')

    # Now, create a public split from X_train.csv
    print('Creating public split...', end='', flush=True)
    X_train_df = pd.read_csv(DATA_PATH / 'X_train.csv', index_col='date')
    X_train_df.index = pd.to_datetime(X_train_df.index)

    last_month_public = X_train_df.index.to_period("M").unique()[-1]
    public_test_set = X_train_df[X_train_df.index.to_period("M") == last_month_public]
    public_training_set = X_train_df[X_train_df.index.to_period("M") != last_month_public]

    # Save the public split data
    public_training_set.to_csv(PUBLIC_PATH / 'X_train.csv', index=True)
    public_test_set.to_csv(PUBLIC_PATH / 'X_test.csv', index=True)
    print('Public split done.')
