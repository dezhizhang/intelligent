import bs4

from langchain_community.document_loaders import WebBaseLoader

page_url = "https://member.expireddomains.net/domain-name-search/?start=2800&q=.ai&o=statusorg&r=a#listing"

loader = WebBaseLoader(page_url)
docs = []
async for doc in loader.alazy_load():
    docs.append(doc)

assert len(docs) == 1
doc = docs[0]


