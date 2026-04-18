"""Forecasting metrics."""
import numpy as np

def mae(y_true, y_pred): return float(np.mean(np.abs(y_true - y_pred)))
def rmse(y_true, y_pred): return float(np.sqrt(np.mean((y_true - y_pred) ** 2)))
def mape(y_true, y_pred, eps=1e-6):
    return float(np.mean(np.abs((y_true - y_pred) / (np.abs(y_true) + eps))) * 100)
