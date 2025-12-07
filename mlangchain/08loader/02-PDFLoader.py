from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(file_path="examples.pdf")

document = loader.load()

for i,doc in enumerate(document):
    print(f'文档片段:{i + 1} 内容:{doc}')
