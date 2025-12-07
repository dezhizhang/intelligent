from langchain_community.document_loaders import  TextLoader

loader = TextLoader(file_path="./examples.txt",encoding="utf-8")

document = loader.load()
print(document[0].page_content)


