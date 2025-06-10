# -*- encoding:utf-8 -*-

# Ovo插件默认
import OlivOS  # type: ignore
import PtilopsisOvoPlugin
from PtilopsisOvoPlugin.sql import UserDataHandle, BlacklistHandle
from PtilopsisOvoPlugin.interaction import *

import math
import time
import random
from os.path import abspath, dirname, join


# 取根目录
dir = dirname(abspath(__file__))

# 数据路径
data_dir = join(dir, "..", "..", "data", "PtilopsisOvoPlugin")

# 数据库路径
user_sqlite_path = join(data_dir, "user_data.db")


# Ovo事件
class Event(object):
    def init(plugin_event, Proc):
        pass

    def private_message(plugin_event, Proc):
        filter(plugin_event, Proc)

    def group_message(plugin_event, Proc):
        filter(plugin_event, Proc)

    def poke(plugin_event, Proc):
        poke_reply(plugin_event, Proc)

    def save(plugin_event, Proc):
        pass

    def menu(plugin_event, Proc):
        if plugin_event.data.namespace == "PtilopsisOvoPlugin":
            if plugin_event.data.event == "OlivOSPluginTemplate_Menu_001":
                pass
            elif plugin_event.data.event == "OlivOSPluginTemplate_Menu_002":
                pass

def filter(plugin_event, Proc):
    if plugin_event.data.group_id == '653931825':
        if (plugin_event.data.message == "祈愿十次"
        or plugin_event.data.message == "原神十连"):
            genshin_draw(plugin_event, Proc)

    unity_reply(plugin_event, Proc)

def unity_reply(plugin_event, Proc):
    # 签到功能
    if plugin_event.data.message == "签到" or plugin_event.data.message.startswith(
        "/签到"
    ):
        everyday_sign(plugin_event, Proc)
        # plugin_event.reply(str(plugin_event.data.sender))

    # 签到功能
    elif (
        plugin_event.data.message == "寻访十次"
        or plugin_event.data.message == "方舟十连" 
    ):
        arknights_draw(plugin_event, Proc)

    # 绑定用户名
    elif plugin_event.data.message.startswith("/更改用户名"):
        change_user_name(plugin_event, Proc)

    # 查询个人
    elif plugin_event.data.message.startswith("查询"):
        select_user_data(plugin_event, Proc)

    # 覆盖help内容
    elif plugin_event.data.message.startswith(
        "/help"
    ) or plugin_event.data.message.startswith(".help"):
        plugin_event.reply(
            "OlivaDice By lunzhiPenxil Ver.3.3.24(1074) [Python 3.11.0 For OlivOS 0.11.27]\n若需要使本机器人退群,请使用[.bot exit]\n输入[.bot on]/[.bot off]可以开关骰子功能\n(如群内有多个骰子,请在@后追加指令)\n白面鸮正在重新恢复中，具体通知以用户群信息为准\n用户群：957992799"
        )
        plugin_event.set_block()

    else:
        reply_message(plugin_event, Proc)


sign_version = "v2.1.0"


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
    plugin_event.reply(
        f"————————————\n▼ 签到成功！\n│ Sign in successfully!\n┣———————————\n│ Dr.{user_name}\n│ 获得合成玉：{hcy_add}\n▲ 现有合成玉：{user_hcy}\n————————————"
    )
    return True


# 更改用户名
def change_user_name(plugin_event, Proc):
    user_name = plugin_event.data.message.strip("/更改用户名").strip()
    if user_name != "":
        sql = UserDataHandle(user_sqlite_path)
        user_id = plugin_event.data.user_id
        user_data = sql.user_data_select(user_id)
        user_ex = user_data[0][3]
        user_hcy = user_data[0][5]
        user_time = user_data[0][6]
        level = math.floor(user_ex / 2000)
        sql.user_data_update(user_id, user_ex, level, user_hcy, user_time, user_name)
        plugin_event.reply("用户名已修改为" + user_name)
    else:
        plugin_event.reply("用户名不能为空！")


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


def private_data_select():
    pass
