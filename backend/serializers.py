from rest_framework import serializers


from backend.models import Role
from backend.models import RoleUser
from backend.models import Permissions
from backend.models import PermissionsRole
from backend.models import User
from backend.models import UserInfo

from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission

class User_Serializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class Role_Serializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"

class Role_User_Serializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=RoleUser
        fields="__all__"

class Permissions_Serializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permissions
        fields = "__all__"


class Permissions_Role_Serializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=PermissionsRole
        fields="__all__"

class UserInfo_Serializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=UserInfo
        fields="__all__"