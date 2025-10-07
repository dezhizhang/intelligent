

from langchain.memory import ConversationTokenBufferMemory
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

memory = ConversationTokenBufferMemory(
    llm = llm,
    max_token_limit=10,
)

memory.save_context({"input":"你好吗"},{"output":"我很好,谢谢！"})
memory.save_context({"input":"今天天气如何"},{"output":"睛天 25度"})

print(memory.load_memory_variables({}))