from langchain_community.llms.tongyi import Tongyi
import os
from dotenv import load_dotenv
load_dotenv(verbose=True)


llm = Tongyi(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url=os.getenv("DASHSCOPE_BASE_URL"),
    model="qwen-max"
)

resp = llm.invoke(input="你是谁呀，能做什么呀？")
print(resp)



