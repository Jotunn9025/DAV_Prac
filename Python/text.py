
text = """
This is not a fun time rn
"""


from wordcloud import WordCloud
import matplotlib.pyplot as plt

wordcloud = WordCloud(width=800, height=400, 
                      background_color='white',
                      colormap='viridis').generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off") 
plt.show()

from transformers import pipeline
sentiment_analyzer = pipeline("sentiment-analysis")
result = sentiment_analyzer(text)
print(result)