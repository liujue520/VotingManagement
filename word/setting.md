#django setting详解

## 1.mysql数据库配置
```
1.pip install pymysql
2.在mysql中新建数据库
3.数据库配置、django如下，mysql中新建
4.数据库迁徙
$python manage.py makemigrations
$python manage.py migrate


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',    #你的数据库名称
        'USER': 'root',   #你的数据库用户名
        'PASSWORD': '19941028', #你的数据库密码
        'HOST': '', #你的数据库主机，留空默认为localhost
        'PORT': '3306', #你的数据库端口
    }
}
```

## 2.设置时区
```
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'
```
## 3.创建应用、在setting中加载应用
```
1.$python manage.py startapp app名称

2.在setting.py中的INSTALLED_APPS中添加设置

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blogApp.apps.BlogappConfig' #这里，具体apps.后是什么看对应app下的apps.py
]

3.运行命令，检测模型文件的修改
$python manage.py makemigrations blogApp
执行迁移命令 $python manage.py migrate
```
## 4.使用Django REST framework
````
安装并配置restframework—>serializer配置—>编写views.py—>URL配置
1.安装：pip install djangorestframework
2.配置settings.py的INSTALLED_APPS中添加:
INSTALLED_APPS = [
    ...
    'rest_framework',
]
3.blogApp下创建serializers.py，编写代码

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Blog

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('header', 'content', 'cover', 'markdownContent', 'time', 'readTimes')
4.在settings中配置权限
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}
````
