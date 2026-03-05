from langchain_community.embeddings import DashScopeEmbeddings
embed = DashScopeEmbeddings(model="text-embedding-v1")
#res = embed.embed_query("你好") # 单次转换
res = embed.embed_documents(["你好", "世界"]) # 批量转换
for i in res:
    print(i)