
#
# from langchain_core.output_parsers import JsonOutputParser
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_openai import ChatOpenAI
#
# llm = ChatOpenAI(
#     model="gpt-4o-mini",
#     api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
#     base_url="https://poloai.top/v1"
# )
#
# prompt_template = ChatPromptTemplate.from_messages([
#     ("system","你是一个告谱的{role}"),
#     ("human","{question}")
# ])
#
# prompt = prompt_template.invoke(input={"role":"人工智能专家","question":"人工智能用英文怎么说?问题用q表示，答案用a表示返回json格式数据"})
#
#
#
# parser = JsonOutputParser()
#
# response = llm.invoke(prompt)
#
# json_result = parser.invoke(response)
# print(json_result)













