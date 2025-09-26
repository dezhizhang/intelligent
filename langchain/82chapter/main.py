from langchain_community.document_loaders import JSONLoader

file_path = "./test.json"

json_loader = JSONLoader(
    file_path=file_path,
    jq_schema=".",
    text_content=False
)

docs = json_loader.load()
print(docs)
