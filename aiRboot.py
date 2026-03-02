import ollama
import streamlit as st

# 创建ollama客户端
client = ollama.Client("http://localhost:11434")
#
if 'message' not in st.session_state:
    st.session_state.message = []
# 创建页面标题
st.title("我的Ai机器人")
# 创建分割线
st.divider()
# 创建输入框
prompt = st.chat_input("请输入你的问题")
# 创建聊天框
if prompt:
    # 储存问题
    st.session_state.message.append({"role": "user", "content": prompt})
    # 显示储存的问题
    for message in st.session_state.message:
        if message["role"] == "user":
            st.chat_message("user").write(message["content"])
        else:
            st.chat_message("assistant").write(message["content"])
    # 调用ollama接口
    response = client.chat(
        model='deepseek-r1:1.5b',
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    # 储存结果
    st.session_state.message.append({"role": "assistant", "content": response.message.content})
    # 显示结果
    st.chat_message("assistant").write(response.message.content)
