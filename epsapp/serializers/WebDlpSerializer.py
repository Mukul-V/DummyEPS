from rest_framework import serializers
from epsapp.models.WebDlp import WebDlp


class WebDlpSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebDlp
        fields = ['organization', 'key', 'name', 'description', 'custom']
