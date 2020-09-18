from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def _create_user(self,username,password,**kwargs):
        if not username:
            raise ValueError("请传入用户名！")
        if not password:
            raise ValueError("请传入密码！")

        user = self.model(username=username,**kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self,username,password,**kwargs):
        kwargs['is_superuser'] = False
        return self._create_user(username,password,**kwargs)

    def create_superuser(self,username,password,**kwargs):
        kwargs['is_superuser'] = True
        kwargs['is_staff'] = True
        return self._create_user(username,password,**kwargs)

#继承AbstractBaseUser设计用户表
class User(AbstractBaseUser,PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=32, verbose_name="用户名", default="请输入用户名",unique=True)
    is_superuser = models.BooleanField(verbose_name="是否超级管理员", default=False)
    is_staff = models.BooleanField(default=True, verbose_name="是否能登录admin后台")
    Created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    Update = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    USERNAME_FIELD = 'username'

    objects = UserManager()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    class Meta:
        db_table='UserTable'
        verbose_name='User_用户表'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.username

#用户信息
class UserInfo(models.Model):
    UserInfoId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Company = models.CharField(max_length=32,verbose_name="公司",default="输入公司名")
    SecondaryOrganization = models.CharField(max_length=32,verbose_name="二级组织",default="输入二级组织名")
    TertiaryOrganization = models.CharField(max_length=32,verbose_name="三级组织",default="输入三级组织名")
    FourOrganization = models.CharField(max_length=32,verbose_name="四级组织",default="输入四级组织名")
    FiveOrganization = models.CharField(max_length=32,verbose_name="五级组织",default="输入五级组织名")
    FileNumber = models.CharField(max_length=32,verbose_name="档案号",default="输入档案号")
    EntryDate = models.DateField(auto_now = False,auto_now_add =False,verbose_name="入职时间")
    sex = models.BooleanField(max_length=1, choices=((0, '男'), (1, '女'),), default=0,verbose_name='性别')
    UserId = models.ForeignKey(to="User", on_delete=models.CASCADE)
    class Meta:
        db_table='UserInfo'
        verbose_name='User_用户信息表'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.FileNumber

#角色表
class Role(models.Model):
    # 通用唯一识别码，设置为主键
    RoleId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    RoleName = models.CharField(max_length=32,verbose_name="角色",default="输入角色名")
    RoleUser = models.ManyToManyField(User,through='RoleUser')
    Created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    Update = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table='Role'
        verbose_name='User_角色表'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.RoleName

#中间表用户角色表
class RoleUser(models.Model):
    # 通用唯一识别码，设置为主键
    RoleUserId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Role = models.ForeignKey(Role, on_delete=models.CASCADE)
    Created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    Update = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table='RoleUser'
        verbose_name='User_用户角色表'
        verbose_name_plural=verbose_name

class Permissions(models.Model):
    # 通用唯一识别码，设置为主键
    PermissionId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    PermissionName = models.CharField(verbose_name='权限名称', max_length=32, default="请输入名称")
    PermissionRole = models.ManyToManyField(Role, through='PermissionsRole')
    Created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    Update = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table='Permission'
        verbose_name='User_权限表'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.PermissionName

class PermissionsRole(models.Model):
    # 通用唯一识别码，设置为主键
    PermissionRoleId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Role= models.ForeignKey(Role, on_delete=models.CASCADE)
    Permission= models.ForeignKey(Permissions, on_delete=models.CASCADE)
    Created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    Update = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table='PermissionRole'
        verbose_name='User_角色权限表'
        verbose_name_plural=verbose_name
