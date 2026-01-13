import base64
import os

import dotenv
import requests

dotenv.load_dotenv()

img_path = "./img/广州塔.jpeg"

with open(img_path, "rb") as f:
    image_data = f.read()

    # 使用python标准base
image_url = f"data:image/jpeg;base64,{base64.b64encode(image_data).decode('utf-8')}"

response = requests.request(
    "POST",
    "https://api.moonshot.cn/v1/chat/completions",
    headers={
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer sk-FLqv9wc64AsWaL1GGvW0RqhmREDGdejICxGy7zAb9uJaEJ86",  # 注意 Bearer
    },
    json={
        "model": "moonshot-v1-8k-vision-preview",
        "messages": [
            {"type":"text","text":"请描述下这张图片，这张图片所在位置是哪里呢"},
            {"type":"image_url","image_url":{"url":image_url}},
        ],
        "stream": False,
    }

)

print(response.json())
