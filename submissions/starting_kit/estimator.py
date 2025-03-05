
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression


def get_estimator():
    pipe = make_pipeline(
        StandardScaler(),
        LinearRegression()
    )

    return pipe
