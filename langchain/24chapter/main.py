
from langchain_core.prompts import PromptTemplate

template = (
    PromptTemplate.from_template("tell me joke about {topic} ") + "{langchain}"
)


prompt = template.format(topic="sports",langchain="spanish")
print(prompt)


