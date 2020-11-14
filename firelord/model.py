"""The :mod:`consignment.model` module contains a Dataset class and 
a function to train an instance of the predictive model used in this application.
"""
# Author: Chris Dare
from pathlib import Path
from typing import Optional, List

import LGBMRegressor, XGBRegressor
from sklearn.ensemble import RandomForestRegressor, VotingRegressor
from sklearn.linear_model import RidgeCV
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV

from firelord.preprocess import get_training_dataset

MODEL_STORE = Path(__file__).parent.absolute() / ".store"
MODEL_STORE.mkdir(exist_ok=True)
RANDOM_SEED = 42  # for reproducibility
default_features = [
    "climate_vs",
    "climate_def",
    "climate_vap",
    "climate_aet",
    "precipitation",
    "landcover_5",
]


class Dataset:
    """Dataset used to train the application's predictive model.

    The instance of this class contains data to train the model as well as data to evaluate its performance.
    This is initiated in a reproducible manner.


    Parameters
    ----------
    separating_date: str, default=None
        The end of the training date range and beginning of the validation date. 

    end_date: str
        The end of the date range for the data required

    test_size:
        the percentage of data that should be reserved as unseen data for evaluating a model trained on the Dataset instance  

    random_state: 
        random_state to ensure reproducibility when splitting the dataset

    Example
    ----------
    >>> From firelord.model import Dataset
    >>> dataset = (
    ...     separating_date = '2013-01-01',
    ...     test_size = 0.25,
    ...     random_state = 42,
    ... )
    >>> 


    """

    def __init__(
        self,
        separating_date: str,
        test_size: float = 0.33,
        random_state: int = RANDOM_SEED,
    ):

        self.df = get_training_dataset()
        self.train = self.df.loc[self.df.date < separating_date]
        self.validation = self.df.loc[self.df.date > separating_date]

        # self.X_train, self.X_eval, self.y_train, self.y_eval = train_test_split(
        #     self.df.drop(columns=[]),
        #     self.df.strike,
        #     test_size=test_size,
        #     stratify=self.df.strike,
        #     random_state=random_state,
        # )


## Hyper Paramter fine tuning


def hyperParameterTuning(X_train, y_train, xgb_model):
    param_tuning = {
        "max_depth": [4, 5],
        "colsample_bytree": [0.2, 0.3],
        "n_estimators": [200, 300, 400],
        "objective": ["reg:squarederror"],
    }

    gsearch = GridSearchCV(
        estimator=xgb_model, param_grid=param_tuning, cv=5, n_jobs=-1, verbose=1
    )

    gsearch.fit(X_train, y_train)

    return gsearch.best_params_


def train(features: List[str]):
    in_cols = [
        "climate_vs",
        "climate_def",
        "climate_vap",
        "climate_aet",
        "precipitation",
        "landcover_5",
    ]
    target_col = "burn_area"
    date_split = "2013-01-01"
    train_all = get_training_dataset()
    train_ = train_all.loc[train_all.date < date_split]
    valid_ = train_all.loc[train_all.date > date_split]

    X_train, y_train = train_[in_cols], train_[target_col]
    X_valid, y_valid = valid_[in_cols], valid_[target_col]

    xgb_model = xgb.XGBRegressor(n_estimators=300, max_depth=3, colsample_bytree=0.5, objective='reg:squarederror')
    
    xgb_model.fit(X_train, y_train)

    # cat_model=CatBoostRegressor(iterations=300, depth=5, learning_rate=0.1, loss_function='RMSE')
    # cat_model.fit(X_train, y_train,eval_set=(X_valid, y_valid),plot=True)

    lgb_model = lgb.LGBMRegressor(n_estimators=100, max_depth=8, num_leaves=6, objective="regression")
    lgb_model.fit(X_train, y_train)

    # voting_regressor = VotingRegressor([('xgb', xgb_model), ('cat', cat_model), ('lgb', lgb_model)])
    voting_regressor = VotingRegressor([('xgb', xgb_model), ('lgb', lgb_model)])
    voting_regressor.fit(X_train, y_train)

    return voting_regressor

    
