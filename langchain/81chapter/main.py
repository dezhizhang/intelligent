from langchain.document_loaders import PyPDFLoader

file_path = "./hello.pdf"

# 定义加载器
pdfLoader = PyPDFLoader(file_path)

# 加载
docs = pdfLoader.load()
print(docs)





