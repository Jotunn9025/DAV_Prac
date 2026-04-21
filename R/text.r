library(tm)
library(wordcloud2)
library(htmlwidgets)

raw_text <- "Data science is amazing. Data science uses data to find data insights. I am enjoying my time in this practical exam preparation. Data science is the future!. This is so much fun. I am enjoying myself"

docs <- Corpus(VectorSource(raw_text))
docs <- tm_map(docs, content_transformer(tolower))
docs <- tm_map(docs, removePunctuation)
docs <- tm_map(docs, removeNumbers)
docs <- tm_map(docs, removeWords, stopwords("english")) 
docs <- tm_map(docs, stripWhitespace)

dtm <- TermDocumentMatrix(docs)
matrix <- as.matrix(dtm)
words <- sort(rowSums(matrix), decreasing = TRUE)
df <- data.frame(word = names(words), freq = words)

hw <- wordcloud2(df, size = 0.7, color = "random-light", backgroundColor = "black")
saveWidget(hw, "wordcloud.html", selfcontained = F)
