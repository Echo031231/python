# 猜数字游戏

import random
target = random.randint(1, 1000) # 1-1000
count = 0

while True:
    try:
        guess = eval(input("请输入一个整数:")) # 用户猜的数字
    except:
        print("输入有误,请重试,不计入猜测次数！")
        continue # 跳出本轮循环
    count += 1
    if guess > target:
        print("猜大了")
    elif guess < target:
        print("猜小了")
    else:
        print("猜对了")
        break   # 跳出while循环   
print("此轮的猜测次数是:{}".format(count))
print("进程结束")












