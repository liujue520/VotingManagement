from django.contrib import admin
from .models import User,Role,Permission
from .models import PermissionRole,RoleUser
from .models import UserTable
# Register your models here.

admin.site.register(UserTable)
# admin.site.register(User)
# admin.site.register(Role)
# admin.site.register(Permission)
# admin.site.register(PermissionRole)
# admin.site.register(RoleUser)