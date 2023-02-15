from rest_framework import serializers
from epsapp.models.FileClassification import FileClassification


class FileClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileClassification
        fields = ['organization', 'class_super', 'key', 'name', 'description', 'file_type', 'file_title', 'file_desc',
                  'file_ext', 'subject', 'tags', 'author', 'program', 'company', 'content_created', 'date_last_saved',
                  'size', 'date_created', 'date_modified', 'owner', 'folder_path', 'custom']
