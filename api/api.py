from typing import Any
from fastapi import FastAPI

from ff1 import f1data

app = FastAPI()


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello from FastAPI!"}


@app.get("/{year}/{gp}/{session}/{driver}")
async def get_fastest_lap(
    year: int, gp: str, session: str, driver: str
) -> dict[Any, Any]:
    session_info = (year, gp, session)

    fs = f1data.get_fastest_lap(driver, session_info)

    driver_name = fs["Driver"]
    driver_number = fs["DriverNumber"]
    driver_team = fs["Team"]

    track_status = fs["TrackStatus"]

    lap_start_date = fs["LapStartDate"]
    lap_start_time = fs["LapStartTime"]

    lap_time = fs["LapTime"]
    lap_number = fs["LapNumber"]

    pitout_time = fs["PitOutTime"]
    pitin_time = fs["PitInTime"]

    sector1_time = fs["Sector1Time"]
    sector2_time = fs["Sector2Time"]
    sector3_time = fs["Sector3Time"]

    sector1_session_time = fs["Sector1SessionTime"]
    sector2_session_time = fs["Sector2SessionTime"]
    sector3_session_time = fs["Sector3SessionTime"]

    speed_i1 = fs["SpeedI1"]
    speed_i2 = fs["SpeedI2"]
    speed_fl = fs["SpeedFL"]
    speed_st = fs["SpeedST"]

    is_personal_best = fs["IsPersonalBest"]

    compound = fs["Compound"]
    tyre_life = fs["TyreLife"]
    fresh_tyre = fs["FreshTyre"]
    stint = fs["Stint"]

    # TODO: treat numpy number types

    return_dict = {
        "driver_name": driver_name,
        "driver_number": driver_number,
        "driver_team": driver_team,
        "track_status": track_status,
        "lap_start_date": lap_start_date,
        "lap_start_time": lap_start_time,
        "lap_time": lap_time,
        # "lap_number": lap_number,
        # "pitout_time": pitout_time,
        # "pitin_time": pitin_time,
        "sector1_time": sector1_time,
        "sector2_time": sector2_time,
        "sector3_time": sector3_time,
        # "sector1_session_time": sector1_session_time,
        # "sector2_session_time": sector2_session_time,
        # "sector3_session_time": sector3_session_time,
        # "speed_i1": speed_i1,
        # "speed_i2": speed_i2,
        # "speed_fl": speed_fl,
        # "speed_st": speed_st,
        # "is_personal_best": is_personal_best,
        "compound": compound,
        "tyre_life": tyre_life,
        "fresh_tyre": fresh_tyre,
        # "stint": stint,
    }

    return return_dict
