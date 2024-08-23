# chapter_9  实例解析---雪景艺术绘图
from turtle import *
from random import *


# 画雪函数
def drawSnow():
    hideturtle()
    pensize(2)
    for i in range(100):
        r , g , b = random(), random(), random() # 生成[0.0, 1.0)的浮点数(double型)
        pencolor(r, g, b) # 或者pencolor((r, g, b))
        penup()
        setx(randint(-350, 350)) # [a, b]之间随机整数
        sety(randint(1, 270))
        pendown()
        dens = randint(8, 12) # 雪花花瓣数
        snowsize = randint(10, 14) # 雪花大小
        for j in range(dens):
            forward(snowsize)
            backward(snowsize)
            right(360/dens)

# 画地面函数:
def drawGround():
    hideturtle()
    for i in range(400):
        pensize(randint(5, 10)) # 通常为[1, 10]
        x = randint(-400, 350)
        y = randint(-280, -1)
        r, g, b = -y/280, -y/280, -y/280
        pencolor((r, g, b))
        penup()
        goto(x, y)
        pendown()
        forward(randint(40, 100))

# 主函数:
setup(800, 600, 200, 200) # 设置画布
# speed(0) # 画笔速度最快 (无动画，立即完成绘图)
tracer(False) # 关闭动画效果(直接生成最终结果)E
bgcolor("black")
drawSnow()
drawGround()
done() # 保持窗口开启



# 代码解释:

### 绘制雪花图案
'''
        dens = randint(8, 12)
        snowsize = randint(10, 14)
        
        for j in range(dens):
            turtle.forward(snowsize)
            turtle.backward(snowsize)
            turtle.right(360 / dens)

# - `dens` 是雪花的密度，即雪花的边数，随机生成在 8 到 12 之间。
# - `snowsize` 是每个雪花的大小，随机生成在 10 到 14 之间。

# 每个雪花的绘制过程：
# - `turtle.forward(snowsize)` 向前移动 `snowsize` 距离。
# - `turtle.backward(snowsize)` 向后移动 `snowsize` 距离，回到起点。
# - `turtle.right(360 / dens)` 右转 `360 / dens` 度，改变画笔的方向，为下一个边做准备。
'''

### RGB值相同时解释:
'''
在 RGB 颜色模型中，当 `r`, `g`, 和 `b` 的值相同时，颜色是一个灰色的不同阴影。具体来说：

### RGB 同样值的含义：

- **RGB 颜色模型**: 每个颜色通道（红色、绿色、蓝色）的强度范围是从 0 到 255（在 0 到 1 的范围内是 0.0 到 1.0）。
RGB 值相同意味着这三个颜色通道的强度相同，因此得到的颜色是灰色。



### 示例

#### 1. **完全黑色**:
```python
r, g, b = 0.0, 0.0, 0.0
```
- 这是完全没有颜色的黑色。

#### 2. **中等灰色**:
```python
r, g, b = 0.5, 0.5, 0.5
```
- 所有颜色通道的强度相等，得到的是中等灰色。

#### 3. **完全白色**:
```python
r, g, b = 1.0, 1.0, 1.0
```
- 所有颜色通道的强度都达到最大值，得到的是完全的白色。



### 在代码中的应用
在你的代码中：
```python
r, g, b = -y/280, -y/280, -y/280
```
- **`-y/280`** 是通过 y 坐标计算的灰度值。
- 当 `r`, `g`, 和 `b` 的值相同，生成的颜色是灰色，颜色的深浅取决于 `-y/280` 的值。

### 总结
RGB 值相同代表一个灰色，因为没有颜色的强度差异。灰色的深浅由 RGB 值的大小决定：值越高，灰色越亮；值越低，灰色越暗。

'''



