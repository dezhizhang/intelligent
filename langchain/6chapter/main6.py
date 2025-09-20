from langchain_openai import ChatOpenAI
from typing import Optional,Union
from typing_extensions import Annotated,TypedDict


llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-ifGCp8P1b7mgq2AiJxLDDkZcCjF4KoukEEhzVfpzPufSBJQs",
    base_url="https://poloai.top/v1"
)

class Joke(TypedDict):
    """Joke to tell user."""
    setup: Annotated[str,..., "The setup of the joke."]
    punchline: Annotated[str,..., "The punchline of the joke."]
    rating: Annotated[Optional[Union[int,float]], "The rating of the joke."]

structured_llm = llm.with_structured_output(Joke)
for chunk in structured_llm.stream("给我讲一个关于程序员的笑话"):
    print(chunk)

