# from pydantic import BaseModel,Field
#
# from langchain_openai import ChatOpenAI
#
# class add(BaseModel):
#     """add to integers"""
#     a:int = Field(...,description="first integer")
#     b:int = Field(...,description="second integer")
#
# class multiply(BaseModel):
#     """multiply two integers"""
#     a:int = Field(...,description="first integer")
#     b:int = Field(...,description="second integer")
#
# llm = ChatOpenAI(
#     temperature=0.8,
#     model="gpt-4o-mini",
#     api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
#     base_url="https://poloai.top/v1"
# )
#
# tools = [add, multiply]
# llm_width_tools = llm.bind_tools(tools)
# query = "3乘以12是多少"
# response = llm_width_tools.invoke(query).tool_calls
# print(response)




