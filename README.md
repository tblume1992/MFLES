# MFLES
A Specific implementation from ThymeBoost written with the help of Numba.

Here is a quick Introduction:


Here is a quick benchmark vs AutoETS from M4:
![alt text](https://github.com/tblume1992/MFLES/blob/main/static/mfles_benchmark.PNG?raw=true "benchmark")
## Quick Start:
Install via pip
```
pip install MFLES
```

Import MFLES class
```
from MFLES.Forecaster import MFLES
```
Import data
```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r'https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv')
```
Fit and predict!
```
mfles = MFLES()
fitted = mfles.fit(df['Passengers'].values, seasonal_period=12)
predicted = mfles.predict(12)

plt.plot(np.append(fitted, predicted))
plt.plot(df['Passengers'].values)
plt.show()
```
![alt text](https://github.com/tblume1992/MFLES/blob/main/static/mfles_example.png?raw=true "example")
