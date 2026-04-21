library(ggplot2)
library(dplyr)
library(reshape2)

data <- read.csv("titanic.csv")
data$Cabin <- ifelse(is.na(data$Cabin)|data$Cabin=="",0,1)
data$Age[is.na(data$Age)] <- mean(data$Age, na.rm = TRUE)
data$Sex <- recode (data$Sex,
    "male"=0,
    "female"=1
)
head(data)
index <- sample(1:nrow(data),nrow(data)*0.8)
train <- data[index,]
test <- data[-index,]
model <- glm(Survived~Sex+Age+Cabin+Fare,data=train,family="binomial")
y_prob <-  predict(model,test,type="response")
y_pred <- ifelse(y_prob<0.5,0,1)
accuracy <- mean(y_pred==test$Survived)
accuracy
library(ggplot2)

plot_df <- data.frame(
  Actual = test$Survived,
  Predicted = y_pred
)

ggplot(plot_df, aes(x = factor(Actual), fill = factor(Predicted))) +
  geom_bar(position = "dodge") +
  labs(x = "Actual", fill = "Predicted")