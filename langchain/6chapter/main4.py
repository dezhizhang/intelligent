import asyncio
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-ifGCp8P1b7mgq2AiJxLDDkZcCjF4KoukEEhzVfpzPufSBJQs",
    base_url="https://poloai.top/v1"
)

question = "介绍一下langchain"

async def main():
    async for event in llm.astream_events(question,version="v2"):
        print(event)

if __name__ == "__main__":
    asyncio.run(main())
