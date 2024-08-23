# 《红楼梦》人物出场统计词云输出:
import jieba
from wordcloud import WordCloud

# 排除词库:
excludes = {"什么", "一个", "我们", "那里", "你们", "如今",
            "说道", "知道", "老太太", "起来", "姑娘", "这里",
            "出来", "他们", "众人", "自己", "一面", "太太",
            "只见", "怎么", "奶奶", "两个", "没有", "不是",
            "不知", "这个", "听见"}


# 读取文本:
f = open("红楼梦.txt", "r",  encoding='utf-8')
txt = f.read()
f.close()

words = jieba.lcut(txt)
newtxt = " ".join(words) # 输入一个序列(通常为列表)返回一个字符串

wordcloud = WordCloud(background_color="black",
                      width=800,
                      height=600,
                      font_path="E:\python\msyh.ttc",
                      max_words=200,
                      max_font_size=80,
                      stopwords=excludes,
                      ).generate(newtxt)

wordcloud.to_file("红楼梦基本词云.png")









