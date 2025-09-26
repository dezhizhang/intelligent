from langchain.document_loaders import UnstructuredMarkdownLoader

file_path = "./test.md"

md_loader = UnstructuredMarkdownLoader(
    file_path,
    strategy="fast"
)

docs = md_loader.load()

print(docs)




