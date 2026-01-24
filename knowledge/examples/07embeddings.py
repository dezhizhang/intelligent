from langchain_community.embeddings import DashScopeEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()


print(os.getenv("DASHSCOPE_API_KEY"))

llm = DashScopeEmbeddings(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url=os.getenv("DASHSCOPE_BASE_URL"),
)


print(llm.embed_query("hello world"))