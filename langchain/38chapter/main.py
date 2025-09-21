
from langchain_core.output_parsers import  CommaSeparatedListOutputParser

output_parser = CommaSeparatedListOutputParser()

format_instructions = output_parser.get_format_instructions()
messages = "大像，猩猩,狮子"
result = output_parser.parse(messages)

print(result)
