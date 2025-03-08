
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR


def get_estimator():
    pipe = make_pipeline(
        StandardScaler(),
        SVR()
    )

    return pipe
