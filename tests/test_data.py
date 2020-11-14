import pandas as pd

from firelord.data import load_burn_area_data


def test_load_burn_area_data():
    categories = ["train", "test"]
    for category in categories:
        burn_stats = load_burn_area_data(category)
        assert type(burn_stats) == pd.DataFrame
