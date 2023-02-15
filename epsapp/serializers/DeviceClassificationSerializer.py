from rest_framework import serializers
from epsapp.models.DeviceClassification import DeviceClassification


class DeviceClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceClassification
        fields = ['organization', 'class_super', 'key', 'name', 'description', 'device_type', 'device_name_regex',
                  'vid', 'pid', 'serial_number', 'brand', 'custom']
