from langchain_huggingface import HuggingFaceEmbeddings


embedding_path = 'bge-large-zh-v1.5';

embeddings = HuggingFaceEmbeddings(model=embedding_path)
vector = embeddings.embed_query("你好，中国")
print(vector)
