from rest_framework import serializers
from epsapp.models.WebClassification.WebClassification import WebClassification


class WebClassification(serializers.ModelSerializer):
    class Meta:
        model = WebClassification
        fields = ['organization', 'class_base', 'key', 'name', 'description', 'custom']