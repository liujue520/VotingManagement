from django.contrib import admin
from .models import ApiInfo,User,Role,Permission
from .models import PermissionRole,RoleUser
# Register your models here.

admin.site.register(ApiInfo)
admin.site.register(User)
admin.site.register(Role)
admin.site.register(Permission)
admin.site.register(PermissionRole)
admin.site.register(RoleUser)