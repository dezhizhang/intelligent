from typing import AsyncIterator, Iterator
from langchain_core.runnables import Runnable


class TextTransformer(Runnable):
    def __init__(self, prefix: str = "处理后的文本"):
        self.prefix = prefix

    def invoke(self, input: str) -> str:
        """自定义文本处理逻辑"""
        processed_text = input.upper()
        return f"{self.prefix}{processed_text}"

    async def ainvoke(self, input: str) -> str:
        """异步处理实现"""
        return self.invoke(input)

    def stream(self, input: str) -> Iterator[str]:
        processed_text = input.upper()
        for char in processed_text:
            yield f"{self.prefix}{char}"

    async def astream(self, input: str) -> AsyncIterator[str]:
        processed_text = input.upper()
        for char in processed_text:
            yield f"{self.prefix}{char}"

    async def abatch(self,inputs:list[str]) -> list[str]:
        return [await self.ainvoke(input) for input in inputs]


transform = TextTransformer("结果")
result = transform.invoke("hello world")
print(result)
print("*" * 30)

for chunk in transform.stream("hello world"):
    print(chunk)


