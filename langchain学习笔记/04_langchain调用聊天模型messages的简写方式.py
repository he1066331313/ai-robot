from langchain_community.chat_models.tongyi import ChatTongyi

chat = ChatTongyi(model="qwen3-max-2026-01-23")
messages = [
    ('system', '你是一个边塞诗人'),
    ('human', '给我写一首诗'),
    ('ai', '锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦'),
    ('human', '按照上次的回复的格式，给我写一首诗'),
]
for chunk in chat.stream(input=messages):
    print(chunk.content, end="", flush=True)
