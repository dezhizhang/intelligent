import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()


client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url=os.getenv("DASHSCOPE_BASE_URL"),
)

response = client.chat.completions.create(
    model="qwen3-max",
    messages=[
        {"role":"system","content":"你是一个Python编程专家,并且不说废话简单回答"},
        {"role":"assistant","content":"好的，我是编程专家，并且话不多，你要问什么"},
        {"role":"user","content":"输出1-10的数字 python 使用python代码"}
    ]
)


print(response.choices[0].message.content)


