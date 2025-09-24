from langchain.prompts.chat import ChatPromptTemplate
from langchain_openai import ChatOpenAI

template = "你是一个翻译专家， 擅长将{input_language} 语言飜译成 {output_language}语言"

chat_prompt = ChatPromptTemplate.from_messages([
    ("system",template),
    ("human","{text}")
])

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

messages = chat_prompt.format_messages(input_language="英文",output_language="中文",text="I love large language Model.")

response  = llm.invoke(messages)

print(response.content)







