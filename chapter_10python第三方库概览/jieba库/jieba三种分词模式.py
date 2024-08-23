# `jieba`库有三种分词模式：

# 1. **精确模式**：试图将句子精确地切分成词，适合用于文本分析。
# 代码示例：
'''
   import jieba
   text = "我喜欢学习自然语言处理"
   words = jieba.cut(text, cut_all=False)
   print("/ ".join(words))
'''

# 2. **全模式**：把句子中所有可能的词语都找出来，速度非常快，但不能解决歧义。
# 代码示例：
'''
   import jieba
   text = "我喜欢学习自然语言处理"
   words = jieba.cut(text, cut_all=True)
   print("/ ".join(words))
   '''

# 3. **搜索引擎模式**：在精确模式的基础上，对长词再进行切分，适合用于搜索引擎构建倒排索引。
# 代码示例：
'''
   import jieba
   text = "我喜欢学习自然语言处理"
   words = jieba.cut_for_search(text)
   print("/ ".join(words))
   '''

# 这三种模式适用于不同的应用场景，根据需求选择合适的模式。