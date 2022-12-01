import fastf1 as ff1
import pandas as pd
import numpy as np
import requests
import random
import seaborn as sns
import json

from typing import Any

from fastf1 import plotting, utils
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure


# Enable caching by providing the path of the cache directory
def enable_cache() -> None:
    # TODO: test if cache directory exists
    try:
        ff1.Cache.enable_cache("cache/")
        CACHE_ENABLED = True
    except:
        print("Could not enable Cache")


def get_fastest_lap(driver: str, session_info: tuple[int, str, str]) -> Any:
    enable_cache()

    y, gp, s = session_info
    session = ff1.get_session(y, gp, s)
    session.load()
    fs = session.laps.pick_driver(driver).pick_fastest()

    return fs
