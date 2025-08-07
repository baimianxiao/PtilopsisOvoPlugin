# -*- encoding:utf-8 -*-

from .sql import UserDataHandle,user_sqlite_path

import math

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
