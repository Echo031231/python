# 比赛结束条件函数
# def gameOver(a, b):
#     return a == 15 or b == 15

# print(gameOver(15, 14))






# # <img src="http://www.dili360.com/public/images/search_btn.png"/>

# line = '<img src="http://www.dili360.com/public/images/search_btn.png"/>'
# if 'img' in line:
#     url = line.split('src=')[-1].split('"')[1]
#     print(url)



# 读取保存在本地的html文件

f = open('nationalgeographic.html', "r", encoding='utf-8')
ls = f.readlines()
f.close()
print(ls)
    


# # 解析并提取其中的图片链接
# def extractImageUrls(htmllist):
#     urls = []
#     for line in htmllist:
#         if 'img' in line:
#             url = line.split('src=')[-1].split('"')[1] # []表示提取(分割成为的列表)中第几个元素
#             if 'http' in url:
#                 urls.append(url)
#     return urls



