library(forecast)
library(ggplot2)

data <- read.csv("airline-passengers.csv")
series <- ts(data, c(1949, 1), frequency = 12)

decomp <- decompose(series, type = "multiplicative")
plot(decomp)