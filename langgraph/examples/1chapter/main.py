

# from langchain_ollama import ChatOllama
#
# llm = ChatOllama(
#     model="deepseek-r1:7b",
#     base_url="http://localhost:11434",
#     temperature=0.1,
# )
#
# for chunk in llm.stream("来一段宋词"):
#     print(chunk.content,end="",flush=True)


# from langchain.chat_models import init_chat_model
#
# llm = init_chat_model(
#     model="ollama:deepseek-r1:7b",
#     base_url="http://localhost:11434",
#     temperature=0.1,
#     timeout=120,
#     max_token=2000,
# )
#


from langchain.chat_models import init_chat_model

llm = init_chat_model(
    model="ollama:deepseek-r1:7b",
    base_url="http://localhost:11434",
    temperature=0.1,
    max_token=10,
)

for chunk in llm.stream("中国唐诗"):
    print(chunk.content,end='',flush=True)










