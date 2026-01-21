
import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv(verbose=True)

llm = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url=os.getenv("DASHSCOPE_BASE_URL"),
)

completion = llm.chat.completions.create(
    model="qwen3-max",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "你是谁？"},
    ],
    stream=True
)

for chunk in completion:
    print(chunk.choices[0].delta.content,end="",flush=True)