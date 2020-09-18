from django.db import models
import uuid

class Project(models.Model):
    ProjectId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ProjectName = models.CharField(max_length=32, verbose_name="项目名称", default="输入项目名")
    Created = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    Update = models.DateTimeField(auto_now=True,verbose_name='更新时间')
    StartingTime = models.DateField(auto_now=False, auto_now_add=False, verbose_name="开始时间")
    EndTime = models.DateField(auto_now=False, auto_now_add=False, verbose_name="结束时间")
    ProjectNumber = models.IntegerField(verbose_name="项目号", blank=True, auto_created=True,default=None)
    ProjectGroup = models.ForeignKey('ProjectGroup', on_delete=models.CASCADE,default=None)

    class Meta:
        db_table='Project'
        verbose_name='Project_项目表'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.ProjectName


class Rule(models.Model):
    RuleId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    RuleName = models.CharField(max_length=32, verbose_name="规则名", default="规则名")
    Created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    Update = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    class Meta:
        db_table = 'Rule'
        verbose_name = 'Project_规则表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.RuleName

class ProjectGroup(models.Model):
    ProjectGroupId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ProjectGroupName = models.CharField(max_length=32, verbose_name="项目组名", default="项目组名")
    Rule = models.ManyToManyField(Rule, through='RuleProjectGroup')
    Created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    Update = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table='ProjectGroup'
        verbose_name='Project_项目组表'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.ProjectGroupName

class RuleProjectGroup(models.Model):
    RuleProjectGroupId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Rule= models.ForeignKey(Rule, on_delete=models.CASCADE)
    ProjectGroup= models.ForeignKey(ProjectGroup, on_delete=models.CASCADE)
    Created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    Update = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    class Meta:
        db_table='RuleProjectGroup'
        verbose_name='Project_规则组表'
        verbose_name_plural=verbose_name