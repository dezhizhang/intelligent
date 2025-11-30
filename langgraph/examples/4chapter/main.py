from langchain_ollama import OllamaEmbeddings
from langchain_chroma import  Chroma
from langchain_core.documents import Document
from langchain_core.runnables import chain
from typing import List


embedding = OllamaEmbeddings(
    model="nomic-embed-text",
    base_url="http://localhost:11434"
)

vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embedding,
    persist_directory="../chapter/chroma_langchain_db"
)



# 用检索器进行相拟度查询
@chain
def retriever(query:str) -> List[Document]:
    return vector_store.similarity_search(query,k=1)

result = retriever.invoke("What imitations dose Force-aware have?")
print(result)







