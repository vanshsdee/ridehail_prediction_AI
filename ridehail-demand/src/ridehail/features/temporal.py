"""Temporal feature engineering: hour-of-day, day-of-week, holidays, etc."""
import numpy as np
import pandas as pd

def add_calendar_features(df: pd.DataFrame, time_col: str) -> pd.DataFrame:
    t = pd.to_datetime(df[time_col])
    df = df.copy()
    df["hour"] = t.dt.hour
    df["dow"] = t.dt.dayofweek
    df["is_weekend"] = (df["dow"] >= 5).astype(int)
    df["hour_sin"] = np.sin(2 * np.pi * df["hour"] / 24)
    df["hour_cos"] = np.cos(2 * np.pi * df["hour"] / 24)
    return df
