from rest_framework import serializers
from epsapp.models.ScreenshotDlp.ScreenshotDlp import ScreenshotDlp


class ScreenshotDlp(serializers.ModelSerializer):
    class Meta:
        model = ScreenshotDlp
        fields = ['organization', 'key', 'name', 'description', 'custom']
