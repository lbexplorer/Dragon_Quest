import tkinter as tk
from tkinter import filedialog

from Key.api_opera import get_key
from ui.game_ui import GameGUI
from ui.main_interface import AdventureGameApp


class APIKeyInput(AdventureGameApp):
    def __init__(self, master):
        self.root = master
        self.root.title("API Key 输入")

        self.create_widgets()

    def create_widgets(self):
        # 创建输入框
        self.api_key_entry = tk.Entry(self.root)
        self.api_key_entry.pack(pady=10)

        # 创建按钮 - 输入 API Key
        self.input_button = tk.Button(self.root, text="输入 API Key", command=self.input_api_key)
        self.input_button.pack()

        # 创建按钮 - 选择文件
        self.file_button = tk.Button(self.root, text="选择文件", command=self.load_api_key_from_file)
        self.file_button.pack()

        # 创建按钮 - 选择本地api
        self.file_button = tk.Button(self.root, text="选择默认API", command=self.default_key)
        self.file_button.pack()

        # 创建显示区域
        self.display_label = tk.Label(self.root, text="")
        self.display_label.pack(pady=10)

        # 创建按钮 - 返回
        self.return_button = tk.Button(self.root, text="返回主界面", command=self.return_to_main)
        self.return_button.pack()
    def input_api_key(self):
        api_key = self.api_key_entry.get()
        self.display_label.config(text=f"输入的 API Key: {api_key}")


    def load_api_key_from_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                api_key = file.read()
                self.display_label.config(text=f"从文件读取的 API Key: {api_key}")

    def default_key(self):
        file_path = r"E:\python\Dragon_Quest\Key\api_key.json"
        api_key = get_key(file_path)
        self.display_label.config(text=f"默认的 API Key: {api_key}")
        self.root.switch_frame(GameGUI).grid(row=0, column=1, pady=100)


if __name__ == "__main__":
    root = tk.Tk()
    app = APIKeyInput(root)
    root.mainloop()
