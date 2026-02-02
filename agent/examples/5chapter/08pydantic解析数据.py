# from pydantic import BaseModel,Field,EmailStr
#
#
# class UserInfo(BaseModel):
#     """传递用户的信息进行数据提取&处理，涵盖name,age,email等"""
#     name:str = Field(...,description="用户名字")
#     age:int = Field(...,description="用户年龄，必须是正整数")
#     email:EmailStr = Field(...,description="用户电子邮件")
#
#
# json_string = '{"name":"张三","age":25,"email":"1541609448@qq.com"}'
#
# try:
#     user = UserInfo.model_validate_json(json_string)
#
#     print(f"解析成功f:{user}")
# except Exception as e:
#     print(e)


from pydantic import BaseModel,Field,field_validator

class User(BaseModel):
    name:str

    @classmethod
    @field_validator("name")
    def validate_name(cls, value:str) -> str:
        if "admin" in value.lower():
            raise ValueError("用户名不能包含admin")
        return value.title()


user = User(name="test_admin")
user_ok = User(name="test_json")
print(user)
print(user_ok)