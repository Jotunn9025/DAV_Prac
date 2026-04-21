library(ggplot2)
library(forecast)
df <- read.csv("airline-passengers.csv")
ts_data <- ts(df$Passengers, start = c(1949, 1), frequency = 12)
ts_data
plot(ts_data,
     main = "AirPassengers Time Series",
     ylab = "Passengers",
     xlab = "Time")

model <- auto.arima(ts_data)
summary(model)


fc <- forecast(model, h = 12)

plot(fc)