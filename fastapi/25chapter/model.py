from tortoise import fields,models

class Student(models.Model):
    """学生模型，包含基本信息，用于演示表单增册改查操作"""
    id = fields.IntField(pk=True,description="学生id主键")
    name = fields.CharField(max_length=50,description="学生姓名")
    age = fields.IntField(max_length=5,description="学生年龄")
    email = fields.CharField(max_length=50,description="<UNK>")

    class Meta:
        table = "student"

    def __str__(self):
        return self.name