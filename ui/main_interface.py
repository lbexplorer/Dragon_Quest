import tkinter as tk  # 导入tkinter库

from ui.game_ui import GameGUI
from ui.gei_api import APIKeyInput


class AdventureGameApp():
    def __init__(self, root):
        self.root = root
        self.root.title("冒险游戏")

        self.create_widgets()

    def create_widgets(self):
        # 创建按钮 - 获取密钥
        self.key_button = tk.Button(self.root, text="获取密钥", command=self.show_key_input)
        self.key_button.pack(pady=10)

        # 创建按钮 - 游戏运行
        self.game_button = tk.Button(self.root, text="开始游戏", command=self.start_game)
        self.game_button.pack()

    def show_key_input(self):
        self.root.destroy()  # 销毁当前界面
        key_input_root = tk.Tk()
        app = APIKeyInput(key_input_root)
        key_input_root.mainloop()

    def start_game(self):
        self.root.destroy()  # 销毁当前界面
        game_root = tk.Tk()
        app = GameGUI(game_root)
        game_root.mainloop()

    def return_to_main(self):
        main_root = tk.Tk()
        app = AdventureGameApp(main_root)
        main_root.mainloop()





# 在此之前的内容照常复制即可
class PageOne(tk.Frame):  # 定义界面1 PageOne
    def __init__(self, master):
        tk.Frame.__init__(self, master)  # 在此之后可以自主加入该页内容所需控件，本例子添加Hello world 标签以及跳转到PageTwo的按钮

        tk.Label(self, text="Hello world", font=('Helvetica', 18, "bold")).grid(row=0, column=0, pady=10)
        tk.Button(self, text="Go to PageTwo",
                  command=lambda: master.switch_frame(PageTwo)).grid(row=1, column=0,
                                                                     pady=10)  # 跳转按钮用了之前定义的switch_frame函数，将其变量输入为新定义的界面变量名即可


class PageTwo(tk.Frame):  # 定义界面2PageTwo
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        tk.Button(self, text="Go to PageOne",
                  command=lambda: master.switch_frame(PageOne)).grid(row=0, column=1, pady=100)  # 在此定义可以跳转回PageOne的按钮


if __name__ == "__main__":
    app = AdventureGameApp()
    app.geometry('800x300+200+150')
    app.title('Welcome')
    app.mainloop()
