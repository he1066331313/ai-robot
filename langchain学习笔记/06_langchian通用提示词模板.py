from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi
prompt_template = PromptTemplate.from_template(
    "我的名字是{name},请帮我评分！"
)
model = Tongyi(
    model="qwen-max",
)
chain = prompt_template | model
print(chain.invoke({"name": "张三"}))