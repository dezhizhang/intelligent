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
        {"role":"system","content":"你是AI助手 回答很简结"},
        {"role":"assistant","content":"小明有2条狗"},
        {"role":"assistant","content":"好的"},
        {"role":"user","content":"小花有3只猫"},
        {"role":"assistant","content":"好的"},
        {"role":"user","content":"总共有几个宠物"}
    ],
    stream=True
)

for chunk in response:
    print(chunk.choices[0].delta.content,end=" ",flush=True)
