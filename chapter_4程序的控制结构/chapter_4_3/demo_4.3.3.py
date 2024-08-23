# 循环控制 break 和 continue

# break结束当前层次的整个循环
# continue语句只结束本次循环


# break语句
'''
# 只有一层循环

while True:
    s = input("请输入一个名字(按Q退出):")
    if s == "Q":   # !!!if后面跟条件没有括号!!!
        break
    print("输入的名字是:",s)
print("程序退出")
# 当你调用 print() 函数时，它会将这些参数按照顺序打印出来，并且在它们之间自动添加一个空格
# 如果你想要将 s 变量的值连接到字符串中，并且不希望在它们之间有空格，你可以使用 + 操作符来实现

'''


'''
# 有两层或多层循环
# 退出内层循环
while True:
    s = input("请输入一个名字(按Q退出):")
    if s == "Q":   
        break      #退出while循环
    for c in s:
        if c == "E":
            break  #退出for循环,但不退出while循环
        print(c, end="")  #不换行
    print()  
print("程序退出")

'''



# continue语句

'''
for s in "PYTHON":
    if s == "Y" or s == "y":
        continue
    print(s, end="")

'''

