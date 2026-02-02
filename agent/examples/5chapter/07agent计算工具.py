import json
import os

import dotenv
from openai import OpenAI
dotenv.load_dotenv()

def calculator(expression:str) -> str:
    """一个简单的计算器，可以执行数学表达式"""
    try:
        result = eval(expression)
        return json.dumps({"result":result})
    except Exception as e:
        return json.dumps({'error': f"无效表达式，错误信息{str(e)}"})


class ReActAgent:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url=os.getenv("OPENAI_API_BASE_URL"),
        )
        self.messages = [
            {
                "role":"system",
                "content":"你是一个强大的聊天机器人，请概据用户的提高进行答复，如果需要工具请直接调用"
            }
        ]
        self.model = "deepseek-chat"
        self.available_tools = {"calculator":calculator}
        self.tools = [
            {
                "type":"function",
                "function":{
                    "name":"calculator",
                    "description":"一个简单的计算器，可以执行数学表达式",
                    "parameters":{
                        "type":"object",
                        "properties":{
                            "expression":{
                                "type":"string",
                                "description":"需要计算的表过式，例如:'123+456'"
                            }
                        }
                    },
                    "required": ["expression"]
                },
            }
        ]


    def process_query(self,query:str) -> str:
        """使用deepseek处理用户输入"""
        self.messages.append({"role":"user","content":query})

        # 调起deepseek发起请求
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages,
            tools=self.tools,
        )

        # 获取响应消息+工具响应
        response_message = response.choices[0].message
        tool_calls = response_message.tool_calls


        # 判断是否执行工具调用
        if tool_calls:
            # 将模型第一次回复添加到历史消息中
            self.messages.append(response_message.model_dump())

            # 循环执行工具调用
            for tool_calls in tool_calls:
                print("tool_calls",tool_calls.function.name)
                tool_name = tool_calls.function.name
                tool_args =json.loads(tool_calls.function.arguments)
                function_to_call = self.available_tools[tool_name]

                # 调用式具
                result = function_to_call(**tool_args)
                print(f"Tool [{tool_name}] result : {result}]")

                # 将工具结果添加到历史消息中
                self.messages.append({
                    "tool_call_id":tool_calls.id,
                    "role":"tool",
                    "name":tool_name,
                    "content":result
                })

            # 再次调用模型
            second_response = self.client.chat.completions.create(
                model=self.model,
                messages=self.messages,
                tools=self.tools,
                tool_choice="none"
            )
            self.messages.append(second_response.choices[0].message.model_dump())
            return "Assistant:" + second_response.choices[0].message.content
        else:
            return "Assistant:" + response.choices[0].message.content

    def chat_loop(self):
        """运行循环对话"""
        while True:
            try:
                # 获取用户输入
                query = input("\nQuery").strip()
                if query.lower() == "exit":
                    break
                print(self.process_query(query))
            except Exception as e:
                print(e)


if __name__ == '__main__':
    ReActAgent().chat_loop()


