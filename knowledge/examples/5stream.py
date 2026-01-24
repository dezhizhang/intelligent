from langchain_community.llms.tongyi import Tongyi
from dotenv import load_dotenv
import os
load_dotenv(verbose=True)

llm = Tongyi(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url=os.getenv("DASHSCOPE_BASE_URL"),
    model="qwen-max"
)

resp = llm.stream(input="你是难呀能干什么?")
for chunk in resp:
    print(chunk,end=" ",flush=True)

