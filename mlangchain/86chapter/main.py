
from langchain.text_splitter import CharacterTextSplitter

text = """
 LangChain 是一个面向 大语言模型（LLM）应用开发的开源框架。目的是帮助开发者 快速搭建智能应用。特别是在 文档问答、知识库、AI 助手、自动化工具 等场景。
"""

splitter = CharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=5,
    separator=" 。"
)

texts = splitter.split_text(text)

# 打印结果
for i,chunk in enumerate(texts):
    print(f"块:{i + 1}:长度:{len(chunk)}")
    print(chunk)


