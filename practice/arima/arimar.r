library(ggplot2)
library(dplyr)
library(forecast)

data <- read.csv('airline-passengers.csv')
series <- ts(data$Passengers, c(1949,1), freq=12)

model <- auto.arima(series)
model

fc <- forecast(model,h=12)
autoplot(fc)