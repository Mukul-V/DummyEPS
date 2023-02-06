from rest_framework import serializers
from epsapp.models.DeviceControlPolicy.DeviceException import DeviceException


class DeviceException(serializers.ModelSerializer):
    class Meta:
        model = DeviceException
        fields = ['device_control_policy', 'types', 'key', 'name', 'description', 'classification', 'action']
