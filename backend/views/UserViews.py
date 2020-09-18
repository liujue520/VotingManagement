from django.contrib.auth.hashers import make_password

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions


from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from backend.permissions import Superuser_Permission

from backend.models import User
from backend.models import Role
from backend.models import RoleUser
from backend.models import Permissions
from backend.models import PermissionsRole
from backend.models import UserInfo

from backend.serializers import User_Serializers
from backend.serializers import Role_Serializers
from backend.serializers import Role_User_Serializers
from backend.serializers import Permissions_Serializers
from backend.serializers import Permissions_Role_Serializers
from backend.serializers import UserInfo_Serializers

class User_ViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    条件1.在Token必须填入token接口中反回的access参数，如果失效用refresh重新请求/token/refresh/
    条件2 在Token接口中使用的用户必须是超级管理员
    返回一组（查）
    list:
    条件1.在Token必须填入token接口中反回的access参数，如果失效用refresh重新请求/token/refresh/
    条件2 在Token接口中使用的用户必须是超级管理员
    返回所有组(查)
    create:
    条件1.在Token必须填入token接口中反回的access参数，如果失效用refresh重新请求/token/refresh/
    条件2 在Token接口中使用的用户必须是超级管理员
    创建新组(增) 可以创建新的超级管理员
    groups字段与user_permissions必须为空
    delete:
    条件1.在Token必须填入token接口中反回的access参数，如果失效用refresh重新请求/token/refresh/
    条件2 在Token接口中使用的用户必须是超级管理员
    删除现有一组(删)
    partial_update:
    条件1.在Token必须填入token接口中反回的access参数，如果失效用refresh重新请求/token/refresh/
    条件2 在Token接口中使用的用户必须是超级管理员
    groups字段与user_permissions保持不变
    更新现有组的一个或多个字段
    update:
    条件1.在Token必须填入token接口中反回的access参数，如果失效用refresh重新请求/token/refresh/
    条件2 在Token接口中使用的用户必须是超级管理员
    groups字段与user_permissions保持不变
    更新一组
    """
    # authentication_classes = [JWTAuthentication]   # jwt用户token自定义登陆认证规则
    # permission_classes = [permissions.IsAuthenticated]  # 必须登录+必须是超级管理员
    permission_classes = [Superuser_Permission]  # 必须是超级管理员
    queryset = User.objects.all()
    serializer_class = User_Serializers

    #重构create函数
    def create(self, request, *args, **kwargs):

        request.data['password']=make_password(request.data['password'])#将密码哈希化
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class UserInfo_ViewSet(viewsets.ModelViewSet):
    """
         retrieve:
         条件1.在Token必须填入token接口中反回的access参数，如果失效用refresh重新请求/token/refresh/
         条件2 在Token接口中使用的用户必须是超级管理员
         返回一组（查）
         list:
         条件1.在Token必须填入token接口中反回的access参数，如果失效用refresh重新请求/token/refresh/
         条件2 在Token接口中使用的用户必须是超级管理员
         返回所有组(查)
         create:
         条件1.在Token必须填入token接口中反回的access参数，如果失效用refresh重新请求/token/refresh/
         条件2 在Token接口中使用的用户必须是超级管理员
         字段*UserId*必须填写User表中存在的字段username，绑定username字段与UserId
         delete:
         条件1.在Token必须填入token接口中反回的access参数，如果失效用refresh重新请求/token/refresh/
         条件2 在Token接口中使用的用户必须是超级管理员
         删除现有一组(删)
         partial_update:
         条件1.在Token必须填入token接口中反回的access参数，如果失效用refresh重新请求/token/refresh/
         条件2 在Token接口中使用的用户必须是超级管理员
         groups字段与user_permissions保持不变
         更新现有组的一个或多个字段
         update:
         条件1.在Token必须填入token接口中反回的access参数，如果失效用refresh重新请求/token/refresh/
         条件2 在Token接口中使用的用户必须是超级管理员
         groups字段与user_permissions保持不变
         更新一组
         """
    permission_classes = [Superuser_Permission]  # 必须是超级管理员
    queryset = UserInfo.objects.all()
    serializer_class = UserInfo_Serializers

class Role_ViewSet(viewsets.ModelViewSet):
    """
        retrieve:
        条件1.在Token必须填入token接口中反回的access参数，如果失效用refresh重新请求/token/refresh/
        条件2 在Token接口中使用的用户必须是超级管理员
        返回一组（查）
        list:
        条件1.在Token必须填入token接口中反回的access参数，如果失效用refresh重新请求/token/refresh/
        条件2 在Token接口中使用的用户必须是超级管理员
        返回所有组(查)
        create:
        条件1.在Token必须填入token接口中反回的access参数，如果失效用refresh重新请求/token/refresh/
        条件2 在Token接口中使用的用户必须是超级管理员
        delete:
        条件1.在Token必须填入token接口中反回的access参数，如果失效用refresh重新请求/token/refresh/
        条件2 在Token接口中使用的用户必须是超级管理员
        删除现有一组(删)
        partial_update:
        条件1.在Token必须填入token接口中反回的access参数，如果失效用refresh重新请求/token/refresh/
        条件2 在Token接口中使用的用户必须是超级管理员
        groups字段与user_permissions保持不变
        更新现有组的一个或多个字段
        update:
        条件1.在Token必须填入token接口中反回的access参数，如果失效用refresh重新请求/token/refresh/
        条件2 在Token接口中使用的用户必须是超级管理员
        groups字段与user_permissions保持不变
        更新一组
        """
    permission_classes = [Superuser_Permission]  # 必须是超级管理员
    queryset = Role.objects.all()
    serializer_class = Role_Serializers

class Role_User_ViewSet(viewsets.ModelViewSet):
    """
         retrieve:
         条件1.在Token必须填入token接口中反回的access参数，如果失效用refresh重新请求/token/refresh/
         条件2 在Token接口中使用的用户必须是超级管理员
         返回一组（查）
         list:
         条件1.在Token必须填入token接口中反回的access参数，如果失效用refresh重新请求/token/refresh/
         条件2 在Token接口中使用的用户必须是超级管理员
         返回所有组(查)
         create:
         条件1.在Token必须填入token接口中反回的access参数，如果失效用refresh重新请求/token/refresh/
         条件2 在Token接口中使用的用户必须是超级管理员
         delete:
         条件1.在Token必须填入token接口中反回的access参数，如果失效用refresh重新请求/token/refresh/
         条件2 在Token接口中使用的用户必须是超级管理员
         删除现有一组(删)
         partial_update:
         条件1.在Token必须填入token接口中反回的access参数，如果失效用refresh重新请求/token/refresh/
         条件2 在Token接口中使用的用户必须是超级管理员
         groups字段与user_permissions保持不变
         更新现有组的一个或多个字段
         update:
         条件1.在Token必须填入token接口中反回的access参数，如果失效用refresh重新请求/token/refresh/
         条件2 在Token接口中使用的用户必须是超级管理员
         groups字段与user_permissions保持不变
         更新一组
         """
    permission_classes = [Superuser_Permission]  # 必须是超级管理员
    queryset = RoleUser.objects.all()
    serializer_class = Role_User_Serializers

class Permissions_ViewSet(viewsets.ModelViewSet):
    """
         retrieve:
         条件1.在Token必须填入token接口中反回的access参数，如果失效用refresh重新请求/token/refresh/
         条件2 在Token接口中使用的用户必须是超级管理员
         返回一组（查）
         list:
         条件1.在Token必须填入token接口中反回的access参数，如果失效用refresh重新请求/token/refresh/
         条件2 在Token接口中使用的用户必须是超级管理员
         返回所有组(查)
         create:
         条件1.在Token必须填入token接口中反回的access参数，如果失效用refresh重新请求/token/refresh/
         条件2 在Token接口中使用的用户必须是超级管理员
         delete:
         条件1.在Token必须填入token接口中反回的access参数，如果失效用refresh重新请求/token/refresh/
         条件2 在Token接口中使用的用户必须是超级管理员
         删除现有一组(删)
         partial_update:
         条件1.在Token必须填入token接口中反回的access参数，如果失效用refresh重新请求/token/refresh/
         条件2 在Token接口中使用的用户必须是超级管理员
         groups字段与user_permissions保持不变
         更新现有组的一个或多个字段
         update:
         条件1.在Token必须填入token接口中反回的access参数，如果失效用refresh重新请求/token/refresh/
         条件2 在Token接口中使用的用户必须是超级管理员
         groups字段与user_permissions保持不变
         更新一组
         """
    permission_classes = [Superuser_Permission]  # 必须是超级管理员
    queryset = Permissions.objects.all()
    serializer_class = Permissions_Serializers

class Permissions_Role_ViewSet(viewsets.ModelViewSet):
    """
         retrieve:
         条件1.在Token必须填入token接口中反回的access参数，如果失效用refresh重新请求/token/refresh/
         条件2 在Token接口中使用的用户必须是超级管理员
         返回一组（查）
         list:
         条件1.在Token必须填入token接口中反回的access参数，如果失效用refresh重新请求/token/refresh/
         条件2 在Token接口中使用的用户必须是超级管理员
         返回所有组(查)
         create:
         条件1.在Token必须填入token接口中反回的access参数，如果失效用refresh重新请求/token/refresh/
         条件2 在Token接口中使用的用户必须是超级管理员
         delete:
         条件1.在Token必须填入token接口中反回的access参数，如果失效用refresh重新请求/token/refresh/
         条件2 在Token接口中使用的用户必须是超级管理员
         删除现有一组(删)
         partial_update:
         条件1.在Token必须填入token接口中反回的access参数，如果失效用refresh重新请求/token/refresh/
         条件2 在Token接口中使用的用户必须是超级管理员
         groups字段与user_permissions保持不变
         更新现有组的一个或多个字段
         update:
         条件1.在Token必须填入token接口中反回的access参数，如果失效用refresh重新请求/token/refresh/
         条件2 在Token接口中使用的用户必须是超级管理员
         groups字段与user_permissions保持不变
         更新一组
         """
    permission_classes = [Superuser_Permission]  # 必须是超级管理员
    queryset = PermissionsRole.objects.all()
    serializer_class = Permissions_Role_Serializers