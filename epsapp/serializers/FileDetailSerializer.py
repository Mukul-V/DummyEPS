from rest_framework import serializers
from epsapp.models.FileDetail import FileDetail


class FileDetail(serializers.ModelSerializer):
    class Meta:
        model = FileDetail
        fields = ['key', 'old_name', 'new_name', 'status']