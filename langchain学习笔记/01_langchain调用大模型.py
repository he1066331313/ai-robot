# pip install langchain langchain-community langchain-ollama dashscope chromadb
# Langchain： 核心包
# langchain-community；社区支持包，提供了更多的第三方模型调用（我们用的阿里云千问模型就需要这个包）
# Langchain-ollama:Ollama支持包，支持调用O1lama托管部署的本地模型
# dashscope：阿里云通义千问的Python
# SDK
# chromadb：轻量向量数据库（后续使用）
from langchain_community.llms.tongyi import Tongyi

model = Tongyi(
    model="qwen-max",
)
# prompt = input("请输入问题：")
res = model.stream(input='你是谁')
for chunk in res:
    print(chunk, end="", flush=True)
