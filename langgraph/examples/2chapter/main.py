#
# from langchain_openai import ChatOpenAI
#
# llm = ChatOpenAI(
#     model="gpt-4o-mini",
#     base_url="https://poloai.top/v1",
#     api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
#     temperature=0.5,
# )
#
# for chunk in llm.stream("来一首唐诗"):
#     print(chunk.content,end='',flush=True)


# from langchain_openai import ChatOpenAI
#
# llm = ChatOpenAI(
#     model="gpt-4o-mini",
#     base_url="https://poloai.top/v1",
#     api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
#     temperature=0.5,
# )
#
# for chunk in llm.stream("来一首唐诗"):
#     print(chunk.content,end="",flush=True)


# from langchain.chat_models import init_chat_model
#
# llm = init_chat_model(
#     model="gpt-4o-mini",
#     base_url="https://poloai.top/v1",
#     api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
#     temperature=0.5,
# )
#
# for chunk in llm.stream("你是 请解释一下大模型"):
#     print(chunk.content,end="",flush=True)

from langchain.chat_models import init_chat_model

llm = init_chat_model(
    model="gpt-4o-mini",
    base_url="https://poloai.top/v1",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    temperature=0.5,
)


for chunk in llm.stream("hello world"):
    print(chunk.content,end="",flush=True)
