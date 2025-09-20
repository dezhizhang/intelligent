from http.client import responses

from pydantic import BaseModel,Field
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-ifGCp8P1b7mgq2AiJxLDDkZcCjF4KoukEEhzVfpzPufSBJQs",
    base_url="https://poloai.top/v1"
)

class Joke(BaseModel):
    """Joke to tell user."""
    setup: str = Field(..., description="The setup of the joke")
    punchline: str = Field(..., description="The punchline of the joke")
    rating: int = Field(..., description="The rating of the joke")


structed_llm = llm.with_structured_output(Joke)
response = structed_llm.invoke("给我讲一个关于程序员的笑话")
print(response)
