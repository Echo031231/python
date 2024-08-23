# 函数的使用
'''
# 定义一个求阶乘的函数
def fact(n):
    s = 1
    for i in range(1, n+1):
        s *= i
    return s

# 调用整数阶乘的函数
print(fact(100))
print(fact(64))
'''

# 函数的类型

'''
def f(x):
    return x+1
print(type(f)) # 函数类型
print(type(f(2))) # 返回值类型

'''

# python最小函数

'''
# 对f()的调用不实现任何功能
def f():
    pass # 保留字(用来占位)
    
'''
