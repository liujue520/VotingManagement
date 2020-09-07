from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import generics

from backend.models import ApiInfo
from backend.serializers import APISerializer
from backend.serializers import APIInfoSerializer

# Create your views here.

class APIList(generics.ListAPIView):
    """
    查看接口列表
    """
    queryset = ApiInfo.objects.all()
    serializer_class = APISerializer

class APIDetail(generics.RetrieveAPIView):
    """
    查看接口详细
    """
    queryset = ApiInfo.objects.all()
    serializer_class = APISerializer

class APIDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    更新接口内容
    """
    queryset = ApiInfo.objects.all()
    serializer_class = APISerializer

class APIInfoViewSet(viewsets.ModelViewSet):
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
    queryset = ApiInfo.objects.all()
    serializer_class = APIInfoSerializer