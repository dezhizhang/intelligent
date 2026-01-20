from typing import Optional
from pydantic import BaseModel,Field
from langchain_openai import ChatOpenAI


llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

class Joke(BaseModel):
    """Joke to tell user"""
    setup: str = Field(description="Joker setup of the joke")
    punchline:str = Field(description="The punchline to the joke")
    roting:Optional[int] = Field(
        default=None,
        description="How funny the joke is from 1 to 10"
    )

structured_llm = llm.with_structured_output(Joke)
response = structured_llm.invoke("给我讲一个关于程序员的笑话")
print(response)


