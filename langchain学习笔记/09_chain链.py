from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.runnables import RunnableSerializable

chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个边塞诗人,可以作诗"),
        MessagesPlaceholder("history"),
        ("human", "请再来一首唐诗,无需额外输出"),
    ]

)
history_data = [
    ("human", "请给我写一首唐诗"),
    ("ai", "锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦"),
    ("human", "请给我写一首唐诗"),
    ("ai", "西风瘦马，客输西风，西风瘦马，客输西风"),
]

model = ChatTongyi(
    model="qwen3-max-2026-01-23"
)
chain:RunnableSerializable = chat_prompt_template | model
res = chain.invoke({"history": history_data})
print(res.content)
# for chunk in chain.stream({"history": history_data}):
#     print(chunk.content)