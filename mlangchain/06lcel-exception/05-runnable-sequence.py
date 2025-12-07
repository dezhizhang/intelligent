# from langchain_core.runnables import RunnableLambda, RunnableSequence
#
# def add_one(x: int) -> int:
#     return x + 1
#
#
# def mul_two(x: int) -> int:
#     return x * 2
#
#
# add_one_runnable = RunnableLambda(func=add_one)
# mul_two_runnable = RunnableLambda(func=mul_two)
#
#
# # sequence = RunnableSequence(first=add_one_runnable, last=mul_two_runnable)
#
# sequence = add_one_runnable | mul_two_runnable
# print(sequence.get_graph().draw_ascii())
# print(sequence.invoke(1))
#

from langchain_core.runnables import Runnable, RunnableSequence
from typing import Any, Dict, List


class DataValidator(Runnable):
    def invoke(self, input: Dict[str, Any]) -> Dict[str, Any]:
        """验证输入数据"""
        if "name" not in input or "age" not in input:
            raise ValueError("输入数据少必要字段")
        return input


class AgeTransformer(Runnable):
    def invoke(self, input: Dict[str, Any],config:Any=None) -> Dict[str, Any]:
        return {
            **input,
            "age_group": "青年" if input["age"] < 35 else "中年"
        }


pipeline = DataValidator() | AgeTransformer()

print(pipeline.get_graph().draw_ascii())
print(pipeline.invoke({"name":"tom","age":32}))


