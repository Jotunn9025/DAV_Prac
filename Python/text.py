
text = """
My name is supercalifragilisticexpialidocious. I am a data scientist. I love data science! It is absolutely amazing and helpful.
I am not having fun. This is a sad time.
This is a neutral statement. It is just a fact.
What a wonderful day! I am so happy to be learning data science.
Fish are swimming in the ocean. The sky is blue. The grass is green.
Fishes are swimming in the ocean. The sky is blue. The grass is green.
Food is delicious. I am enjoying my meal.
I am feeling terrible. This is the worst day ever.
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