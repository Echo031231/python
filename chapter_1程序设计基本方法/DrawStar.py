# 绘制一个五角星图形
from turtle import *
speed(1)
color('red', 'red') # 设置画笔颜色和填充颜色   
begin_fill()
for i in range(5):
    fd(200) # forward()
    rt(144) # right()
end_fill()
hideturtle()
done()       # 保持窗口开启


