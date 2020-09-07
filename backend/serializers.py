from rest_framework import serializers
from backend.models import ApiInfo


class APIInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ApiInfo
        fields = "__all__"

class APISerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiInfo
        fields = "__all__"


