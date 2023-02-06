from rest_framework import serializers
from epsapp.models.ClassificationGroup.BaseClassificationGroup import BaseClassificationGroup


class BaseClassificationGroup(serializers.ModelSerializer):
    class Meta:
        model = BaseClassificationGroup
        fields = ['organization', 'key', 'name', 'description', 'custom', 'type']
