from rest_framework import serializers
from epsapp.models.WebDlp.WebDlp import WebDlp


class WebDlp(serializers.ModelSerializer):
    class Meta:
        model = WebDlp
        fields = ['organization', 'key', 'name', 'description', 'custom']
