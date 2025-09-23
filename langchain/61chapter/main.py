from langchain_core.tools import tool

@tool
def add_num(a:int,b:int)-> int:
    """计算两个整数的和"""
    return a + b

print(f"name={add_num.name}")
print(f"args={add_num.args}")
print(f"descript={add_num.description}")
print(f"return_direct={add_num.return_direct}")

print(add_num.invoke({"a":10,"b":20}))