# 下面是 `turtle` 模块中所有与画笔状态相关的函数和方法的详细列表，涵盖画笔的设置、获取和控制功能：

# | 函数名                 | 用途                                 | 示例代码                                      |
# |------------------------|--------------------------------------|-----------------------------------------------|
# | `turtle.pensize()`     | 设置或获取画笔的宽度（粗细）           | `pen.pensize(5)`<br>`current_size = pen.pensize()` |
# | `turtle.pencolor()`    | 设置或获取画笔的颜色                 | `pen.pencolor("red")`<br>`current_color = pen.pencolor()` |
# | `turtle.fillcolor()`   | 设置或获取填充颜色                   | `pen.fillcolor("blue")`<br>`current_fill_color = pen.fillcolor()` |
# | `turtle.pendown()`     | 将画笔状态设置为“下”，即开始绘制     | `pen.pendown()`<br>`pen.forward(100)`          |
# | `turtle.penup()`       | 将画笔状态设置为“上”，即停止绘制     | `pen.penup()`<br>`pen.forward(100)`            |
# | `turtle.isdown()`      | 检查画笔是否在绘制状态（即画笔是否在下） | `if pen.isdown():`<br>`print("画笔正在绘制")`  |
# | `turtle.hideturtle()`  | 隐藏画笔图标                         | `pen.hideturtle()`                            |
# | `turtle.showturtle()`  | 显示画笔图标                         | `pen.showturtle()`                            |
# | `turtle.speed()`       | 设置画笔的速度                       | `pen.speed(3)`                                |
# | `turtle.dot()`         | 绘制一个点                           | `pen.dot(10, "red")`                          |
# | `turtle.circle()`      | 绘制圆形                             | `pen.circle(50)`                              |
# | `turtle.begin_fill()`  | 开始填充绘制图形                      | `pen.begin_fill()`                            |
# | `turtle.end_fill()`    | 结束填充绘制图形                      | `pen.end_fill()`                              |
# | `turtle.write()`       | 在当前绘图位置写文字                 | `pen.write("Hello", font=("Arial", 16, "normal"))` |
# | `turtle.setheading()`  | 设置画笔的方向                       | `pen.setheading(90)`                          |
# | `turtle.getheading()`  | 获取画笔的当前方向                   | `current_heading = pen.getheading()`          |
# | `turtle.color()`       | 设置画笔颜色和填充颜色               | `pen.color("purple", "yellow")`               |
# | `turtle.turtlesize()`  | 设置海龟的大小                       | `pen.turtlesize(2, 2, 1)`                     |
# | `turtle.shapesize()`   | 设置海龟的形状大小                   | `pen.shapesize(stretch_wid=2, stretch_len=3)` |
# | `turtle.shape()`       | 设置海龟的形状                       | `pen.shape("turtle")`                         |

# ### 示例代码

# 以下是一个示例，展示了如何使用这些函数：

'''
import turtle

# 创建海龟对象
pen = turtle.Turtle()

# 设置画笔属性
pen.pensize(5)                # 设置画笔宽度
pen.pencolor("red")           # 设置画笔颜色
pen.fillcolor("blue")         # 设置填充颜色
pen.speed(3)                  # 设置画笔速度

# 绘制图形
pen.pendown()                 # 开始绘制
pen.begin_fill()              # 开始填充
pen.circle(50)                # 绘制圆形
pen.end_fill()                # 结束填充

# 绘制点
pen.dot(10, "green")          # 绘制一个绿色点

# 写文字
pen.penup()                   # 提起画笔
pen.goto(-100, -100)          # 移动到指定位置
pen.write("Hello Turtle", font=("Arial", 16, "normal"))

# 设置方向
pen.setheading(90)            # 设置方向为90度

# 获取当前方向
current_heading = pen.getheading()
print("当前方向:", current_heading)

# 设置海龟的形状和大小
pen.shape("turtle")           # 设置海龟形状为 "turtle"
pen.turtlesize(2, 2, 1)       # 设置海龟的大小

# 隐藏和显示画笔
pen.hideturtle()              # 隐藏画笔
pen.showturtle()              # 显示画笔

# 结束绘图
turtle.done()
'''

# 这个表格和示例代码涵盖了 `turtle` 模块中所有与画笔状态相关的函数，包括画笔的属性设置、图形绘制和海龟形状管理。如果你还有其他问题或需要进一步的信息，请告诉我！



# 在 `turtle` 模块中，`pencolor()` 方法可以接受不同的参数形式：

# 1. **元组形式**: `pencolor((r, g, b))`，其中 `r`、`g` 和 `b` 可以是 0 到 1 之间的浮点数，或者是 0 到 255 之间的整数。例如：


'''
#     import turtle
    
#     t = turtle.Turtle()
#     t.pencolor((1.0, 0.0, 0.0))  # 红色
#     t.pencolor((0.0, 1.0, 0.0))  # 绿色
#     t.pencolor((0.0, 0.0, 1.0))  # 蓝色
'''


# 2. **分开参数形式**: `pencolor(r, g, b)`，其中 `r`、`g` 和 `b` 是 0 到 1 之间的浮点数。例如：

'''
    import turtle
    
    t = turtle.Turtle()
    t.pencolor(1.0, 0.0, 0.0)  # 红色
    t.pencolor(0.0, 1.0, 0.0)  # 绿色
    t.pencolor(0.0, 0.0, 1.0)  # 蓝色
    t.pencolor(0.0, 0.0, 1.0)  # 蓝色
'''

# 总之，你可以选择使用元组形式或分开参数形式来设置颜色，功能是一样的。
