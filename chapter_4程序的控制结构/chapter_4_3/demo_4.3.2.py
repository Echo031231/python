# 无限循环 while



""" 
while <条件>:
    <语句块>

"""


'''
n = 0
while n < 10:
    print(n)
    n += 3
'''


# 无线循环的扩展模式
""" 
while <条件>:
    <语句块1>
else:
    <语句块2>

"""


'''    
s = "python"
index = 0
print(len(s))
while index < len(s):  # 判断条件为True时执行循环体
    print("循环执行中:"+s[index])
    index += 1
else:
    s = "循环正常结束"
    print(s)
    
 '''






