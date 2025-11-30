'''
1. 读取PDF, 按照页来管理，Document,List
2. 分割文本
3. 向量化
4. 向量库
'''

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import  Chroma

file_path = "./resume.pdf"

# 读取pdf
loader = PyPDFLoader(file_path)
docs = loader.load()

## 分割文本
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=200,
    add_start_index=True,
)

all_splits = text_splitter.split_documents(docs)

# 向量化

embedding = OllamaEmbeddings(
    model="nomic-embed-text",
    base_url="http://localhost:11434"
)


embedding.embed_query(all_splits[0].page_content)

vector_0 = embedding.embed_query(all_splits[0].page_content)


# 文本向量库
vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embedding,
    persist_directory="./chroma_langchain_db"
)


ids = vector_store.add_documents(documents=all_splits)

print(len(ids))








