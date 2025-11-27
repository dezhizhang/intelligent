from dashscope import api_key
from langchain.chat_models import init_chat_model
from langchain_core.rate_limiters import InMemoryRateLimiter
from openai import base_url

#
# llm = ChatOpenAI(
#     api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
#     base_url="https://poloai.top/v1",
#     temperature=1,
#     max_tokens=10,
#     max_retries=10
# )

# rate_limiter = InMemoryRateLimiter(
#     requests_per_second=0.1,
#     check_every_n_seconds=0.1,
#     max_bucket_size=10,
# )
#
#
# llm = init_chat_model(
#     api_key= "sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
#     model="deepseek-r1-0528",
#     base_url = "https://poloai.top/v1",
#     model_provider="openai",
#     rate_limiter=rate_limiter,
# )
#
# resp = llm.invoke("你好")
# print(resp)

rate_limiter = InMemoryRateLimiter(
    requests_per_second=0.1,
    check_every_n_seconds=0.1,
    max_bucket_size=10,
)

llm = init_chat_model(
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    model="deepseek-r1-0528",
    model_provider="openai",
    base_url="https://poloai.top/v1",
    rate_limiter=rate_limiter,
)

resp = llm.invoke("你好")
print(resp)

