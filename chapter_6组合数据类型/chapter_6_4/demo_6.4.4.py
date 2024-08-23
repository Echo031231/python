# 元组数据类型---序列类型


# <class 'tuple'>
t = (1, 2, 3)
print(type(t))

for i in (1, 2, 3):
    print(i, end="月")
print() # 控制换行

def f(x):
    return x , x+1, x+2
# 返回一个元组数据类型
print(type(f(1)))





