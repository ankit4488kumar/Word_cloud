import sys
import numpy as np
from PIL import Image
import wikipedia
from wordcloud import WordCloud,STOPWORDS



word = str(input("Enter the title :"))
title = wikipedia.search(word)[0]
page = wikipedia.page(title)
text = page.content
print("Informatiion about the Title",text)

#import a blank black background image
background = np.array(Image.open("/home/akki/Documents/Mini_Projects/word_cloud/cloud.png"))
# for Stopwords
sw = set(STOPWORDS)
# for word cloud
wc = WordCloud(background_color = 'white',
               max_words = 200,
               mask = background,
               stopwords = sw)

wc.generate(text)
wc.to_file('/home/akki/Documents/Mini_Projects/word_cloud/wc_image.png')
