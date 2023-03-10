from rest_framework import serializers
from epsapp.models.NetworkDlpData import NetworkDlpData


class NetworkDlpDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkDlpData
        fields = ['key', 'network_dlp', 'file_class_group', 'ip_class_group', 'schedule_class_group', 'action']
