from rest_framework import serializers
from epsapp.models.ScreenshotDlp.ScreenshotDlpData import ScreenshotDlpData


class ScreenshotDlpData(serializers.ModelSerializer):
    class Meta:
        model = ScreenshotDlpData
        fields = ['screenshot_dlp', 'key', 'app_class_group', 'schedule_class_group', 'action']
