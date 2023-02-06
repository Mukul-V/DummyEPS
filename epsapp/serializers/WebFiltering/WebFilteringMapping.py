from rest_framework import serializers
from epsapp.models.WebFiltering.WebFilteringMapping import WebFilteringMapping


class WebFilteringMapping(serializers.ModelSerializer):
    class Meta:
        model = WebFilteringMapping
        fields = ['key', 'web_filter', 'web_class', 'schedule_class_group', 'action']
