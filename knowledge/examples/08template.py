import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi
load_dotenv(verbose=True)

prompt_template = PromptTemplate.from_template(
    "我的邻居姓{lastname},刚生了{gender},你帮我起个名字,简单回答。"
)

llm = Tongyi(
    model="qwen-max",
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url=os.getenv("DASHSCOPE_BASE_URL")
)


chain = prompt_template | llm
resp = chain.invoke(input={"lastname":"张","gender":"女"})
print(resp)


