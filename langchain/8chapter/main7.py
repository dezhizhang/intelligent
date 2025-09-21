# from langchain_core.prompts import PromptTemplate

# prompt = PromptTemplate.from_template("{foo}1212{bar}")
# partial_prompt = prompt.partial(foo="foo")
# print(partial_prompt.format(bar="baz"))


from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template("{foo}1212{bar}")
partial_prompt = prompt.partial(foo="foo")
print(partial_prompt.format(bar="baz"))

