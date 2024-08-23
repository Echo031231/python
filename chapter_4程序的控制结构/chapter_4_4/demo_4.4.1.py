# 程序的异常处理
'''
try:
    <语句块1>
except:
    <语句块1>
'''

# 将字符串当作 Python 表达式进行求值并返回结果------eval()函数



# 处理输入错误
'''
try:
    n = eval(input("请输入一个数字:"))
    print("输入数字的3次方值为:", n**3)
except:
    print("输入错误,请输入一个数字!")

'''


'''
# 处理程序执行中的运行异常
try:
    for i in range(5): # 0-4
        print(10/i, end="")
except:
    print("某种原因,出错了")

'''








