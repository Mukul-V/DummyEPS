from rest_framework import serializers
from epsapp.models.Rules.Rules import Rules


class Rules(serializers.ModelSerializer):
    class Meta:
        model = Rules
        fields = ['organization', 'key', 'name', 'description', 'device_control_policy', 'app_control_policy',
                  'app_file_access_dlp', 'clipboard_dlp', 'local_printer_dlp', 'network_dlp', 'screenshot_dlp',
                  'web_dlp', 'web_filter', 'position', 'custom']
