# from langchain.memory import ConversationBufferMemory
#
# memory = ConversationBufferMemory()
#
#
# # 存储相关的信息
# memory.save_context(inputs={"input":"你好，我叫小明"},outputs={"output":"很高兴认识你"})
# memory.save_context(inputs={"input":"帮我回答一下1 + 2 * 3 = ?"},outputs={"output":"7"})
#
# # 获取存储的信息
# print(memory.load_memory_variables({}))


from langchain.memory import ConversationBufferMemory
from langchain.schema import messages_from_dict, messages_to_dict

# 创建 Memory
memory = ConversationBufferMemory(
    memory_key="chat_history",  # 存储对话历史的 key
    return_messages=True        # 返回消息对象，而非纯文本
)
# 存储相关信息
memory.save_context(inputs={"input":"你好，我叫小明"},outputs={"output":"很高兴认识你"})
memory.save_context(inputs={"input":"帮我回答一下1 + 2 * 3 = ?"},outputs={"output":"7"})

print(memory.load_memory_variables({}))
