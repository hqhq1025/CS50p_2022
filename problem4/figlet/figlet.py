import sys
import random
from pyfiglet import Figlet

# 创建 Figlet 实例
figlet = Figlet()

# 获取可用字体列表
font_list = figlet.getFonts()

# 处理命令行参数
if len(sys.argv) == 1:
    # 随机字体
    font = random.choice(font_list)
    figlet.setFont(font=font)
    text = input("Input: ")
    print(figlet.renderText(text))
elif len(sys.argv) == 3 and sys.argv[1] in ['-f', '--font']:
    font = sys.argv[2]
    if font in font_list:
        figlet.setFont(font=font)
        text = input("Input: ")
        print(figlet.renderText(text))
    else:
        sys.exit("Invalid font")
else:
    sys.exit("Invalid usage")