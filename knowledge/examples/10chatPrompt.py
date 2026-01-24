import os
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_community.chat_models.tongyi import ChatTongyi
from dotenv import load_dotenv

load_dotenv()

chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system","你是一个边塞诗人,可以作诗。"),
        MessagesPlaceholder("history"),
        ("human","请再来一首唐诗")
    ]
)

history_data = [
    ("human","你来写一首唐诗"),
    ("ai","床前明月光,疑是地上霜,举头望明月,低头思故乡"),
    ("human","好诗再来一个"),
    ("ai","锄禾日当午,汗滴禾下锄,谁知盘中餐,粒粒皆辛苦"),
]

prompt_template = chat_prompt_template.invoke({"history":history_data}).to_string()

llm = ChatTongyi(
    model="qwen-max",
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url=os.getenv("DASHSCOPE_BASE_URL")
)

resp = llm.invoke(prompt_template)
print(resp.content)





