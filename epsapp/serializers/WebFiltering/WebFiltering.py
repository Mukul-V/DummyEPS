from rest_framework import serializers
from epsapp.models.WebFiltering.WebFiltering import WebFiltering


class WebFiltering(serializers.ModelSerializer):
    class Meta:
        model = WebFiltering
        fields = ['organization', 'key', 'name', 'description', 'default_action', 'custom']
