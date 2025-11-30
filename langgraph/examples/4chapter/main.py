from langchain_ollama import OllamaEmbeddings
from langchain_chroma import  Chroma


embedding = OllamaEmbeddings(
    model="nomic-embed-text",
    base_url="http://localhost:11434"
)

vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embedding,
    persist_directory="../chapter/chroma_langchain_db"
)

# 相拟度查询
result = vector_store.similarity_search(
    "What"
)


for index,result in enumerate(result):
    print(index)
    print(result)




