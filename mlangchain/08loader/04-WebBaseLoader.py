from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader(web_paths='https://aint.top/strategy/detail?slug=6756d13981739f25f2a02ec8')

documents = loader.load()

print(documents)