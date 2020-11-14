import joblib


def get_model():
    """Return an instance of the latest predictive model
    """
    # the mechanism for retrieving an instance of the model is abstracted...
    # ...to allow for easy integration of updates
    model = joblib.load(".store/ozai_latest.model")
    return model
