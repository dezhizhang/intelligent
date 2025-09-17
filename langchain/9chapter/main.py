from langchain_openai import ChatOpenAI


api_key = "sk-ifGCp8P1b7mgq2AiJxLDDkZcCjF4KoukEEhzVfpzPufSBJQs"
base_url = "https://poloai.top/v1"

llm = ChatOpenAI(
    model= "gpt-4o-mini",
    api_key = api_key,
    base_url = base_url,
)

response = llm.invoke("什么是大模型")
print(response)

