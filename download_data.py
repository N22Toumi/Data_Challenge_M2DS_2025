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

    X_df = pd.read_csv(os.path.join(DATA_PATH, 'energydata_complete.csv'), index_col='date')
    X_df.index = pd.to_datetime(X_df.index)
    last_month = X_df.index.to_period("M").unique()[-1]
    private_test_set = X_df[X_df.index.to_period("M") == last_month]
    training_set = X_df[X_df.index.to_period("M") != last_month]

    # Save the data
    training_set.to_csv(DATA_PATH / 'X_train.csv', index=True)
    private_test_set.to_csv(DATA_PATH / 'X_test.csv', index=True)
    print('done')
