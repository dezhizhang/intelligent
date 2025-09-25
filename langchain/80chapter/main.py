from langchain_community.document_loaders import TextLoader

filePath = "./test.txt"

text_loader = TextLoader(
    file_path=filePath,
    encoding="utf-8"
)

docs = text_loader.load()
print(docs)




