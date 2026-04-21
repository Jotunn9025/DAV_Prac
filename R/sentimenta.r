library(syuzhet)

text <- "I am not having fun. This is a sad time."
score <- get_sentiment(text, method = "syuzhet")

print(score)
