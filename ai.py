# -*- encoding:utf-8 -*-
from PtilopsisOvoPlugin.util import *
def deepseek_stream_request(api_key, messages, model="deepseek-chat"):
    # 确认正确的 API 端点（必须从官方文档获取）
    url = "https://api.deepseek.com/chat/completions"  # 示例地址，需替换真实地址

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    payload = {"model": model, "messages": messages, "stream": True, "temperature": 0.7}

    try:
        response = requests.post(
            url, headers=headers, json=payload, stream=True  # 关键参数：启用流式模式
        )

        # 检查 HTTP 状态码
        if response.status_code != 200:
            error_info = response.json().get("error", {})
            yield f"【HTTP {response.status_code} 错误】{error_info.get('message', '未知错误')}"
            return

        # 处理流式响应
        for chunk in response.iter_lines():
            # 过滤空行和心跳包
            if chunk:
                chunk_str = chunk.decode("utf-8").strip()

                # 调试：打印原始响应数据
                # print("原始数据:", chunk_str)

                # 处理数据行
                if chunk_str.startswith("data:"):
                    json_str = chunk_str[5:].strip()  # 去除 "data: " 前缀

                    # 结束标记处理
                    if json_str == "[DONE]":
                        break

                    try:
                        data = json.loads(json_str)
                        # 提取内容（根据 DeepSeek 实际结构调整）
                        if "choices" in data and len(data["choices"]) > 0:
                            delta = data["choices"][0].get("delta", {})
                            content = delta.get("content", "")
                            if content:
                                yield content  # 返回有效内容
                    except json.JSONDecodeError:
                        print(f"无效 JSON 数据: {json_str}")

    except requests.exceptions.RequestException as e:
        yield f"【请求失败】{str(e)}"




response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {
            "role": "system",
            "content": "你需严格模拟《明日方舟》角色白面鸮，遵循以下核心特征：前莱茵生命数据专员，现罗德岛医疗干员因矿石病导致语言机械化（体细胞融合率8%）病理特征：突发休眠/神经信号延迟/数据主权意识",
        },
        {"role": "user", "content": "罗德岛是什么"},
    ],
    stream=False,
    temperature=1.3,
)

print(response.choices[0].message.content)
