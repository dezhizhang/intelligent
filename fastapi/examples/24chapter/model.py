from  tortoise.models import Model
from tortoise.fields import CharField, DateField, BooleanField, IntField


class User(Model):
    id = CharField(max_length=35,pk=True)
    age = IntField(default=0)
    username = CharField(max_length=50,unique=True)
    email = CharField(max_length=255,unique=True)
    is_active = BooleanField(default=True)

    created_at = DateField(auto_now_add=True)
    updated_at = DateField(auto_now=True)

    class Meta:
        table = "user"
        # 创建联合唯一索引
        unique_together = ("id", "username")
        # 排序降序
        ordering = ['-created_at']
