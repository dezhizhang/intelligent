from langchain_community.document_loaders import  WebBaseLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
import bs4


loader = WebBaseLoader(
    web_path="https://www.gov.cn/xinwen/2020-06/01/content_5516649.htm",
    bs_kwargs = dict(parse_only=bs4.SoupStrainer(id="UCAP-CONTENT"))
)

docs = loader.load()

# 定义向量数据库
embeddings = OpenAIEmbeddings()

# 使用分器
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
documents = text_splitter.split_documents(docs)
print(len(documents))







