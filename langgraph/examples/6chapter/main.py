from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

# 嵌入模型
embedding = OllamaEmbeddings(
    base_url="http://localhost:11434",
    model="qwen3-embedding:4b"
)

# 评份方式
score_measures = [
    "default",
    "cosine",
    "l2",
    "ip"
]

persist_dir = "./chroma_score_db"
vector_stores = []

for score_measure in score_measures:
    collection_metadata = {"hnsw:space": score_measure}
    if score_measure == "default":
        collection_metadata = None

    collection_name = f"my_collection_{score_measure}"
    vector_stores.append(Chroma(
        collection_name = collection_name,
        embedding_function=embedding,
        persist_directory=persist_dir,
        collection_metadata=collection_metadata,
    ))

def indexing(docs):
    print(f"\n加入文档:")
    for vector_store in vector_stores:
        ids = vector_store.add_documents(docs)
        print(f"集合:{vector_store._collection.name}")
        print(ids)

docs = [
    Document(page_content="功能好用户好哈哈"),
    Document(page_content="我国"),
]
indexing(docs)
