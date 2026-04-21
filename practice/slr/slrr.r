data <- read.csv("rawsal.csv")
data$x <- data$YearsExperience
data$y <- data$Salary
n <- nrow(data)
data$x2  <- data$x^2
data$xy <- data$x * data$y
a1 <- (n*sum(data$xy)-sum(data$x)*sum(data$y))/(( (n*sum(data$x2)) - (sum(data$x))^2))

a0 <- sum(data$y)/n-a1*sum(data$x)/n
plot(data$x,data$y)
lines(data$x,a0+a1*data$x,type="l",col="red")