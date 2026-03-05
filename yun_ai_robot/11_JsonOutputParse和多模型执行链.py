from langchain_community.chat_models.tongyi import  ChatTongyi
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser

str_parse = StrOutputParser()
json_parse = JsonOutputParser()
first_prompt = PromptTemplate.from_template(
    "我邻居姓{lastname}，刚生了{gender}。请帮忙起名字"
    "并封装为JSON格式返回给我，要求key是name，value就是你起的名字，请严格按照格式要求"
)
second_prompt = PromptTemplate.from_template(
    "姓名{name}，请帮我解释含义"
)
model = ChatTongyi(
    model="qwen3-max-2026-01-23"
)
chain  = first_prompt | model | json_parse | second_prompt | model | str_parse
for chunk in chain.stream({"lastname": "何", "gender": "男"}):
    print(chunk,end="",flush=True)