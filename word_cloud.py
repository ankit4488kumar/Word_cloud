import sys
import numpy as np
from PIL import Image
import wikipedia
from wordcloud import WordCloud,STOPWORDS



x = str(input("Enter the title :"))
title = wikipedia.search(x)[0]
page = wikipedia.page(title)
text = page.content
print(text)
background = np.array(Image.open("/home/akki/Desktop/word_cloud/cloud.png")
stopwords = set(STOPWORDS)
wc = WordCloud(background_color = 'white',
               max_words = 200
               mask = background
               stopwords = stopwords)

wc.gererate(text)
wc.to_file('/home/akki/Desktop/word_cloud/1.png')
