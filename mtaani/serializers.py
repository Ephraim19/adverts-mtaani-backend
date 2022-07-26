from rest_framework import serializers
from .models import FileId

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileId
        fields = '__all__'