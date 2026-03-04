from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import HumanMessage,SystemMessage


chat = ChatTongyi(model="qwen3-max-2026-01-23")
messages = [
    SystemMessage(content="你是一个边塞诗人"),
    HumanMessage(content="给我写一首诗")
]
for chunk in chat.stream(input=messages):
    print(chunk.content, end="", flush=True)
