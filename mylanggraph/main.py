from bs4 import BeautifulSoup as Soup
from langchain_community.document_loaders.recursive_url_loader import  RecursiveUrlLoader

url = "https://python.langchain.com/docs/concepts/lcel/"

loader = RecursiveUrlLoader(
    url=url,
    max_depth=30,
    extractor= lambda x:Soup(x,"html.parser").text
)

docs = loader.load()
d_sorted = sorted(docs, key=lambda x: x.metadata['source'])
d_reversed = list(reversed(d_sorted))

concatenated_content = "\n\n\n --- \n\n\n".join(
    [doc.page_content for doc in d_reversed]
)

print(concatenated_content)

# 设置大模型




