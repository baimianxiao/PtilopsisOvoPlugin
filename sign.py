# -*- encoing:utf-8 -*-

from .sql import UserDataHandle,user_sqlite_path
from .llonebot import llonebot_api

import random
import time
import math

sign_version = "v2.1.1"


# 每日签到
def everyday_sign(plugin_event, Proc):
    sql = UserDataHandle(user_sqlite_path)
    user_id = plugin_event.data.user_id
    user_data = sql.user_data_select(user_id)
    if user_data is None:
        sql.user_data_insert(
            "用户", user_id, 1, 0, 12000, time.strftime("%Y-%m-%d", time.localtime())
        )
        plugin_event.reply(
            f"————————————\n▼ 初始化成功！\n│ successfully!\n┣———————————\n▲ 获得初始合成玉：12000\n————————————\n请使用 更改用户名+名称 更改用户名"
        )
        return True
    user_name = user_data[0][1]
    user_ex = user_data[0][3]
    user_hcy = user_data[0][5]
    user_time = user_data[0][6]
    if user_time == time.strftime("%Y-%m-%d", time.localtime()):
        plugin_event.reply("今天已经签到了")
        return True
    hcy_add = random.randint(20, 50) * 600
    ex_add = random.randint(1, 20) * 10

    user_ex = int(user_ex) + int(ex_add)
    user_hcy = int(user_hcy) + int(hcy_add)
    level = math.floor(user_ex / 2000)
    sql.user_data_update(
        user_id, user_ex, level, user_hcy, time.strftime("%Y-%m-%d", time.localtime())
    )
    llonebot_api.send_like(int(user_id),10)
    plugin_event.reply(
        f"————————————\n▼ 签到成功！\n│ Sign in successfully!\n┣———————————\n│ Dr.{user_name}\n│ 获得合成玉：{hcy_add}\n▲ 现有合成玉：{user_hcy}\n————————————"
    )
    return True


# 查询信息
def select_user_data(plugin_event, Proc):
    sql = UserDataHandle(user_sqlite_path)
    user_id = plugin_event.data.user_id
    user_data = sql.user_data_select(user_id)
    if user_data is None:
        plugin_event.reply(f"————————————\n▼ Error！\n▲ 没有相关签到记录\n————————————")
        return True
    user_name = user_data[0][1]
    user_hcy = user_data[0][5]
    plugin_event.reply(
        f"————————————\n▼ Dr.{user_name}\n▲ 现有合成玉：{user_hcy}\n————————————"
    )
    return True