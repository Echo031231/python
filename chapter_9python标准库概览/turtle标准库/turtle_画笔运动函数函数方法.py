# 了解了！我将 `undo` 和 `speed` 函数添加到表格中，并更新内容以确保全面性。以下是包括所有相关画笔运动函数的完整表格：

# | 函数名                           | 用途                                | 示例代码                                      |
# |----------------------------------|-------------------------------------|-----------------------------------------------|
# | `turtle.forward(distance)`       | 向前移动指定的距离                 | `pen.forward(100)`                           |
# | `turtle.backward(distance)`      | 向后移动指定的距离                 | `pen.backward(100)`                          |
# | `turtle.left(angle)`             | 左转指定的角度                      | `pen.left(90)`                               |
# | `turtle.right(angle)`            | 右转指定的角度                      | `pen.right(90)`                              |
# | `turtle.setx(x)`                 | 设置当前位置的 x 坐标               | `pen.setx(50)`                               |
# | `turtle.sety(y)`                 | 设置当前位置的 y 坐标               | `pen.sety(50)`                               |
# | `turtle.setposition(x, y)`        | 移动到指定的位置 (x, y)             | `pen.setposition(50, 50)`                     |
# | `turtle.setpos(x, y)`            | 移动到指定的位置 (x, y)             | `pen.setpos(50, 50)`                         |
# | `turtle.goto(x, y)`              | 移动到指定的位置 (x, y)             | `pen.goto(50, 50)`                           |
# | `turtle.setheading(angle)`        | 设置海龟的方向                      | `pen.setheading(90)`                         |
# | `turtle.getheading()`            | 获取海龟的当前方向                 | `current_heading = pen.getheading()`          |
# | `turtle.circle(radius, extent=None, steps=None)` | 绘制圆形或圆弧 | `pen.circle(50)`<br>`pen.circle(50, 180)`<br>`pen.circle(50, steps=6)` |
# | `turtle.dot(size, color)`         | 在当前位置绘制一个点                | `pen.dot(10, "red")`                         |
# | `turtle.home()`                  | 移动到原点 (0, 0) 并恢复方向       | `pen.home()`                                 |
# | `turtle.position()`              | 获取当前位置                        | `current_pos = pen.position()`<br>`print("当前位置:", current_pos)` |
# | `turtle.xcor()`                  | 获取当前位置的 x 坐标               | `x = pen.xcor()`<br>`print("x 坐标:", x)`    |
# | `turtle.ycor()`                  | 获取当前位置的 y 坐标               | `y = pen.ycor()`<br>`print("y 坐标:", y)`    |
# | `turtle.undo()`                  | 撤销上一个绘图动作                  | `pen.undo()`                                 |
# | `turtle.speed(speed)`            | 设置绘图速度                        | `pen.speed(3)`<br>`pen.speed("fastest")`    |

# ### 示例代码
# 见画笔运动函数实例.py




# 补充:

# circle() 函数
'''
circle() 函数用于在 Turtle 模块中绘制圆形。它的参数主要包括：

半径 (radius)：指定圆的半径。这个参数是必需的。

角度 (extent)：可选参数，表示绘制圆弧的角度（以度为单位）。默认值是 360 度，表示绘制完整的圆。如果设置为其他值，将绘制一个圆弧。

方向 (steps)：可选参数，用于绘制多边形。指定多边形的边数。默认值是 None，表示绘制圆形。如果指定了边数，circle() 函数将绘制一个近似圆形的多边形
'''



# speed()函数
'''
# `turtle.speed()` 是 `turtle` 模块中的一个函数，用于设置绘图的速度。它的参数可以是以下几种形式：

### 1. 数值参数
# `speed()` 函数可以接受 0 到 10 的整数参数，用于设置绘图速度：

# - **0**: 最快（无动画，立即完成绘图）
# - **1**: 最慢
# - **10**: 较快
# - **其他数值**: 表示介于 1 和 10 之间的速度

# ### 2. 字符串参数
# `turtle.speed()` 还可以接受以下字符串参数：

# - **"fastest"**: 最快（等同于 0）
# - **"fast"**: 较快（等同于 10）
# - **"normal"**: 默认速度（等同于 6）
# - **"slow"**: 较慢（等同于 3）
# - **"slowest"**: 最慢（等同于 1）

'''




