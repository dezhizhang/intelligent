from langchain_community.document_loaders import Docx2txtLoader


loader = Docx2txtLoader(file_path='examples.docx')

document = loader.load()

for i,doc in enumerate(document):
    print(f'文档片段{i + 1},文档内容:{doc}')
