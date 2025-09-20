
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_openai import OpenAIEmbeddings

llm = OpenAIEmbeddings(
    model="text-embedding-ada-002",
    api_key="sk-ifGCp8P1b7mgq2AiJxLDDkZcCjF4KoukEEhzVfpzPufSBJQs",
    base_url="https://poloai.top/v1"
)

examples = [
    {
        "question": "谁活得更久,穆罕默德·阿里还是艾伦·图灵?",
        "answer": """
        接下来还需要问什么问题吗?
        追问:穆罕默德·阿里去世时多大年纪?
        中间答案:穆罕默德·阿里去世时享年74岁""",
    },
    {
        "question": "craigslist的创始人是什么时候出生的?",
        "answer": """
        接下来还需要问什么问题吗?
        追问:谁是craigslist的创始人?
        中级答案:Craigslist是由克雷格·纽马克创立的。"""
    },
    {
        "question":"谁是乔治·华盛顿的外祖父?",
        "answer": """
        接下来还需要问什么问题吗?
        追问:谁是乔治·华盛顿的母亲?
        中间答案:乔治·华盛顿的母亲是玛丽·鲍尔·华盛顿。"""
    },
    {
        "question":"《大白鲨》和《皇家赌场》的导演都来自同一个国家吗?",
        "answer":"""接下来还需要问什么问题吗?
        追问:《大白鲨》的导演是谁?
        中级答案:
        《大白鲨》的导演是史蒂文·斯皮尔伯格"""
    }
]

# examples_selector = SemanticSimilarityExampleSelector.from_examples(
#     examples,
#     embeddings_modeel=llm,
#     Chroma,
#      k = 1,
# )
