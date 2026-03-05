from openai import OpenAI
client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
res = client.chat.completions.create(
    model="qwen3-max-2026-01-23",
    messages=[
        {"role": "user", "content": "请给我写一首唐诗"},
        {"role": "assistant", "content": "锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦"},
        {"role": "user", "content": "请再给我写一首唐诗"},
    ]
)
print(res.choices[0].message.content)