from rest_framework import serializers
from epsapp.models.ClipboardDlpData import ClipboardDlpData


class ClipboardDlpDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClipboardDlpData
        fields = ['clipboard_dlp', 'key', 'from_app_class_group', 'to_app_class_group', 'schedule_class_group',
                  'action']
