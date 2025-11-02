
from langchain_openai import ChatOpenAI
import os
import dotenv

dotenv.load_dotenv()

llm = ChatOpenAI(
    model=os.getenv("OPENAI_BASE_MODEL"),
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY")
)

response = llm.invoke("什么是langchain")
print(response.content)




