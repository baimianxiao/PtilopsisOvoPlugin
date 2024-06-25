from PtilopsisOvoPlugin.util import random_reply

def poke_reply(plugin_event, Proc):
    loginInfo = plugin_event.get_login_info()
    if(plugin_event.data.target_id == loginInfo["data"]["id"]):
        plugin_event.reply(random_reply("pokeReply"))
        plugin_event.set_block()