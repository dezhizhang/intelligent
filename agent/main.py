

import os
import dotenv
import requests

dotenv.load_dotenv()
API_KEY = os.getenv("DEEPSEEK_API_KEY")  # 放在 .env 里

response = requests.post(
    "https://api.deepseek.com/chat/completions",
    headers={
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer sk-abe370cdbb064f86b69cce0ee2d60007",  # 注意 Bearer
    },
    json={
        "model": "deepseek-reasoner",
        "messages": [{"role": "user", "content": "你好，你是?"}],
        "stream": False,
    }
)

print(response.json())





#