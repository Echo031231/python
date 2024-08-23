import turtle

# 创建海龟对象
pen = turtle.Turtle()

# 设置画笔速度
pen.speed(1)  # 设置速度为最慢

# 绘制图形
pen.forward(100)                 # 向前移动100单位
pen.left(90)                     # 左转90度
pen.forward(100)                 # 向前移动100单位


# 移动到不同位置
pen.setposition(-50, -50)        # 移动到 (-50, -50)
pen.dot(10, "blue")              # 绘制一个蓝色点


# 绘制圆形
pen.circle(50)                   # 绘制半径为50的圆形


# 撤销上一个绘图动作
pen.undo()                       # 撤销上一个绘图动作


# 获取当前位置和坐标
current_pos = pen.position()     # 获取当前位置
x = pen.xcor()                   # 获取x坐标
y = pen.ycor()                   # 获取y坐标
print("当前位置:", current_pos)
print("x 坐标:", x)
print("y 坐标:", y)


# 返回原点并恢复方向
pen.home()                       # 移动到 (0, 0) 并恢复方向


# 结束绘图
turtle.done()







# 以下是包含所有函数的示例代码：

'''
import turtle

# 创建海龟对象
pen = turtle.Turtle()

# 设置画笔速度
pen.speed(1)  # 设置速度为最慢

# 绘制图形
pen.forward(100)                 # 向前移动100单位
pen.left(90)                     # 左转90度
pen.forward(100)                 # 向前移动100单位

# 移动到不同位置
pen.setposition(-50, -50)        # 移动到 (-50, -50)
pen.dot(10, "blue")              # 绘制一个蓝色点

# 绘制圆形
pen.circle(50)                   # 绘制半径为50的圆形

# 撤销上一个绘图动作
pen.undo()                       # 撤销上一个绘图动作

# 获取当前位置和坐标
current_pos = pen.position()     # 获取当前位置
x = pen.xcor()                   # 获取x坐标
y = pen.ycor()                   # 获取y坐标
print("当前位置:", current_pos)
print("x 坐标:", x)
print("y 坐标:", y)

# 返回原点并恢复方向
pen.home()                       # 移动到 (0, 0) 并恢复方向

# 结束绘图
turtle.done()
'''

# 这个表格和示例代码涵盖了 `turtle` 模块中所有与画笔运动相关的函数，包括直线移动、旋转、设置位置、绘制圆形和点、撤销操作等功能。




 










