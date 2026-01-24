from langchain_community.chat_models import ChatTongyi
from dotenv import load_dotenv
import os

load_dotenv(verbose=True)

llm = ChatTongyi(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url=os.getenv("DASHSCOPE_BASE_URL"),
    model="qwen3-max"
)

messages = [
    ("system","你是一个边塞诗人"),
    ("human", "写一首唐诗"),
    ("ai","锄禾日当午,汗滴禾下土,谁知盘中餐,粒粒皆辛苦。"),
    ("human","按照你上一个回复的格式,在写一首唐诗。")
]

resp = llm.stream(input=messages)

for chunk in resp:
    print(chunk.content,end="",flush=True)




