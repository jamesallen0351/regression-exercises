# evaluate.py

import math
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

# plot_residuals(y, yhat): creates a residual plot
def plot_residuals(actual, predicted):
    fig, ax = plt.subplots(figsize=(13, 7))

    ax.hist(df.baseline_residuals, label='baseline residuals', alpha=.6)
    ax.hist(df.residuals, label='model residuals', alpha=.6)
    ax.legend()

# residuals
def residuals(actual, predicted):
    return actual - predicted

# sum of squared errors (SSE)
def sse(actual, predicted):
    return (residuals(actual, predicted) **2).sum()

# mean squared error (MSE)
def mse(actual, predicted):
    n = actual.shape[0]
    return sse(actual, predicted) / n

# root mean squared error (RMSE)
def rmse(actual, predicted):
    return math.sqrt(mse(actual, predicted))

# explained sum of squares (ESS)
def ess(actual, predicted):
    return ((predicted - actual.mean()) ** 2).sum()

# total sum of squares (TSS)
def tss(actual):
    return ((actual - actual.mean()) ** 2).sum()

# r2 score
def r2_score(actual, predicted):
    return ess(actual, predicted) / tss(actual)

# regression_errors(y, yhat): returns the following values
def regression_errors(actual, predicted):
    return pd.Series({
        'sse': sse(actual, predicted),
        'ess': ess(actual, predicted),
        'tss': tss(actual),
        'mse': mse(actual, predicted),
        'rmse': rmse(actual, predicted),
        'r2': r2_score(actual, predicted)
    })

# baseline_mean_errors(y): computes the SSE, MSE, and RMSE for the baseline model
def baseline_mean_errors(actual):
    predicted = actual.mean()
    return {
        'sse': sse(actual, predicted),
        'mse': mse(actual, predicted),
        'rmse': rmse(actual, predicted),
    }

# better_than_baseline(y, yhat): returns true if your model performs better than the baseline, otherwise false
def better_than_baseline(actual, predicted):
    sse_baseline = sse(actual, actual.mean())
    sse_model = sse(actual, predicted)
    return sse_model < sse_baseline
