import json
import os
import dotenv
import requests

dotenv.load_dotenv()
API_KEY = os.getenv("DEEPSEEK_API_KEY")  # 放在 .env 里

with requests.post(
    "https://api.deepseek.com/chat/completions",
    headers={
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer sk-abe370cdbb064f86b69cce0ee2d60007",  # 注意 Bearer
    },
    json={
        "model": "deepseek-reasoner",
        "messages": [{"role": "user", "content": "你好，你是?"}],
        "stream": True,
    }
) as resp:

    for line in resp.iter_lines(decode_unicode=True):
       if line:
           if line.startswith("data:"):
               data = line.lstrip("data:").strip()
               print("data",data)






#