# 变量的作用域

'''
# 局部变量(函数内部定义并使用的变量)
def multiply(x, y = 10):
    z = x * y
    return z

s = multiply(2, 50)
print(s)

'''

'''
# 全局变量(函数之外定义的变量)
#函数内部使用全局变量时,需要使用 global <全局变量> 在函数中申明
n = 2
def multiply(x, y = 10):
    global n 
    return x * y * n

s = multiply(4, 90)
print(s)

'''

'''
# 对比----global <全局变量>
n = 2   # 全局变量
def multiply(x, y = 10):
    n = x * y
    return n # 此处的n不是全局变量

s = multiply(4, 90)
print(s)

print(n) # 不改变外部全局变量的值

'''


