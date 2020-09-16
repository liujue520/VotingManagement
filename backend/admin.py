from django.contrib import admin
from .models import Role,RoleUser
from .models import PermissionsRole,Permissions
from .models import User
from django.contrib.auth.models import Permission
# Register your models here.

admin.site.register(User)
admin.site.register(Permission)
admin.site.register(Role)
admin.site.register(RoleUser)
admin.site.register(PermissionsRole)
admin.site.register(Permissions)
