from langchain_core.output_parsers import  JsonOutputParser
from langchain_core.prompts import  ChatPromptTemplate
from langchain_openai import  ChatOpenAI

llm = ChatOpenAI(
    model="gpt-3.5-turbo-0613",
    temperature=0.9,
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system","你是一个靠谱的{role}"),
        ("human","{question}")
    ]
)

prompt = chat_prompt_template.invoke(
    input={
        "role":"人工智能专家",
        "question":"人工智能用英文怎么说,问题用q表示，答案用a表示，返回一个json数据"
    }
)

response = llm.invoke(prompt)
parser = JsonOutputParser()
json = parser.invoke(response)

print(json)




