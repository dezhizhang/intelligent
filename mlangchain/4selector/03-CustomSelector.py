from typing import Any, Dict, List
from langchain_core.example_selectors import BaseExampleSelector
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate


class CustomSelector(BaseExampleSelector):
    """医疗示例选择器"""

    def __init__(self, examples: List[dict[str, str]]):
        """
            初始化医疗示例选择器
            :param examples: 医疗相关的示列列表，每个示例是一个字典，包含输入和输出
        """
        self.examples = examples

    def add_example(self, example: dict[str, str]) -> Any:
        """将示例添加到存储中的键"""
        self.examples.append(example)

    def select_examples(self, input_variables: dict[str, str]) -> List[dict[str, str]]:
        """
        根据输入变量选择医疗示例
        :param input_variables: 包含选择条件(如疾病名称、症获等)的字典
        :return:符合条件的示列表
        """

        disease_name = input_variables.get("disease_name", None)
        if disease_name is None:
            return []
        selected_examples = [
            example for example in self.examples
            if disease_name.lower() in example['input'].lower()
        ]
        return selected_examples


# 示例数据,模拟数据库存放时数据

examples = [
    {"input": "流感症状", "output": "发烧、咳嗽、喉咙痛、身体酸痛。"},
    {"input": "糖尿病治疗", "output": "饮食控制、运动、药物"},
    {"input": "新冠肺炎症状", "output": "发烧、咳嗽、疲劳、味觉或嗅觉丧失。"},
    {"input": "糖尿病症状", "output": "口渴、尿频、体重减轻。"}
]


custom_selector = CustomSelector(examples)
selected_examples = custom_selector.select_examples({"disease_name":"糖尿病"})
print(selected_examples)

