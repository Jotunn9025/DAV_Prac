import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

df = pd.read_csv("airline-passengers.csv", parse_dates=['Month'], index_col='Month')
series = df['Passengers']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
plot_acf(series, ax=ax1)
plot_pacf(series, ax=ax2)
plt.show()

model = ARIMA(series, order=(15, 1, 4))
model_fit = model.fit()

forecast_steps = 24
forecast = model_fit.get_forecast(steps=forecast_steps)
forecast_idx = pd.date_range(series.index[-1], periods=forecast_steps + 1, freq='MS')[1:]

plt.figure(figsize=(10, 6))
plt.plot(series, label='Actual')
plt.plot(forecast_idx, forecast.predicted_mean, color='red', label='Forecast')
plt.title("Air Passengers Manual ARIMA Forecast")
plt.legend()
plt.show()

print(model_fit.summary())