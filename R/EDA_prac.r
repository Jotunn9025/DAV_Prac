library(ggplot2)
df <- read.csv("titanic.csv")
head(df)
hist(df$Age,breaks=12,col="blue",border="pink",main="Age Distribution",xlab="Age")
plot(df$Age,df$Fare,col="red",main="Age vs Fare",xlab="Age",ylab="Fare")

ggplot(df, aes(x=Age, y=Fare)) + 
  geom_line(color="red") + 
  labs(title="Age vs Fare", x="Age", y="Fare") +
  theme_minimal()


ggplot(df, aes(x=Age)) + 
  geom_histogram(color="red",fill="blue",bins=5) + 
  labs(title="Age freq hist", x="Age") +
  theme_minimal()


ggplot(df, aes(x=Age, y=Fare)) + 
  geom_point(color="green") + 
  labs(title="Age vs Fare", x="Age", y="Fare") +
  theme_minimal()