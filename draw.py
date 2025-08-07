# -*- encoding:utf-8 -*-

from .sql import UserDataHandle,user_sqlite_path

import math
import random

def arknights_draw(plugin_event, Proc):
    user_id = plugin_event.data.user_id
    sql = UserDataHandle(user_sqlite_path)
    user_data = sql.user_data_select(user_id)
    if user_data is None:
        plugin_event.reply(
            f"————————————\n▼ ERROR!\n│ 未查询到用户资料 \n┣———————————\n▲ 请使用签到指令初始化!\n————————————"
        )
        return True
    user_ex = user_data[0][3]
    user_hcy = user_data[0][5]
    user_time = user_data[0][6]
    level = math.floor(user_ex / 2000)
    if user_hcy < 6000:
        plugin_event.reply(
            f"————————————\n▼ ERROR!\n│ 合成玉不足 \n┣———————————\n▲ 现有合成玉：{user_hcy}\n————————————"
        )
        return True
    hcy = 6000
    user_hcy = int(user_hcy) - int(hcy)
    sql.user_data_update(user_id, user_ex, level, user_hcy, user_time)
    id=random.randint(1, 100000)
    plugin_event.reply(f"[CQ:image,file=http://127.0.0.1:11451/api/draw/image?game=arknights&cha={id}]")
    return True

def genshin_draw(plugin_event, Proc):
    user_id = plugin_event.data.user_id
    sql = UserDataHandle(user_sqlite_path)
    user_data = sql.user_data_select(user_id)
    if user_data is None:
        plugin_event.reply(
            f"————————————\n▼ ERROR!\n│ 未查询到用户资料 \n┣———————————\n▲ 请使用签到指令初始化!\n————————————"
        )
        return True
    user_ex = user_data[0][3]
    user_hcy = user_data[0][5]
    user_time = user_data[0][6]
    level = math.floor(user_ex / 2000)
    if user_hcy < 6000:
        plugin_event.reply(
            f"————————————\n▼ ERROR!\n│ 合成玉不足 \n│ 无法转换 \n┣———————————\n▲ 现有合成玉：{user_hcy}\n————————————"
        )
        return True
    hcy = 6000
    user_hcy = int(user_hcy) - int(hcy)
    sql.user_data_update(user_id, user_ex, level, user_hcy, user_time)
    id=random.randint(1, 100000)
    plugin_event.reply(f"[CQ:image,file=http://127.0.0.1:11451/api/draw/image?game=genshin&cha={id}]")
    return True

