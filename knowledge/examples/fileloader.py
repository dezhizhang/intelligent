
"""加载网页地址"""
import bs4
from langchain_community.document_loaders import WebBaseLoader

page_url = "https://www.langchain.com/community"

loader = WebBaseLoader(web_paths=[page_url])

docs = []
async for doc in loader.alazy_load():
    docs.append(doc)

assert len(docs) == 1
doc = docs[0]
