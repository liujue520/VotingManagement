from rest_framework import serializers
# from backend.models import User
# from backend.models import Role
# from backend.models import Permission
# from backend.models import RoleUser
# from backend.models import PermissionRole
from backend.models import UserTable

class UserTable_Serializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserTable
        fields = "__all__"

# class User_Serializers(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = "__all__"
#
# class Role_Serializers(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Role
#         fields = "__all__"
#
# class Permission_Serializers(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Permission
#         fields = "__all__"
#
# class Role_User_Serializers(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model=RoleUser
#         fields="__all__"
#
# class Permission_Role_Serializers(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model=PermissionRole
#         fields="__all__"
