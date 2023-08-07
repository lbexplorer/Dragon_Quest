from Class_ChatGPT.Class_GPT import *


def main():
    name=input("你的名字：")
    game= Generate_response(name)
    game.game_start(name)

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
   main()
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
