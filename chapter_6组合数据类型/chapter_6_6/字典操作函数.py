

# ### 字典的操作函数（通常不作为字典对象的方法）：

# | 函数       | 描述                                      | 示例                                     |
# |------------|-----------------------------------------|----------------------------------------|
# | `len()`    | 返回字典中键值对的数量                    | `len(my_dict)`                          |
# | `dict()`   | 创建一个新的字典                         | `new_dict = dict(a=1, b=2)`             |
# | `sorted()` | 对字典的键进行排序                       | `sorted(my_dict.keys())`                |
# | `list()`   | 从字典的键或值中创建列表                  | `list(my_dict.keys())`                  |
# | `min()`    | 返回字典的键或值中的最小值                | `min(my_dict.keys())`                   |
# | `max()`    | 返回字典的键或值中的最大值                | `max(my_dict.values())`                 |


# ### 说明：
# - `min()` 和 `max()` 函数可以用来获取字典中键或值的最小值和最大值。需要注意的是，这些函数处理的是字典的键或值集合，而不是字典本身。



# ### 字典的方法（作为字典对象的内建方法）：

# | 方法         | 描述                                      | 示例                                       |
# |--------------|-----------------------------------------|------------------------------------------|
# | `get()`      | 获取指定键的值，如果键不存在则返回默认值 | `my_dict.get('key', 'default')`           |
# | `pop()`      | 移除指定键并返回其对应的值                | `my_dict.pop('key')`                      |
# | `popitem()`  | 移除并返回字典中的最后一对键值对          | `my_dict.popitem()`                       |
# | `items()`    | 返回字典中所有键值对的视图                | `my_dict.items()`                         |
# | `keys()`     | 返回字典中所有键的视图                   | `my_dict.keys()`                          |
# | `values()`   | 返回字典中所有值的视图                   | `my_dict.values()`                        |
# | `update()`   | 更新字典，将另一个字典或键值对添加到当前字典中 | `my_dict.update({'new_key': 'new_value'})`|
# | `setdefault()` | 如果键不存在，则将键值对添加到字典中，并返回该值 | `my_dict.setdefault('key', 'default')`   |
# | `clear()`    | 删除字典中的所有键值对                   | `my_dict.clear()`                         |
# | `copy()`     | 返回字典的一个浅拷贝                      | `new_dict = my_dict.copy()`               |
# | `fromkeys()` | 创建一个新字典，以指定的键和一个可选的初始值 | `dict.fromkeys(['a', 'b'], 0)`           |
# | `__contains__()` | 检查字典是否包含指定的键                | `'key' in my_dict`                       |




