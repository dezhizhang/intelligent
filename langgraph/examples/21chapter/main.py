from langchain.agents import create_agent
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import  Chroma
from langchain.tools import tool
from dotenv import load_dotenv

load_dotenv()

embedding = OllamaEmbeddings(
    model="nomic-embed-text",
    base_url="http://localhost:11434"
)

# 向量存储
vector_store =Chroma(
    collection_name="rag_collection",
    embedding_function=embedding,
    persist_directory="./chroma_rag_db"
)

@tool(response_format="content_and_artifact")
def retrieve_context(query:str):
    """retrieve information to help answer a query"""
    retrieve_docs = vector_store.similarity_search(query,k=2)
    content = '\n\n'.join(
        (f"Source:{doc.metadata}\n Content:{doc.page_content}") for doc in retrieve_docs
    )
    return content,retrieve_docs

# 系统提示词
system_prompt = """
    你可以使用信息检索工具，回答用户的问题
"""

agent = create_agent(
    model="deepseek:deepseek-chat",
    tools=[retrieve_context],
    system_prompt=system_prompt
)

results = agent.invoke({"messages":[{"role":"user","content":"求职面试：如何巧妙解释离职原因"}]})
messages = results['messages']
print(f"历史消息:{len(messages)} 条")

for message in messages:
    message.pretty_print()


