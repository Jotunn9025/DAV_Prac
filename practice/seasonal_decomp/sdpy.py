import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

df=pd.read_csv('airline-passengers.csv',parse_dates=['Month'],index_col='Month')
res=seasonal_decompose(df['Passengers'],model='multiplicative',period=12)
res.plot()
plt.show()