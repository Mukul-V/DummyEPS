from rest_framework import serializers
from epsapp.models.WebFilteringMapping import WebFilteringMapping


class WebFilteringMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebFilteringMapping
        fields = ['key', 'web_filter', 'web_class', 'schedule_class_group', 'action']
