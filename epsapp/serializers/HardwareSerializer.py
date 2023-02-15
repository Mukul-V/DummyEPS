from rest_framework import serializers
from epsapp.models.Hardware import Hardware


class HardwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hardware
        fields = ['organization', 'key', 'hardware_value', 'user', 'key_value', 'bandwidth', 'cpu', 'ram', 'hdd',
                  'current_wifi', 'current_ip']
