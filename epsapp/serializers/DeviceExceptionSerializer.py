from rest_framework import serializers
from epsapp.models.DeviceException import DeviceException


class DeviceExceptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceException
        fields = ['device_control_policy', 'types', 'key', 'name', 'description', 'classification', 'action']
