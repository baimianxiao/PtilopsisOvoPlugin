# -*- encoding:utf-8 -*-

import requests # type: ignore

onebot11_token= "12345678"


# LLoneBot接口实现
class LLoneBotApi:

    def __init__(self,onebot11_token,host = "127.0.0.1",port = 3000):
        self.host = host
        self.port = port
        self.headers = {
            "Authorization": f"Bearer {onebot11_token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    # 向llonebot发送post请求
    def llonebot_post(self,route,data):
        url="http://"+self.host +":" + str(self.port) + route
        response = requests.post(url, headers=self.headers, json=data)
 
        # 检查 HTTP 状态码
        if response.status_code != 200:
            error_info = response.json().get("error", {})
            return f"【HTTP {response.status_code} 错误】{error_info.get('message', '未知错误')}\n{url}"
        return f"success!\n{url}"

    
    def send_like(self,user_id:int,times:int):
        data = {
            "user_id":user_id,
            "times":times
        }
        return self.llonebot_post("/send_like",data)

    
llonebot_api=LLoneBotApi(onebot11_token)