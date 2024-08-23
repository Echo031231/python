# 函数的定义
'''
def <函数名>(<参数列表>):
    <函数体>
    return<返回值列表>

'''

# n的阶乘计算函数

def fact(n):
    s = 1
    for i in range(1, n+1):
        s *= i
    return s



