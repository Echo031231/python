import turtle as t

# | `turtle.forward(distance)` | 向前移动指定的距离   
'''
# t.fd(500)
t.forward(500)
t.forward(-250)
'''

# | `turtle.backward(distance)` | 向后移动指定的距离  
'''
# t.bk(-500)
t.backward(750)
t.backward(-500)
'''

# | `turtle.right(angle)`    | 右转指定的角度 
# | `turtle.left(angle)`     | 左转指定的角度  
'''
t.forward(250)
t.right(90)
t.forward(250)
t.left(90)
t.forward(100)
'''

# | `turtle.goto(x, y)`      | 移动到指定的位置 (x, y)  
'''
t.goto(300, 250)
'''

# | `turtle.setx(x)`         | 设置当前位置的 x 坐标   
# | `turtle.sety(y)`         | 设置当前位置的 y 坐标  
'''
t.setx(300)
t.sety(250)
'''

# | `turtle.setheading(angle)` | 设置海龟的方向
'''   
t.setheading(45)
t.forward(250)
'''  

# | `turtle.home()`          | 移动到原点 (0, 0) 并恢复方向 
'''
t.home()
t.forward(250)
'''

# | `turtle.circle(radius, extent=None, steps=None)` | 绘制圆形或圆弧 
'''
t.circle(100, extent=90)
t.circle(-50)
'''

# | `turtle.dot(size, color)` | 在当前位置绘制一个点   
'''
t.dot(100, 'purple')
'''

# | `turtle.undo()`                  | 撤销上一个绘图动作

'''
t.forward(250)
t.right(45)
t.forward(250)
t.backward(200)
t.undo()
'''    

# | `turtle.speed(speed)`            | 设置绘图速度           
'''
t.speed(1)
t.forward(250)
t.right(45)
t.speed(1)
t.forward(250)
t.speed(10)
t.backward(200)
'''





