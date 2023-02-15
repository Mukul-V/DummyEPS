from rest_framework import serializers
from epsapp.models.NetworkDlp import NetworkDlp


class NetworkDlpSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkDlp
        fields = ['organization', 'key', 'name', 'description', 'custom']
