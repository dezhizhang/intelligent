import shutil

from langchain_community.document_loaders import WebBaseLoader
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
import bs4
from langchain_chroma import Chroma
import os
import shutil

if os.path.exists("./chroma_rag_db"):
    shutil.rmtree("./chroma_rag_db")

page_url = "https://aint.top/strategy/detail?slug=6756d13981739f25f2a02ec8"

bs4_strainer = bs4.SoupStrainer()

loader = WebBaseLoader(
    web_paths=(page_url,),
    bs_kwargs={"parse_only": bs4_strainer}
)

docs = loader.load()
print(len(docs))
print(type(docs[0]))
print(docs[0])

# 分割文档
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=200,
    add_start_index=True
)

all_splits = text_splitter.split_documents(docs)

embedding = OllamaEmbeddings(
    model="nomic-embed-text",
    base_url="http://localhost:11434"
)
# 向量化
vector_store = Chroma(
    collection_name="rag_collection",
    embedding_function=embedding,
    persist_directory="./chroma_rag_db"
)

ids = vector_store.add_documents(documents=all_splits)
print(ids)
