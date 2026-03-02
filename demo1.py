import ollama

client = ollama.Client("http://localhost:11434")
# client.show('deepseek-r1:1.5b')
# info = client.ps()
# print(info)

while True:
    prompt = input("请输入：")
    response = client.chat(
        model='deepseek-r1:1.5b',
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    print(response['message']['content'])
