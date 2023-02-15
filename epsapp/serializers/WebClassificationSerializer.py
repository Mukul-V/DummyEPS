from rest_framework import serializers
from epsapp.models.WebClassification import WebClassification


class WebClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebClassification
        fields = ['organization', 'class_base', 'key', 'name', 'description', 'custom']