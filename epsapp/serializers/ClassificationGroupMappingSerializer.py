from rest_framework import serializers
from epsapp.models.ClassificationGroupMapping import ClassificationGroupMapping


class ClassificationGroupMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassificationGroupMapping
        fields = ['key', 'class_group', 'class_super', 'types']
