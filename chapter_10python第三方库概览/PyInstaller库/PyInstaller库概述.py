# `pyinstaller` 是一个将 Python 程序打包成独立可执行文件的工具。
# 它可以将你的 Python 脚本和所有依赖项打包到一个单独的可执行文件中，便于在没有 Python 解释器的环境中运行。使用方法很简单：




# 示例:
'''
1. 安装 `pyinstaller`：
   ```bash
   pip install pyinstaller
   ```

2. 使用 `pyinstaller` 打包你的 Python 脚本：
   ```bash
   pyinstaller your_script.py
   ```

   这会生成一个 `dist` 目录，其中包含你的可执行文件。
'''

# 常用命令参数:
'''
当然，这里是 `pyinstaller` 常用参数的表格：

| 参数               | 描述                                           |
|--------------------|------------------------------------------------|
| `--onefile`        | 将所有内容打包成一个单独的可执行文件              |
| `--noconsole`      | 不显示控制台窗口（仅适用于 Windows 上的 GUI 应用） |
| `--console`        | 显示控制台窗口（默认，适用于命令行应用）         |
| `--windowed`       | 启用 GUI 模式，不显示控制台窗口（适用于 Windows 和 macOS） |
| `--icon=icon.ico`  | 为可执行文件设置图标                           |
| `--add-data`       | 添加额外的数据文件或文件夹（格式: `source;dest`） |
| `--hidden-import`  | 指定隐藏的导入模块（可避免某些模块被省略）      |
| `--exclude-module` | 排除特定模块或包（多个模块使用逗号分隔）        |
| `--name`           | 指定生成的可执行文件名称                        |
| `--distpath`       | 设置生成的可执行文件的输出目录                  |
| `--workpath`       | 设置临时工作目录                               |
| `--specpath`       | 设置 `.spec` 文件的存放目录                     |

这些参数可以组合使用，以满足不同的打包需求。
'''

# 文件打包
# pyinstaller SnowView.py
# 单文件打包
# pyinstaller -F SnowView.py
# 增加图标
# pyinstaller -i snowflake.ico -F SnowView.py
# -i <图标文件名.ico>---打包使用指定图标


# ConvertICO
# ConvertICO是一款免费的在线 PNG 到 ICO 文件转换器


