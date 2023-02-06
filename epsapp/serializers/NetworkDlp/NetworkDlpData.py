from rest_framework import serializers
from epsapp.models.NetworkDlp.NetworkDlpData import NetworkDlpData


class NetworkDlpData(serializers.ModelSerializer):
    class Meta:
        model = NetworkDlpData
        fields = ['key', 'network_dlp', 'file_class_group', 'ip_class_group', 'schedule_class_group', 'action']
