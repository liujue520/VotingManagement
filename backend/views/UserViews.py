from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions
from rest_framework_simplejwt import authentication

# from backend.models import User
# from backend.models import Role
# from backend.models import Permission
# from backend.models import RoleUser
# from backend.models import PermissionRole
# from backend.serializers import User_Serializers
# from backend.serializers import Role_Serializers
# from backend.serializers import Permission_Serializers
# from backend.serializers import Role_User_Serializers
# from backend.serializers import Permission_Role_Serializers
from backend.models import UserTable
from backend.serializers import UserTable_Serializers

class UserTable_ViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    返回一组（查）
    list:
    返回所有组(查)
    create:
    创建新组(增)
    delete:
    删除现有一组(删)
    partial_update:
    更新现有组的一个或多个字段
    update:
    更新一组
    """
    authentication_classes = [authentication.JWTAuthentication]   # jwt用户token自定义登陆认证规则
    permission_classes = [permissions.IsAuthenticated]  # 必须登录

    queryset = UserTable.objects.all()
    serializer_class = UserTable_Serializers

# class User_ViewSet(viewsets.ModelViewSet):
#     """
#     retrieve:
#     返回一组（查）
#     list:
#     返回所有组(查)
#     create:
#     创建新组(增)
#     delete:
#     删除现有一组(删)
#     partial_update:
#     更新现有组的一个或多个字段
#     update:
#     更新一组
#     """
#     authentication_classes = [authentication.JWTAuthentication]   # jwt用户token自定义登陆认证规则
#     permission_classes = [permissions.IsAuthenticated]  # 必须登录
#
#     queryset = User.objects.all()
#     serializer_class = User_Serializers
#
# class Role_ViewSet(viewsets.ModelViewSet):
#     """
#     retrieve:
#     返回一组（查）
#     list:
#     返回所有组(查)
#     create:
#     创建新组(增)
#     delete:
#     删除现有一组(删)
#     partial_update:
#     更新现有组的一个或多个字段
#     update:
#     更新一组
#     """
#     queryset = Role.objects.all()
#     serializer_class = Role_Serializers
#
# class Permission_ViewSet(viewsets.ModelViewSet):
#     """
#     retrieve:
#     返回一组（查）
#     list:
#     返回所有组(查)
#     create:
#     创建新组(增)
#     delete:
#     删除现有一组(删)
#     partial_update:
#     更新现有组的一个或多个字段
#     update:
#     更新一组
#     """
#     queryset = Permission.objects.all()
#     serializer_class = Permission_Serializers
#
# class Role_User_ViewSet(viewsets.ModelViewSet):
#     """
#     retrieve:
#     返回一组（查）
#     list:
#     返回所有组(查)
#     create:
#     创建新组(增) 使用url添加
#     delete:
#     删除现有一组(删)
#     partial_update:
#     更新现有组的一个或多个字段
#     update:
#     更新一组
#     """
#     queryset = RoleUser.objects.all()
#     serializer_class = Role_User_Serializers
#
# class Permission_Role_ViewSet(viewsets.ModelViewSet):
#     """
#     retrieve:
#     返回一组（查）
#     list:
#     返回所有组(查)
#     create:
#     创建新组(增) 使用url添加
#     delete:
#     删除现有一组(删)
#     partial_update:
#     更新现有组的一个或多个字段
#     update:
#     更新一组
#     """
#     queryset = PermissionRole.objects.all()
#     serializer_class = Permission_Role_Serializers