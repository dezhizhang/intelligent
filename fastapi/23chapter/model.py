from tortoise.models import Model

from tortoise.fields import CharField,DateField,BooleanField


class User(Model):
    id = CharField(max_length=36,pk=True)
    username = CharField(max_length=36,unique=True)
    email = CharField(max_length=36,unique=True)
    password = CharField(max_length=36)
    is_active = BooleanField(default=True)
    is_admin = BooleanField(default=False)
    created_at = DateField(auto_now_add=True)
    updated_at = DateField(auto_now=True)
    class Meta:
        table = "user"
        ordering = ['-created_at']

        def __str__(self):
            return self.username