from pathlib import Path

import pandas as pd
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

DATA_PATH = Path('data')


if __name__ == '__main__':
    if not DATA_PATH.exists():
        DATA_PATH.mkdir()

    print('Loading the data...', end='', flush=True)
    data = pd.read_csv(DATA_PATH / 'energydata_complete.csv')
    X_df = data.drop(columns=['Appliances'])
    y = data['Appliances']

    X_train, X_test = train_test_split( # A modifier
        X_df, test_size=0.2, random_state=57, shuffle=False
    )

    # Save the data
    X_train.to_csv(DATA_PATH / 'X_train.csv', index=False)
    X_test.to_csv(DATA_PATH / 'X_test.csv', index=False)
    print('done')
