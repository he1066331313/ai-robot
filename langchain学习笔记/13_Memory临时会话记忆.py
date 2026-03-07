#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2026/3/5 13:17
# @Author : heming
# @File : 13_Memory临时会话记忆.py
# @Software: PyCharm
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.output_parsers import  StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

model = ChatTongyi(
    model="qwen3-max-2026-01-23",
)


prompt = ChatPromptTemplate.from_messages([
    ('system', "你需要根据历史会话回应用户问题。"),
    MessagesPlaceholder(variable_name="chat_history"),
    ('human', "用户提问：{input}，请回答"),
])
str_parse = StrOutputParser()

base_chain = prompt | model | str_parse

store = {}
def get_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

# 创建一个新的链续，并添加一个历史记录
conversation_chain = RunnableWithMessageHistory(
    base_chain,
    get_history,
    input_messages_key="input",
    history_messages_key="chat_history"
)
if __name__ == "__main__":
    session_config = {
        "configurable":{
            "session_id": "user_001"
        }
    }
    res = conversation_chain.invoke({'input':'小明有2只猫'},session_config)
    res = conversation_chain.invoke({'input': '小刚有1只狗'}, session_config)
    res = conversation_chain.invoke({'input': '总共有几只宠物'}, session_config)
    print(res)