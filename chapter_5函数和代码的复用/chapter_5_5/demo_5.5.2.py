# 递归构建

# 阶乘的计算函数
'''
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
    
num = eval(input("请输入一个整数:"))
print(fact(abs(int(num)))) # 非负整数

'''



'''
# 字符串的翻转函数

def reverse(s):
    if s == "":
        return s
    else:
        return reverse(s[1:]) + s[0]

str = input("请输入一个字符串:")
print(reverse(str))

'''







