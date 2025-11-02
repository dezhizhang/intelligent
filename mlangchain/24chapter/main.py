

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

import os
import dotenv
dotenv.load_dotenv()

llm = ChatOpenAI(
    model=os.getenv("OPENAI_BASE_MODEL"),
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY")
)

template = PromptTemplate.from_template(
    template="请评价{product}的质量,包括{aspect1}和{aspect2}"
)

prompt = template.invoke(input={"product":"智能手机","aspect1":"电池续航","aspect2":"拍照质量"})
response = llm.invoke(prompt)

print(response)
















