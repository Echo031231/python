# 函数的返回值

'''
# 一个或多个返回值
def multiply (x , y = 10):
    return x + y , x * y
s = multiply(5, 6)
print(s)
a , b = multiply(5, 6)
print(a)
print(b)

'''

# 当函数存在多种结束条件时，将使用多个return语句
def manyret(x):
    try:
        if x > 0:
            return x + 1
        else:
            return x - 1
    except:
        return 0

print(manyret("python"))



