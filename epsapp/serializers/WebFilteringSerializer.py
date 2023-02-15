from rest_framework import serializers
from epsapp.models.WebFiltering import WebFiltering


class WebFilteringSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebFiltering
        fields = ['organization', 'key', 'name', 'description', 'default_action', 'custom']
