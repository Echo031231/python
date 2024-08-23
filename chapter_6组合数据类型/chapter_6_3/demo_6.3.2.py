# 集合的操作函数




# 在 Python 集合操作中，方法和函数的具体区别如下：

# 1. **方法（Method）**：是属于某个对象的操作，调用时需要在对象上进行。方法通常用在对象的实例上，例如集合的方法。
   
# 2. **函数（Function）**：是独立于对象的操作，不需要对象的上下文来调用。函数通常是全局的或模块级别的。



# | 类型    | 名称                                   | 说明                                      |
# |---------|--------------------------------------|-----------------------------------------|
# | **方法** | `add(elem)`                         | 添加单个元素到集合中                     |
# | **方法** | `remove(elem)`                      | 移除指定元素，不存在时引发 `KeyError`    |
# | **方法** | `discard(elem)`                     | 移除指定元素，不存在时不报错             |
# | **方法** | `clear()`                           | 移除集合中的所有元素                     |
# | **方法** | `pop()`                             | 随机移除并返回一个元素                   |
# | **方法** | `copy()`                            | 返回集合的浅拷贝                         |
# | **方法** | `update(*others)`                   | 更新集合，添加其他集合中的元素           |
# | **方法** | `intersection_update(*others)`      | 更新集合，保留交集中的元素               |
# | **方法** | `difference_update(*others)`        | 更新集合，移除差集中的元素              |
# | **方法** | `symmetric_difference_update(other_set)` | 更新集合，保留对称差集中的元素      |
# | **函数** | `union(other_set)` 或 `|`          | 返回两个集合的并集                      |
# | **函数** | `intersection(other_set)` 或 `&`   | 返回两个集合的交集                      |
# | **函数** | `difference(other_set)` 或 `-`     | 返回两个集合的差集                      |
# | **函数** | `symmetric_difference(other_set)` 或 `^` | 返回两个集合的对称差集               |
# | **函数** | `issubset(other_set)`              | 判断当前集合是否是另一个集合的子集       |
# | **函数** | `issuperset(other_set)`            | 判断当前集合是否是另一个集合的超集       |

# ### 说明：
# - 方法：前面提到的 `add`、`remove`、`discard`、`clear`、`pop`、`copy`、`update`、`intersection_update`、`difference_update` 和 `symmetric_difference_update` 都是集合的方法。
# - 函数：`union`、`intersection`、`difference`、`symmetric_difference`、`issubset` 和 `issuperset` 是集合运算函数。

# 方法和函数的区分在于，方法是集合对象的操作，而函数通常是用于集合运算的操作。




# 集合主要作用为元素去重
S = set('知之为知之不知为不知')
print(S)

S.add('python')
print(S)

S.discard('为')
print(S)

a = S.pop()
print(a)
print(S)

S1 = set('1234')

S.update(S1)
print(S)

S.remove('1')
print(S)

for i in S:
    print(i, end="")




