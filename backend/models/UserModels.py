from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def _create_user(self,username,password,email,**kwargs):
        if not username:
            raise ValueError("请传入用户名！")
        if not password:
            raise ValueError("请传入密码！")
        if not email:
            raise ValueError("请传入邮箱地址！")
        user = self.model(username=username,email=email,**kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self,username,password,email,**kwargs):
        kwargs['is_superuser'] = False
        return self._create_user(username,password,email,**kwargs)

    def create_superuser(self,username,password,email,**kwargs):
        kwargs['is_superuser'] = True
        kwargs['is_staff'] = True
        return self._create_user(username,password,email,**kwargs)

class UserTable(AbstractBaseUser,PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=32, verbose_name="用户名", default="请输入用户名",unique=True)
    is_superuser = models.BooleanField(verbose_name="是否超级管理员", default=False)
    is_staff = models.BooleanField(default=True, verbose_name="是否能登录admin后台")
    email = models.EmailField(verbose_name="邮箱", default='请输入邮箱')
    Created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    Update = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    class Meta:
        db_table='UserTable'
        verbose_name='用户列表'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.username


# class User(models.Model):
#     #通用唯一识别码，设置为主键
#     UserId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     UserName = models.CharField(max_length=32,verbose_name="用户名",default="请输入用户名")
#     UserPassword = models.CharField(max_length=256,verbose_name="密码",default="请输入密码")
#     IsSuperuser = models.BooleanField(verbose_name="是否超级管理员",default=False)
#     Created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
#     Update = models.DateTimeField(auto_now=True, verbose_name='更新时间')
#
#     class Meta:
#         db_table='User'
#         verbose_name='用户列表'
#         verbose_name_plural="用户列表"
#
#     def __str__(self):
#         return self.UserName
#
# class Role(models.Model):
#     # 通用唯一识别码，设置为主键
#     RoleId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     RoleName = models.CharField(max_length=32,verbose_name="角色",default="输入角色名")
#     RoleUser = models.ManyToManyField(User,through='RoleUser')
#     Created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
#     Update = models.DateTimeField(auto_now=True, verbose_name='更新时间')
#
#     class Meta:
#         db_table='Role'
#         verbose_name='角色列表'
#         verbose_name_plural="角色列表"
#
#     def __str__(self):
#         return self.RoleName
#
# class RoleUser(models.Model):
#     # 通用唯一识别码，设置为主键
#     RoleUserId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     User = models.ForeignKey(User, on_delete=models.CASCADE)
#     Role = models.ForeignKey(Role, on_delete=models.CASCADE)
#     Created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
#     Update = models.DateTimeField(auto_now=True, verbose_name='更新时间')
#
#     class Meta:
#         db_table='RoleUser'
#         verbose_name='用户角色表'
#         verbose_name_plural="用户角色表"
#
#
#
# class Permission(models.Model):
#     # 通用唯一识别码，设置为主键
#     PermissionId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     PermissionName = models.CharField(verbose_name='权限名称', max_length=32, default="请输入名称")
#     PermissionRole = models.ManyToManyField(Role, through='PermissionRole')
#     Created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
#     Update = models.DateTimeField(auto_now=True, verbose_name='更新时间')
#
#     class Meta:
#         db_table='Permission'
#         verbose_name='权限列表'
#         verbose_name_plural="权限列表"
#
#     def __str__(self):
#         return self.PermissionName
#
# class PermissionRole(models.Model):
#     # 通用唯一识别码，设置为主键
#     PermissionRoleId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     Role= models.ForeignKey(Role, on_delete=models.CASCADE)
#     Permission= models.ForeignKey(Permission, on_delete=models.CASCADE)
#     Created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
#     Update = models.DateTimeField(auto_now=True, verbose_name='更新时间')
#
#     class Meta:
#         db_table='PermissionRole'
#         verbose_name='角色权限表'
#         verbose_name_plural="角色权限表"
