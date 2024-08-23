# wordcloud实例:
from wordcloud import WordCloud
from PIL import Image
import numpy as np

mask = Image.open('AliceMask.png')
mask_arrary = np.array(mask)

f = open('AliceInWonderland.txt', 'r', encoding='utf-8')
txt = f.read()

wordcloud = WordCloud(background_color="white",
                      width=800,
                      height=600,
                      max_words=200,
                      max_font_size=80,
                      mask=mask_arrary
                      ).generate(txt)

wordcloud.to_file('Alice实例词云图片.png')


