
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

llm = ChatOpenAI(
    model="deepseek-chat",
    api_key="sk-ad2baecfde824382bbd93423a405e0df",
    base_url="https://api.deepseek.com"
)

prompt = PromptTemplate.from_template("你是一名起名大师，请模防示例起3个{county}名字，比如男孩经常被叫{boy}，女孩经常被叫{girl}")
message = prompt.format(county="中国特色", boy="狗蛋", girl="小花")

print(message)
response = llm.invoke(message)
print(response)


