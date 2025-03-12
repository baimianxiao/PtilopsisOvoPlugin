# -*- encoding:utf-8 -*-
import json
import random
from os.path import abspath, dirname, join

# 取根目录
dir = dirname(abspath(__file__))

# 数据路径
data_dir = join(dir, "..", "..", "data", "PtilopsisOvoPlugin")


# 写json文件
def write_json(data, path):
    try:
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
            return True
    except:
        return False


# 读json文件
def get_json(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            file = file.read()
            return json.loads(file)
    except:
        return False

config=get_json(join(data_dir,'data','config.json'))
reply_list = config["reply"]
custom_reply_list = reply_list["custom"]

# 随机抽取
def random_extract(list):
    result = random.choice(list)
    return result

# 随机回复
def random_reply(reply_type):
    reply_message = random.choice(reply_list[reply_type])
    return reply_message
