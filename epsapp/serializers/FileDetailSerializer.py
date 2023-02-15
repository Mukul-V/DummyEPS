from rest_framework import serializers
from epsapp.models.FileDetail import FileDetail


class FileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileDetail
        fields = ['key', 'old_name', 'new_name', 'status']
