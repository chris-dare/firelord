"""The :mod:`firelord.data` module contains functions to load the fires dataset.
"""
# Author: Chris Dare

from pathlib import Path
from typing import Optional

import pandas as pd

data_folder_path = Path(__file__).parent.absolute() / ".tmp"
data_files = {
    "train": data_folder_path / "Train.csv",
    "test": data_folder_path / "Test.csv",
}


def load_burn_area_data(category: str):
    burn_statistics = None
    data_file = data_files.get(category)
    if data_file:
        burn_statistics = pd.read_csv(data_file)
    return burn_statistics
