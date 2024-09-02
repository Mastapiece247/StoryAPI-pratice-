from rest_framework import serializers
from .models import Novel


class NovelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Novel
