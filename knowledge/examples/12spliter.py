from langchain_text_splitters import MarkdownTextSplitter

docs =  "# Foo\n\n ## Bar\n\nHi this is Jim\n\nHi this is Joe\n\n ### Boo \n\n Hi this is Lance"


headers_to_split_on = [
    ("#","Header 1"),
    ("#","Header 2"),
    ("#","Header 3"),
]


markdown_splitter = MarkdownTextSplitter(headers_to_split_on)
md_header_splits = markdown_splitter.split_text(docs)

print(md_header_splits)
