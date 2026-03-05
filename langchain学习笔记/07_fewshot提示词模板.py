from langchain_core.prompts import FewShotPromptTemplate,PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi

prompt = PromptTemplate.from_template(
    "单词:{word},反义词:{antonym}"
)
examples = [
    {"word":"大", "antonym":"小"},
    {"word":"高", "antonym":"低"}
]
few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=prompt,
    prefix="给出给定词的反义词，有如下示例",
    suffix="基于示例告诉我，{input_word}的反义词",
    input_variables=["input_word"],
)

model = ChatTongyi(model="qwen3-max-2026-01-23")
prompt_text = few_shot_prompt.invoke({"input_word": "男"}).to_string()
print(prompt_text)
res = model.invoke(input=prompt_text)
print(res.content)