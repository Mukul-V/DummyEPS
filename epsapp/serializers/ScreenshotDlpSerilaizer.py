from rest_framework import serializers
from epsapp.models.ScreenshotDlp import ScreenshotDlp


class ScreenshotDlpSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScreenshotDlp
        fields = ['organization', 'key', 'name', 'description', 'custom']
