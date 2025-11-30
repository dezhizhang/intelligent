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

print(vector_store)




