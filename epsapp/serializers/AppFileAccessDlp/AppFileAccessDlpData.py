from rest_framework import serializers
from epsapp.models.AppFileAccessDlp.AppFileAccessDlpData import AppFileAccessDlpData


class AppFileAccessDlpData(serializers.ModelSerializer):
    class Meta:
        model = AppFileAccessDlpData
        fields = ['key', 'app_file_access_dlp', 'app_class_group', 'file_class_group', 'schedule_class_group', 'action']
