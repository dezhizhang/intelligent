import os
import dotenv
from openai import OpenAI
from pydantic import BaseModel, Field, EmailStr

dotenv.load_dotenv()

class UserInfo(BaseModel):
    """传递用户信息进行计算"""
    name: str = Field(..., description="用户名字")
    age: int = Field(..., description="用户年龄，必须是正整数")
    email: EmailStr = Field(..., description="用户电子邮件")

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com/v1"
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "user", "content": "我叫泽辉呀，今年10岁，我的联系方式是zehiya@163.com"}
    ],
    tools=[
        {
            "type": "function",
            "function": {
                "name": "UserInfo",
                "description": UserInfo.__doc__,
                "parameters": UserInfo.model_json_schema()
            }
        }
    ],
    tool_choice={
        "type": "function",
        "function": {"name": "UserInfo"}
    }
)

args = response.choices[0].message.tool_calls[0].function.arguments
user_info = UserInfo.model_validate_json(args)

print(user_info)
