from langchain_openai import OpenAIEmbeddings

llm = OpenAIEmbeddings(
    model="text-embedding-ada-002",
    api_key="sk-ifGCp8P1b7mgq2AiJxLDDkZcCjF4KoukEEhzVfpzPufSBJQs",
    base_url="https://poloai.top/v1"
)

response = llm.embed_query("我是文档中的数据")
print(response)
