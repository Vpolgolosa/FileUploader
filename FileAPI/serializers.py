from rest_framework import serializers
from rest_framework.serializers import Serializer, FileField, ListField
from .models import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ["file", "uploaded_at", "processed"]
        read_only_fields = ['processed']


