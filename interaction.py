from PtilopsisOvoPlugin.util import *

def poke_reply(plugin_event, Proc):
    loginInfo = plugin_event.get_login_info()
    if(plugin_event.data.target_id == loginInfo["data"]["id"]):
        plugin_event.reply(random_reply("poke"))
        plugin_event.set_block()


def reply_message(plugin_event, Proc):
    message = plugin_event.data.message
    if message in custom_reply_list.keys():
        custom_reply = custom_reply_list[message]
        custom_reply = random_extract(custom_reply)
        plugin_event.reply(custom_reply)
