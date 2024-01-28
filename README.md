# MFLES
<img src="[https://user-images.githubusercontent.com/link-to-your-image.png](https://github.com/tblume1992/MFLES/blob/main/static/mfles_logo.png)" width="200" />

A Specific implementation from ThymeBoost written with the help of Numba.

Here is a quick Introduction and demonstration of methods such as Conformal Prediction Intervals and seasonality decomposition:

https://github.com/tblume1992/MFLES/blob/main/examples/MFLES_Intro.ipynb


Here is a quick benchmark vs AutoETS from M4:
![alt text](https://github.com/tblume1992/MFLES/blob/main/static/mfles_benchmark.PNG?raw=true "benchmark")
## Quick Start:
### Install via pip
```
pip install MFLES
```

### Import MFLES class
```
from MFLES.Forecaster import MFLES
```
### Import data
```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r'https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv')
```
### Fit and predict!
```
mfles = MFLES()
fitted = mfles.fit(df['Passengers'].values, seasonal_period=12)
predicted = mfles.predict(12)

plt.plot(np.append(fitted, predicted))
plt.plot(df['Passengers'].values)
plt.show()
```
![alt text](https://github.com/tblume1992/MFLES/blob/main/static/mfles_example.png?raw=true "example")

### Or Optimize
```
mfles = MFLES()
opt_params = mfles.optimize(df['Passengers'].values,
                          seasonal_period=12,
                          test_size=6,
                          n_steps=3, #number of train/test splits to make
                          step_size=6, #the number of periods to move each step
                          metric='mse' #should support smape, mse, mae, mape
                          )
fitted = mfles.fit(df['Passengers'].values, **opt_params)
predicted = mfles.predict(12)

plt.plot(np.append(fitted, predicted))
plt.plot(df['Passengers'].values)
plt.show()
```
### Fitting from dataframe:
```
from MFLES.Forecaster import fit_from_df

output = fit_from_df(df,
                      forecast_horizon=24,
                      freq='M',
                      seasonal_period=12,
                      id_column='unique_id',
                      time_column='ds',
                      value_column='y',
                      floor=0)
```
### Optimizing from dataframe
```
from MFLES.Forecaster import optimize_from_df

output = optimize_from_df(df,
                          forecast_horizon=4,
                          test_size=4,
                          n_steps=3,
                          step_size=1,
                          metric='mse',
                          seasonal_period=12,
                          freq='M')
```
## Gradient Boosted Time Series Decomposition Theory
The idea is pretty simple, take a process like decomposition and view it as
a type of 'psuedo' gradient boosting since we are passing residuals around
simlar to standard gradient boosting. Then apply gradient boosting approaches
such as iterating with a global mechanism to control the process and introduce
learning rates for each of the components in the process such as trend or
seasonality or exogenous. By doing this we graduate from this 'psuedo' approach
to full blown gradient boosting.

This process allows us to fit pretty exotic models and optimize for each learning
rate to make them jive. Also enables online learning since the framework is made
for residuals. Also opens up changepoint detection using segmentation schemes
although that is out-of-scope of this library.

## Citing
```
@software{
author = {Blume Tyler},
license = {MIT License},
title = {{MFLES}},
url = {https://github.com/tblume1992/MFLES},
version = {0.2.2},
year = {2024}
}
```
