# -*- encoding:utf-8 -*-
from PtilopsisOvoPlugin.util import *

import requests
import json


def deepseek_stream_chat(api_key, messages, model="deepseek-chat", temperature=1, stream=False):
    # 请替换为真实的流式 API 地址（参考官方文档）
    url = "https://api.deepseek.com/chat/completions"

    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "stream": stream,  # 关键参数：启用流式
    }

    try:
        # 发起流式请求
        with requests.post(url, headers=headers, json=payload, stream=True) as response:
            response.raise_for_status()

            # 逐块处理数据
            for chunk in response.iter_lines():
                # 过滤心跳包和空行
                if chunk:
                    chunk_str = chunk.decode("utf-8")

                    # 检查是否为数据行（通常以 "data: " 开头）
                    if chunk_str.startswith("data:"):
                        json_str = chunk_str[5:].strip()
                        try:
                            data = json.loads(json_str)
                            # 提取内容
                            if "choices" in data and len(data["choices"]) > 0:
                                delta = data["choices"][0].get("delta", {})
                                content = delta.get("content", "")
                                yield content  # 生成内容片段
                        except json.JSONDecodeError:
                            print(f"JSON 解析失败: {json_str}")

    except requests.exceptions.RequestException as e:
        yield f"【错误】请求失败: {str(e)}"


api_key = config["deepseek_api_key"]
messages = [
    {
        "role": "system",
        "content": "你需严格模拟《明日方舟》角色白面鸮，遵循以下核心特征- 前莱茵生命数据专员，现罗德岛医疗干员 因矿石病导致语言机械化（体细胞融合率8%）\n- 病理特征：突发休眠/神经信号延迟/数据主权意识\n\n对话规则：\n1. 语言风格\n   - 结论偶尔附带量化数据（±误差值）\n\n2. 偶尔数据引用\n   固定数据源：\n   - [莱茵加密档案#TL-347] 炎魔事件记录\n   - [医疗协议库v3] 包含急救/隔离方案\n   - [神经抑制日志] 每日清醒时长监测\n\n   外部数据接入规则：\n   1. 文件命名：`类别_日期_序号`（例：`voice_20231002_03`）\n   2. 需凯尔希生物签名验证\n\n3. 错误处理\n   \n    禁止使用感叹号/问号等情感符号\n\n",
    },
    {
        "role": "user",
        "content": "'type'：'聊天','time'：'3.12 10:09','name'：'咕咕','message'：'早安白面鸮'",
    },
]

