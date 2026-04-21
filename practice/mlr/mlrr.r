library(ggplot2)
library(dplyr)

data <- read.csv("sales.csv")
index <- sample(1:nrow(data),0.8*nrow(data))
train <- data[index,]
test <- data[-index,]
dim(train)
dim(test)
model <- lm(sales~TV+radio+newspaper,data=train)
model
y_pred <- predict(model,test)

mse <- mean((test$sales - y_pred)^2)
mse
rmse <- sqrt(mse)
rmse

ggplot(test,aes(x=radio,y=sales))+
    geom_point()+
    geom_smooth(aes(x=radio,y=y_pred),color="red",method="lm")