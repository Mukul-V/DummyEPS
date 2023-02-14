from rest_framework import serializers
from epsapp.models.WebDlpData import WebDlpData


class WebDlpData(serializers.ModelSerializer):
    class Meta:
        model = WebDlpData
        fields = ['key', 'web_dlp', 'file_class_group', 'web_class_group', 'schedule_class_group', 'action']
