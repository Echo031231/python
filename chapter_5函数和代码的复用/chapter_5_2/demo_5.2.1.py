# 可选参数传递

'''
def <函数名> (<非可选参数列表>, <可选参数> = <默认值>)
    <函数体>
    return<返回值列表>

'''


# 可选参数(有默认值)一般放在非可选参数后面
def multiply(x, y = 10):
    print(x + y)

multiply(2)
multiply(4, 5)





