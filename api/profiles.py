"""The :mod:`api.Landprofile` module provides functions data classes for modelling land profiles
"""
# Author: Christopher Dare
from pydantic import BaseModel


class LandProfile(BaseModel):

    climate_vs: float
    climate_def: float
    climate_vap: float
    climate_aet: float
    precipitation: float
    landcover_5: float