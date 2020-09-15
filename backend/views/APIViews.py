# from django.shortcuts import render
#
# from rest_framework import viewsets
# from rest_framework import generics
#
# from backend.models import ApiInfo
# from backend.serializers import APIInfo_Serializer
#
#
#
# class APIInfo_ViewSet(viewsets.ModelViewSet):
#     """
#     retrieve:
#     返回一组（查）
#     list:
#     返回所有组(查)
#     create:
#     创建新组(增)
#     delete:
#     删除现有一组(删)
#     partial_update:
#     更新现有组的一个或多个字段
#     update:
#     更新一组
#     """
#     queryset = ApiInfo.objects.all()
#     serializer_class = APIInfo_Serializer