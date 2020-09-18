from django.contrib import admin
from .models import Role,RoleUser
from .models import PermissionsRole,Permissions
from .models import User
from .models import Project
from django.contrib.auth.models import Permission
from .models import UserInfo
from .models import Rule
from .models import ProjectGroup
from .models import RuleProjectGroup
# Register your models here.

admin.site.register(User)
admin.site.register(Permission)
admin.site.register(Role)
admin.site.register(RoleUser)
admin.site.register(PermissionsRole)
admin.site.register(Permissions)
admin.site.register(Project)
admin.site.register(UserInfo)
admin.site.register(Rule)
admin.site.register(ProjectGroup)
admin.site.register(RuleProjectGroup)
