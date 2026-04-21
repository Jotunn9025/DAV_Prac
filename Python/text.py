
text = """
NixOS is a Linux distribution based on the Nix package manager. It uses a 
declarative configuration and allows reliable system upgrades. While the 
learning curve can be steep, the ability to reproduce a system perfectly 
across different machines is an absolute game-changer for developers. 
I love how it handles dependencies without version conflicts!
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