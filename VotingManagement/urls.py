"""VotingManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path,include,re_path

from rest_framework import routers,permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

from backend import views


router = routers.DefaultRouter()

router.register('User',views.User_ViewSet)
router.register('Role',views.Role_ViewSet)
router.register('Permissions',views.Permissions_ViewSet)
router.register('Role_User',views.Role_User_ViewSet)
router.register('Permissions_Role',views.Permissions_Role_ViewSet)
router.register('UserInfo',views.UserInfo_ViewSet)

schema_view=get_schema_view(
    # 具体定义详见 [Swagger/OpenAPI 规范](https://swagger.io/specification/#infoObject)
    openapi.Info(
        title="系统API",
        default_version='v1.0',
        description="系统接口文档",
        terms_of_service="https://ahnu678.com/",
        contact=openapi.Contact(email="liujue212@gmail.com"),
        license=openapi.License(name="liujue"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('backend.urls')),

    #配置Simple JWT
    # 配置django-rest-framwork API路由
    path('api/', include(router.urls)),
    #配置JWT用户登录认证
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    #配置simplejwt认证接口
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #配置drf-yasg路由
    re_path('^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
