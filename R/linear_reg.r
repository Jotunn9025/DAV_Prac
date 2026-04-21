library(ggplot2)
library(dplyr)
library(reshape2)
df <-read.csv("sales.csv")
index <- sample(1:nrow(df),0.8*nrow(df))
train <- df[index,]
test <- df[-index,]
model <- lm(sales~ TV+radio+newspaper,data=train)
y_pred <- predict(model,test)
mse <- mean((test$sales-y_pred)^2)
mse
rmse <- sqrt(mse)
rmse
ggplot(test,aes(x=radio, y=sales))+
geom_point(color="blue")+
geom_smooth(method="lm",color="red")
summary(model)

corr <- cor(df)
melt <- melt(corr)
ggplot(melt,aes(x=Var1,y=Var2,fill=value))+
    geom_tile()+
    geom_text(aes(label=round(value,2)),color="white",size=5)+
    scale_fill_gradient(low="blue",high="red")