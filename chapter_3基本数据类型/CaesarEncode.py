# | `chr()`    | 将整数转换为对应的字符                 | `chr(65)` -> `'A'`           |
# | `ord()`    | 将字符转换为对应的整数                 | `ord('A')` -> `65`           |

ptxt = input("请输入明文文本:")

for p in ptxt:
    if 'a' <= p <= 'z':
        print(chr(ord('a') + (ord(p)-ord('a') + 3) % 26), end="")
        # print(chr(ord(p) + 3), end="")-----无法处理循环
    elif 'A' <= p <= 'Z':
        print(chr(ord('A') + (ord(p)-ord('A') + 3) % 26), end="")
        # print(chr(ord(p) + 3), end="")-----无法处理循环
    else:
        print(p, end="")









# 好的，我们用字符 `h` 来演示第一个语句的效果。

# ### 示例：

# 设 `p = 'h'`。

# #### 1. 计算步骤：

# - `ord(p)` 是 `'h'` 的 Unicode 编码值，即 `ord('h') = 104`。
# - `ord('a')` 是 `'a'` 的 Unicode 编码值，即 `ord('a') = 97`。
# - 计算 `ord(p) - ord('a')`，即 `104 - 97 = 7`。这表示 `'h'` 是从 `'a'` 开始的第 7 个字母（0 索引下）。
# - 计算 `(7 + 3) % 26`，即 `(10) % 26 = 10`。这表示从 `'h'` 向右移动 3 个字母之后，我们得到了字母表中的第 10 个字母。
# - 计算 `ord('a') + 10`，即 `97 + 10 = 107`。
# - `chr(107)` 是 `'k'`。

# #### 2. 输出：

# ```python
# print(chr(ord('a') + (ord('h') - ord('a') + 3) % 26), end="")
# ```

# 运行这个代码将输出 `'k'`。

# ### 解释：

# 这个语句将字母 `'h'` 向右移动 3 个位置，结果是 `'k'`。因为从 `'h'` 开始，向右移动 3 个位置依次是 `'i'`、`'j'` 和 `'k'`。









