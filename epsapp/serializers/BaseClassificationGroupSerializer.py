from rest_framework import serializers
from epsapp.models.BaseClassificationGroup import BaseClassificationGroup


class BaseClassificationGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseClassificationGroup
        fields = ['organization', 'key', 'name', 'description', 'custom', 'type']
