from langchain_openai import  OpenAIEmbeddings

embedding_model = OpenAIEmbeddings(
    model="text-embedding-004",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

text = "langchain"
query = embedding_model.embed_query(text=text)

print(query)


