from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-ifGCp8P1b7mgq2AiJxLDDkZcCjF4KoukEEhzVfpzPufSBJQs",
    base_url="https://poloai.top/v1"
)

prompt_template = PromptTemplate.from_template(template="你是一个{role},你的名字叫{name}")
prompt = prompt_template.format(role="人工智能专家",name="晓智")

response = llm.invoke(prompt)

print(response.content)

