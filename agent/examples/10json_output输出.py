import os

import dotenv
from openai import OpenAI
from pydantic import BaseModel,Field

dotenv.load_dotenv()

class SplitTask(BaseModel):
    task_count: int = Field(..., ge=0,le=10,description="折分的子任务总数")
    tasks:list[str] = Field(...,description="拆分的任务列表")

llm = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://api.deepseek.com/v1"
)
system_prompt = """用户提问了一个问题，请拆解为多个子任务。请**用 JSON 格式输出**，示例如下:
{
    "task_count": 3,
    "tasks": [
        "调用浏览器搜索今天的时间",
        "调用浏览器搜索广州的天气",
        "综合搜索结果调用 LLM 整理答案并回答"
    ]
}
注意：
- task_count 不超过10
- tasks 是有顺序的数组，每个元素是字符串
"""
while True:
    user_prompt = input("Query:").strip()
    if user_prompt == "exit":
        break

    messages = [
        {"role":"system","content":system_prompt},
        {"role":"user","content":user_prompt}
    ]

    response = llm.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        response_format={"type":"json_object"}
    )

    split_task = SplitTask.model_validate_json(response.choices[0].message.content)
    print("拆解任务数:",split_task.task_count)
    for idx,task in enumerate(split_task.tasks):
        print("<UNK>:",task)
