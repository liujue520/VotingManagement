from django.db import models


# Create your models here.

class ApiInfo(models.Model):
    ApiName=models.CharField(max_length=32,verbose_name="接口名称",default="请输入接口名称")
    ApiDescribe=models.TextField(max_length=255,verbose_name="接口描述",default="请输入接口描述")
    ApiManager=models.CharField(max_length=11,verbose_name="接口负责人",default="请输入接口负责人名字")
    CreateTime=models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    UpdateTime = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="修改时间")

    class Meta:
        db_table='ApiInfo'
        verbose_name='接口列表'
        verbose_name_plural="接口列表"

    def __str__(self):
        return self.ApiName





