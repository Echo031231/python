# 《红楼梦》人物出场统计:
import jieba

# 排除词库:
excludes = {"什么", "一个", "我们", "那里", "你们", "如今",
            "说道", "知道", "老太太", "起来", "姑娘", "这里",
            "出来", "他们", "众人", "自己", "一面", "太太",
            "只见", "怎么", "奶奶", "两个", "没有", "不是",
            "不知", "这个", "听见"}
# print(type(excludes)) # 集合的类型


# 读取文本:
f = open("红楼梦.txt", "r",  encoding='utf-8')
txt = f.read()
f.close()
# print(txt)


# jieba库精准分词  and 统计词频:
counts = {}
ls = jieba.lcut(txt)
# print(ls)
for i in ls:
    if len(i) == 1:
        continue
    else:
        counts[i] = counts.get(i, 0) + 1
# print(counts)

# 删除字典counts中excludes中内容:
for word in excludes:
    del counts[word]


# 获取items列表并且排序
items = list(counts.items()) # 列表
items.sort(key=lambda x:x[1], reverse=True)
# sort() 方法会在原地对列表进行排序，没有返回值（返回 None）。
# 提取元组的第二个元素用于排序
# 列表按降序排列



# 格式化打印输出:
for i in range(5):
    word, count = items[i]
    print("{0:<10} {1:>5}".format(word, count))




















