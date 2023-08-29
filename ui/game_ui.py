import tkinter as tk

from Class_ChatGPT.Class_GPT import generateResponse


class GameGUI(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)  # 在此之后可以自主加入该页内容所需控件
        self.root = master
        self.root.title("勇者斗恶龙冒险")
        self.create_widgets()
        self.player_hp = 100
        pass

    def create_widgets(self):
        # 创建文本框
        self.text_box_system = tk.Text(self.root, height=20, width=100)
        self.insert_text("请输入你的名字")
        self.text_box_system.pack()
        self.text_box_user = tk.Text(self.root, height=10, width=50)  # 读取玩家的输入
        self.text_box_user.pack()
        # 创建按钮
        self.button = tk.Button(self.root, text="发送", command=self.game_loop)
        self.button.pack()
        # 创建生命值标签
        self.hp_label = tk.Label(self.root, text="生命值: 100")
        self.hp_label.place(x=100, y=450)

    def game_loop(self):  # 游戏主循环
        user_input = self.text_box_user.get("1.0", "end-1c")
        # 从文本框中获取玩家输入的文本内容。
        Chat = generateResponse(user_input)
        if user_input.lower() == "结束冒险" or user_input.lower() == "退出游戏":
            result_text = "你决定结束冒险。游戏结束。"
            self.insert_text(result_text)
            self.text_box_user.configure(state=tk.DISABLED)
        # 将玩家输入添加到谈话记录中
        Chat.conversation_history.append({"role": "user", "content": user_input})
        # 获取模型回应，进行解析，更新生命值和界面显示
        assistant_reply = Chat.generate_response()
        event, hp_change = Chat.parse_response(assistant_reply)
        if hp_change is not None:
            if hp_change != 0:
                self.player_hp += hp_change
            self.update_hp_label()

        # 将产生的事件存入到历史记录中
        Chat.conversation_history.append({"role": "assistant", "content": event})
        # 输出事件到文本框中
        self.insert_text(f"事件：{event}")

    def insert_text(self, result_text):  # 更新文本框中的内容，将从模型获得的回复输出到文本框
        self.text_box_system.insert(tk.END, f"\n{result_text}\n")

    def update_hp_label(self):  # 更新生命值
        self.hp_label.config(text=f"生命值: {self.player_hp}")

    def process_event(self, hp_change):
        self.player_hp += hp_change
