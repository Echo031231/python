# 绘制七彩圆圈
import turtle
turtle.speed(10)
color = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple'] #indigo靛蓝
for i in range(7):
    c = color[i]
    turtle.color(c, c)
    turtle.begin_fill()
    turtle.rt(360/7)
    turtle.circle(50)
    turtle.end_fill()
turtle.done()

