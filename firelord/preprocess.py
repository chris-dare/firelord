"""The :mod:`firelord.preprocess` module contains functions to preprocess 
burn area data.
"""
# Author: Christopher Dare

from typing import Optional

from firelord.data import load_burn_area_data

import pandas as pd
from joblib import Memory


def get_training_dataset():
    burn_area_stats = load_burn_area_data(category="train").dropna()
    burn_area_stats["date"] = pd.to_datetime(
        burn_area_stats["ID"].apply(lambda x: x.split("_")[1])
    )
    burn_area_stats["month"] = burn_area_stats.date.dt.month
    burn_area_stats["year"] = burn_area_stats.date.dt.year
    return burn_area_stats
