# 列表的操作方法


# 以下是常用列表操作方法的表格，详细列出了每个方法的功能和示例：

# | **方法**         | **描述**                            | **示例**                               |
# |------------------|-------------------------------------|----------------------------------------|
# | **`append(x)`**  | 在列表末尾添加一个元素(可以为列表)                | `lst.append(4)` -> `[1, 2, 3, 4]`       |
# | **`extend(iterable)`** | 用可迭代对象扩展列表                | `lst.extend([5, 6])` -> `[1, 2, 3, 5, 6]` |
# | **`insert(i, x)`** | 在指定位置插入一个元素                | `lst.insert(1, 10)` -> `[1, 10, 2, 3]`   |
# | **`remove(x)`**  | 删除列表中第一个匹配的元素            | `lst.remove(2)` -> `[1, 3]`            |
# | **`pop([i])`**   | 删除并返回指定位置的元素              | `lst.pop(1)` -> `3`, `lst` -> `[1, 2]`  |
# | **`clear()`**    | 删除列表中的所有元素                  | `lst.clear()` -> `[]`                   |
# | **`index(x[, start[, end]])`** | 返回第一个匹配元素的索引       | `lst.index(3)` -> `2`                  |
# | **`count(x)`**   | 计算元素出现的次数                    | `lst.count(1)` -> `1`                  |
# | **`sort(key=None, reverse=False)`** | 对列表进行排序                  | `lst.sort()` -> `[1, 2, 3]`            |
# | **`reverse()`**  | 对列表进行反转                        | `lst.reverse()` -> `[3, 2, 1]`         |
# | **`copy()`**     | 返回列表的浅拷贝                      | `lst.copy()` -> `[1, 2, 3]`            |

# ### 说明

# - **`append(x)`**: 在列表末尾添加元素 `x`。
# - **`extend(iterable)`**: 用 `iterable` 中的元素扩展原列表。
# - **`insert(i, x)`**: 在索引 `i` 位置插入元素 `x`。
# - **`remove(x)`**: 删除列表中第一个出现的元素 `x`，如果没有找到元素，会引发 `ValueError`。
# - **`pop([i])`**: 删除并返回指定位置 `i` 的元素，如果未指定位置，则删除并返回列表的最后一个元素。
# - **`clear()`**: 清空列表中的所有元素。
# - **`index(x[, start[, end]])`**: 返回元素 `x` 在列表中的第一个匹配位置，`start` 和 `end` 参数可用来限定搜索范围。
# - **`count(x)`**: 统计元素 `x` 在列表中出现的次数。
# - **`sort(key=None, reverse=False)`**: 对列表进行排序，`key` 用于指定排序的依据，`reverse` 用于指定是否反向排序。
# - **`reverse()`**: 反转列表中的元素顺序。
# - **`copy()`**: 返回列表的浅拷贝，即新列表包含原列表中的元素，但与原列表独立。

# 这个表格涵盖了列表的主要操作方法，希望对你有帮助！






# 下面是一个表格，总结了如何使用 `del` 对列表进行各种操作：

# | **操作**                           | **描述**                                           | **示例代码**                              | **结果**                |
# |------------------------------------|----------------------------------------------------|-------------------------------------------|-------------------------|
# | **删除指定位置的元素**              | 删除列表中指定索引位置的元素                      | `lst = [1, 2, 3, 4, 5]` <br> `del lst[2]` | `[1, 2, 4, 5]`          |
# | **删除指定切片范围的元素**          | 删除列表中指定范围内的多个元素                    | `lst = [1, 2, 3, 4, 5]` <br> `del lst[1:4]` | `[1, 5]`                |
# | **删除列表中的单个元素（使用循环）** | 使用循环删除符合条件的元素（需要确保删除不会导致索引错误） | `lst = [1, 2, 3, 4, 5]` <br> `for i in range(len(lst) - 1, -1, -1): if lst[i] % 2 == 0: del lst[i]` | `[1, 3, 5]`            |
# | **删除整个列表**                   | 删除整个列表，使得该变量不再引用任何列表对象       | `lst = [1, 2, 3, 4, 5]` <br> `del lst`    | `NameError: name 'lst' is not defined` |

# ### 说明

# - **删除指定位置的元素**：通过索引指定要删除的元素。
# - **删除指定切片范围的元素**：通过切片指定范围删除多个元素。
# - **删除列表中的单个元素（使用循环）**：当需要删除符合特定条件的元素时，可以用循环和条件判断来实现。
# - **删除整个列表**：使用 `del` 删除整个列表，这样变量 `lst` 就不再引用任何列表对象了。

# 这些操作允许你灵活地修改和管理列表中的元素。