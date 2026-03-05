from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda

str_parse = StrOutputParser()

first_prompt = PromptTemplate.from_template(
    "我邻居姓{lastname}，刚生了{gender}。请帮忙起名字，仅生成一个名字，并告诉我名字，不要额外信息"
)
second_prompt = PromptTemplate.from_template(
    "姓名{name}，请帮我解释含义"
)
model = ChatTongyi(
    model="qwen3-max-2026-01-23"
)
# my_func = RunnableLambda(lambda ai_msg: ai_msg.content)

chain  = first_prompt | model | (lambda ai_msg: {"name":ai_msg.content}) | second_prompt | model | str_parse
for chunk in chain.stream({"lastname": "何", "gender": "男"}):
    print(chunk,end="",flush=True)