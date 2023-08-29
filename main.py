import tkinter as tk

from Class_ChatGPT.Class_GPT import *
from ui.game_ui import GameGUI


def main():
    root = tk.Tk()
    # 设置主窗口的大小
    root.geometry("800x600")  # 设置宽度为800像素，高度为600像素
    app = GameGUI(root)
    root.mainloop()

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
   main()
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
