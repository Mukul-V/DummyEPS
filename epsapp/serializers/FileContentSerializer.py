from rest_framework import serializers
from epsapp.models.FileContent import FileContent


class FileContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileContent
        fields = ['key', 'file_data', 'file_row']
