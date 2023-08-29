import json


def get_key( path):
    # 从 JSON 文件读取数据
    with open(f"{path}", "r") as json_file:
        data = json.load(json_file)

    # 获取密钥
    api_key = data["api_key"]

    # 输出密钥
    # print("API Key:", api_key)
    return api_key