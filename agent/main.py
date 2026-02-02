import json
from datetime import date
from typing import Literal

import dotenv
from pydantic import BaseModel, Field

dotenv.load_dotenv()


class GetEmployeeInfoInput(BaseModel):
    employee_id: str = Field(..., description="需要查询员工工号")


class SubmitReimbursementInput(BaseModel):
    employee_id: str = Field(..., description="员工工号")
    employee_name: str = Field(..., description="员工姓名")
    submission_date: str = Field(..., description="<UNK>")


class CalculatorInput(BaseModel):
    expression: str = Field(..., description="需要计算的数学表达式")


def get_employee_info(employee_id: str) -> str:
    """概据员工工号查询员工信息，包括姓名和职级"""
    if employee_id == "E12345":
        return json.dumps({"employee_id": "E12345"})
    return json.dumps({"error": "该员工不存在"})

def submit_reimbursement(**kwargs) -> str:
    """提交已填写的报销表单"""
    print(kwargs)
    return json.dumps({"status":"success","message":"报销单提交成功"})

def calculator(expression: str) -> str:
    """一个简单的计算器，可以执行数学表达式"""
    try:
        result = eval(expression)
        return json.dumps({"result":result})
    except Exception as e:
        return json.dumps({"error":str(e)})