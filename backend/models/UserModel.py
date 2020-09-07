from django.db import models


class User(models.Model):
    UserName=models.CharField(max_length=32,verbose_name="用户名",unique=True)
    Password=models.CharField(max_length=32,verbose_name="密码")

    class Meta:
        db_table = 'User'
        verbose_name = '用户信息表'
        verbose_name_plural = '用户信息表'
