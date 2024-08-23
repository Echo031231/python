# turtle使用实例:

import turtle
turtle.shape("turtle")
turtle.showturtle()
turtle.pensize(3) #常见的范围是从 1 到 10 像素
turtle.speed(2)   # 设置速度为最慢

# 三角形
turtle.penup()
turtle.goto(-200, -50) # 如果当前画笔处于落下状态，则会绘制当前位置到目标位置的线条
turtle.pendown()
turtle.begin_fill()
turtle.color('red')
turtle.circle(radius=40, steps=3)
turtle.end_fill()

# 四边形
turtle.penup()
turtle.goto(-100, -50) # 如果当前画笔处于落下状态，则会绘制当前位置到目标位置的线条
turtle.pendown()
turtle.begin_fill()
turtle.color('blue')
turtle.circle(radius=40, steps=4)
turtle.end_fill()


# 五边形
turtle.penup()
turtle.goto(0, -50) # 如果当前画笔处于落下状态，则会绘制当前位置到目标位置的线条
turtle.pendown()
turtle.begin_fill()
turtle.color('green')
turtle.circle(radius=40, steps=5)
turtle.end_fill()


# 六边形
turtle.penup()
turtle.goto(100, -50) # 如果当前画笔处于落下状态，则会绘制当前位置到目标位置的线条
turtle.pendown()
turtle.begin_fill()
turtle.color('yellow')
turtle.circle(radius=40, steps=6)
turtle.end_fill()


# 圆形
turtle.penup()
turtle.goto(200, -50) # 如果当前画笔处于落下状态，则会绘制当前位置到目标位置的线条
turtle.pendown()
turtle.begin_fill()
turtle.color('purple')
turtle.circle(radius=40)
turtle.down()
turtle.end_fill()


# 文字
turtle.color('green') # 文字表示颜色
turtle.penup()
turtle.goto(-100, 50)
turtle.pendown()
turtle.write("Cool Colorful Shapes", font=("Times", "18", "bold"))
turtle.hideturtle()


turtle.done()









