library(ggplot2)
library(dplyr)
df <- read.csv("titanic.csv", header=T)
colSums(is.na(df))
df$Age <- mean(df$Age, na.rm=T)
df$Cabin <- ifelse(is.na(df$Cabin)|df$Cabin=="",0,1)
df$Sex <- recode(df$Sex,
        "male"=1,
        "female"=0)
head(df)

index <- sample(1:nrow(df),0.8*nrow(df))
train <- df[index,]
test <- df[-index,]


model <- glm(Survived ~ Pclass+Sex+Age+Cabin+Fare,data=train,family="binomial")
y_prob <- predict(model,test,type = "response")
y_pred <- ifelse(y_prob > 0.5, 1, 0)
accuracy <- mean(as.numeric(as.character(test$Survived))==y_pred)
accuracy

cm <- table(Predicted = y_pred, Actual = as.numeric(as.character(test$Survived)))
cm
df_cm <- as.data.frame(cm)
df_cm$Percent <- df_cm$Freq/sum(df_cm$Freq)
ggplot(df_cm,aes(x=Actual, y=Predicted,fill=Percent))+
    geom_tile()+
    geom_text(aes(label=Freq),color="white",size=5)+
    scale_fill_gradient(low="blue",high="red")