from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi
prompt = ChatPromptTemplate.from_template(
    "我的名字是{name},请帮我评分！"
)
model = ChatTongyi(model="qwen3-max-2026-01-23")
res = model.invoke(input=prompt.invoke({"name": "张三"}))
print(res.content)