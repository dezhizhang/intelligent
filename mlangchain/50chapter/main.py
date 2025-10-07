from langchain.memory import ConversationBufferMemory
# 实例化memory
memory = ConversationBufferMemory()


memory.save_context(inputs={"input":"你好，我叫小明"},outputs={"output":"很高兴认识你"})
memory.save_context(inputs={"input":"帮我回签一下 1 + 2 * 3 = ?"},outputs={"output":"7"})


print(memory.load_memory_variables({}))
