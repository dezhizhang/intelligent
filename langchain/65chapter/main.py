
from langchain_openai import  ChatOpenAI

from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)

system_message_prompt = SystemMessagePromptTemplate.from_template(
    "你是一个翻译专家，擅长将{input_language} 语言翻译成 {output_language}语言"
)

human_message_prompt = HumanMessagePromptTemplate.from_template(
    "{text}"
)

prompt_template = ChatPromptTemplate.from_messages(
    [
        system_message_prompt,
        human_message_prompt
    ]
)

prompt = prompt_template.format_prompt(
    input_language = "英文",
    output_language = "中文",
    text = "I love large langchain Model."
).to_messages()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM",
    base_url="https://poloai.top/v1"
)

response = llm.invoke(prompt)
print(response.content)





