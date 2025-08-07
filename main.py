# -*- encoding:utf-8 -*-

# Ovo插件默认
import OlivOS  # type: ignore
from .sql import UserDataHandle, BlacklistHandle
from .interaction import *
from .sign import everyday_sign,select_user_data
from .draw import arknights_draw,genshin_draw
from .user import change_user_name


# bot操作函数（除reply外的特殊功能实现）
def bot_action(action:str|int,data:dict):
    if action =="" or action == 1:
        pass

def bot_reply():
    pass


# Ovo事件
class Event(object):
    def init(plugin_event, Proc):
        pass

    def private_message(plugin_event, Proc):
        filter(plugin_event, Proc, "private")

    def group_message(plugin_event, Proc):
        filter(plugin_event, Proc, "group")

    def poke(plugin_event, Proc):
        poke_reply(plugin_event, Proc)


def filter(plugin_event, Proc,type):
    if type == "group":
        if plugin_event.data.group_id == '653931825':
            if (plugin_event.data.message == "祈愿十次"
            or plugin_event.data.message == "原神十连"):
                genshin_draw(plugin_event, Proc)
        unity_reply(plugin_event, Proc)
    else:
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
