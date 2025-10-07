from langchain_community.memory import ConversationBufferWindowMemory

# # 实例化conversion
# memory = ConversationBufferWindowMemory(k=5, return_messages=True)
#
# # 保存消息
# memory.save_context({"input":"你好"},{"output":"怎么了"})
# memory.save_context({"input":"你是谁"},{"output":"我是AI助手"})
# memory.save_context({"input":"你的生日是哪天"},{"output":"我不清楚"})
#
# print(memory.load_memory_variables({}))

from langchain.memory import  ConversationBufferWindowMemory

# 实全名