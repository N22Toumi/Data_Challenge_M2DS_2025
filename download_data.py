from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

DATA_PATH = Path('data')


if __name__ == '__main__':
    if not DATA_PATH.exists():
        DATA_PATH.mkdir()

    print('Loading the data...', end='', flush=True)
    X_df = pd.read_csv(DATA_PATH / 'energydata_complete.csv')

    X_train, X_test = train_test_split(  # A modifier
        X_df, test_size=0.2, random_state=57, shuffle=False
    )

    # Save the data
    X_train.to_csv(DATA_PATH / 'X_train.csv', index=False)
    X_test.to_csv(DATA_PATH / 'X_test.csv', index=False)
    print('done')
