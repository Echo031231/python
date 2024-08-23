# 列表的切片---用于获得列表的一个片段


# <列表或列表变量>[N:M]---不包括M
# <列表或列表变量>[N:M:K]

# []表示区间需要使用(:)
# []表示枚举需要使用(,)

ls = [1010, "1010", [1010, "1010"], 1010]
print(ls[1:4])

# 负索引
# 负号 - 在序列操作（如切片和索引）中表示从序列的末尾开始计算位置
print(ls[-1:-3]) # N > M 情况
print(ls[-3:-1]) 

# 设置步长
print(ls[0:4:2])

