# 异常处理类型

'''
try:
    <语句块1>
except <异常处理类型>:
    <语句块2>
except:
    <语句块3>
'''

try:
    for i in range(5): # 0-4
        print(10/i, end="")
except ZeroDivisionError:
    print("除数不能为0")
except:
    print("某种原因,出错了")


