
from langchain_core.runnables import RunnableLambda

def multiply(a:int,b:int) -> int:
    return a * b

def multiply_dict_wrapper(inputs:dict):
    return multiply(inputs['a'],inputs['b'])

runnable_multiply = RunnableLambda(multiply_dict_wrapper)
print(runnable_multiply.invoke({"a":2,"b":3}))



