# Web 页面元素提取:


def main():
    inputfile = "nationalgeographic.html"
    outputfile = "nationalgeographic-urls.txt"

    # 读取保存在本地的html文件
    htmlLines = getHTMLlines(inputfile)
    # 解析并提取其中的图片链接
    imageUrls = extractImageUrls(htmlLines)
    # 输出提取结果到屏幕
    showResult(imageUrls)
    # 保存提取的结果为文件
    saveResult(outputfile, imageUrls)



# 读取保存在本地的html文件
def getHTMLlines(htmlpath):
    f = open(htmlpath, "r", encoding='utf-8')
    ls = f.readlines()
    f.close()
    return ls


# 解析并提取其中的图片链接
def extractImageUrls(htmllist):
    urls = []
    for line in htmllist:
        if 'img' in line:
            url = line.split('src=')[-1].split('"')  # []表示提取(分割成为的列表)中第几个元素
            
            if len(url) == 1:
                url = url[0]
            else:
                url = url[1]
                
            if 'http' in url:
                urls.append(url)
    return urls


# 输出提取结果到屏幕
def showResult(urls):
    count = 0
    for url in urls:
        print("第{:2}个URL:{}".format(count, url))
        count += 1


# 保存提取的结果为文件
def saveResult(filepath, urls):
    f = open(filepath, "w")
    for url in urls:
        f.write(url + "\n")
    f.close()


main()