# 下面是 `turtle` 模块中窗体（窗口）相关函数的表格，包括函数名、用途和示例：

# | 函数名             | 用途                                | 示例代码                                      |
# |--------------------|-------------------------------------|-----------------------------------------------|
# | `turtle.Screen()`  | 创建或获取绘图窗口                  | `window = turtle.Screen()`                   |
# | `window.title()`   | 设置窗口标题                        | `window.title("新的标题")`                    |
# | `window.bgcolor()` | 设置窗口背景颜色                    | `window.bgcolor("lightblue")`                 |
# | `window.setup()`   | 设置窗口大小和位置                  | `window.setup(width=800, height=600)`        |
# | `window.clear()`   | 清除窗口中的所有绘图内容            | `window.clear()`                             |
# | `window.exitonclick()` | 设置窗口在点击时关闭            | `window.exitonclick()`                        |
# | `window.bye()`     | 关闭窗口                            | `window.bye()`                               |
# | `window.tracer()`  | 控制绘图的更新频率                  | `window.tracer(0)`                            |
# | `window.update()`  | 手动更新窗口                        | `window.update()`                            |

# ### 示例代码

# 以下是一个包含上述函数的完整示例：

# ```python
# import turtle

# # 创建绘图窗口
# window = turtle.Screen()
# window.title("窗体函数示例")
# window.bgcolor("lightgreen")
# window.setup(width=800, height=600)

# # 创建海龟对象
# pen = turtle.Turtle()
# pen.color("blue")

# # 绘制一个正方形
# for _ in range(4):
#     pen.forward(100)
#     pen.right(90)

# # 关闭窗口时退出
# window.exitonclick()
# ```

# 这个表格和示例代码总结了 `turtle` 模块中与窗口相关的函数和方法。如果你有更多问题或需要更详细的信息，请随时告知！








# `setup` 是 `turtle` 模块中的一个方法，用于设置绘图窗口的尺寸和位置。它可以用于调整窗口的宽度、高度以及初始位置。这个方法在创建和管理图形窗口时非常有用。

# ### `setup()` 方法

# #### 用法

# ```python
# turtle.setup(width=0, height=0, startx=None, starty=None)
# ```

# #### 参数

# - **`width`**: 设置窗口的宽度（像素）。如果为 `0` 或省略，则宽度保持默认值。
# - **`height`**: 设置窗口的高度（像素）。如果为 `0` 或省略，则高度保持默认值。
# - **`startx`**: 设置窗口的初始水平位置（像素），相对于屏幕的左边缘。如果为 `None` 或省略，则使用默认位置。
# - **`starty`**: 设置窗口的初始垂直位置（像素），相对于屏幕的上边缘。如果为 `None` 或省略，则使用默认位置。

# ### 示例

# 以下是 `setup()` 方法的几个使用示例：

# #### 1. **设置窗口大小**

# 设置窗口的宽度为 800 像素，高度为 600 像素。

# ```python
# import turtle

# window = turtle.Screen()
# window.setup(width=800, height=600)

# # 创建海龟对象
# pen = turtle.Turtle()
# pen.forward(100)

# # 结束绘图
# turtle.done()
# ```

# #### 2. **设置窗口大小和位置**

# 设置窗口的宽度为 800 像素，高度为 600 像素，并将窗口位置设置在屏幕的左上角。

# ```python
# import turtle

# window = turtle.Screen()
# window.setup(width=800, height=600, startx=100, starty=100)

# # 创建海龟对象
# pen = turtle.Turtle()
# pen.forward(100)

# # 结束绘图
# turtle.done()
# ```

# #### 3. **仅设置窗口位置**

# 只设置窗口的位置，不改变窗口的默认大小。

# ```python
# import turtle

# window = turtle.Screen()
# window.setup(startx=200, starty=200)

# # 创建海龟对象
# pen = turtle.Turtle()
# pen.forward(100)

# # 结束绘图
# turtle.done()
# ```

# ### 总结

# `setup()` 方法是 `turtle` 模块中用于控制窗口尺寸和位置的重要工具。你可以通过调整这些参数来适应不同的显示需求。如果你有任何其他问题或需要进一步的信息，请随时告诉我！