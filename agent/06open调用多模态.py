import os

import dotenv

from openai import OpenAI

dotenv.load_dotenv()

llm = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE_URL"),
)

response = llm.chat.completions.create(
    model="deepseek-reasoner",
    messages=[{"role": "user", "content": "你好"}]
)

print(response.choices[0].message)


