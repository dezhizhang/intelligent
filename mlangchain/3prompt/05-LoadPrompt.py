from langchain_core.prompts import load_prompt
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

prompt_template = load_prompt("08-prompt.json")

prompt = prompt_template.invoke({"name":"tom","who":"猎"})

response = llm.invoke(prompt)
print(response)


