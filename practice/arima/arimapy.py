from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_pacf,plot_acf
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("airline-passengers.csv",parse_dates=["Month"], index_col="Month")

series=df["Passengers"]
plot_pacf(series)
plot_acf(series)
plt.show()

model=ARIMA(series,order=(1,1,1))
model_fit=model.fit()

forecast_steps=24
forecast_idx=pd.date_range(series.index[-1],periods=forecast_steps+1,freq="MS")[1:]
forecast=model_fit.get_forecast(steps=forecast_steps)

plt.plot(series,label="ACTUAL")
plt.plot(forecast_idx, forecast.predicted_mean,label="Pred",color="red")
plt.legend()
plt.show()
