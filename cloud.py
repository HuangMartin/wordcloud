from tabnanny import process_tokens
import tweepy
import numpy as np
import configparser
import pandas as pd
import matplotlib.pylab as plt
from wordcloud import STOPWORDS, ImageColorGenerator, WordCloud
from PIL import Image
import wordcloud

#load file
text = open('tweets.csv', 'r', encoding='utf-8', errors='ignore').read()
#斷句＆一些推文常出現的字眼過濾
stopwords = set(STOPWORDS)
stopwords.add("RT")
stopwords.add("t")
stopwords.add("co")
stopwords.add("will")
stopwords.add("https")
stopwords.add("Tesla")
stopwords.add("elonmusk")

#wordcloud set
mask = np.array(Image.open('elonmusk.jpg'))#set jpg or png
wc = WordCloud(background_color = 'white',
                max_words = 1000,
                width = 350,
                height = 350,
                margin = 1,
                stopwords = stopwords,
                mask = mask,
                contour_width = 4,
                contour_color = 'black'
                )

wc.generate(text)
image_colors = ImageColorGenerator(mask)
wc.recolor(color_func = image_colors)

plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()

#將結果令存在資料夾中
wc.to_file('elonmusk_wordcloud.png')