from rest_framework import serializers
from epsapp.models.AppClassification import AppClassification


class AppClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppClassification
        fields = ['organization', 'class_super', 'key', 'name', 'description', 'custom']
