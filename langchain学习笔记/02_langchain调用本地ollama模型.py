from langchain_ollama import OllamaLLM
model = OllamaLLM(model="qwen3:1.7b")
res = model.invoke(input='你是谁')
print(res)