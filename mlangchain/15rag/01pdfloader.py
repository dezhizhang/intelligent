# import asyncio
# from langchain_community.document_loaders import PyPDFLoader

# async def load_pdf():
#     file_path = "deepseek.pdf"
#     loader = PyPDFLoader(file_path)
#     pages = []
#     async for page in loader.alazy_load():
#         pages.append(page)
#     return pages
#
# # 运行异步函数
# pages = asyncio.run(load_pdf())
# print(pages)

import asyncio
from langchain_community.document_loaders import PyPDFLoader

async def load_pdf():
    file_path = "deepseek.pdf"
    loader = PyPDFLoader(file_path)

    pages = []
    async for page in loader.alazy_load():
        pages.append(page)
    return pages

pages = asyncio.run(load_pdf())
print(pages)

