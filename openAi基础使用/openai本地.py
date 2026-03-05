from langchain_classic.chains.question_answering.map_reduce_prompt import messages
from openai import OpenAI
import streamlit as st
st.title('ai机器人')
st.divider()
if 'message' not in st.session_state:
    st.session_state.message = []
client = OpenAI(
    base_url="http://localhost:11434/v1",
)

prompt = st.chat_input("请输入你的问题")
messages = [
        {"role": "system", "content": "你是一个智能助手"}
    ]
if prompt:
    st.session_state.message.append({"role": "user", "content": prompt})
    for message in st.session_state.message:
        if message["role"] == "user":
            st.chat_message("user").markdown(message["content"])
        else:
            st.chat_message("assistant").markdown(message["content"])

    messages.append({"role": "user", "content": prompt})
    res = client.chat.completions.create(
        model="qwen3:4b",
        messages=messages
    )
    st.session_state.message.append({"role": "assistant", "content": res.choices[0].message.content})
    st.chat_message("assistant").markdown(res.choices[0].message.content)