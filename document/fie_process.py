import json
import os


class FileProcessor():

    def __init__(self):
        pass

    def write_json(self, path, string):
        try:
            if not os.path.exists(path):
                with open(path, "w") as f1:
                    pass  # 先判断是否存在该文件，若无则新建

            with open(path, 'w', encoding='utf-8') as f:
                json.dump(string, f)
        except Exception as e:
            print(f"错误代码{e}")


    def read_json(self, path):
        try:
            # 读取游戏历史
            with open(path) as f2:
                msg = json.load(f2)
                return msg
        except Exception as e:
            print(f"错误代码{e}")
