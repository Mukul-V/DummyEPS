from rest_framework import serializers
from epsapp.models.DeviceControlPolicy import DeviceControlPolicy


class DeviceControlPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceControlPolicy
        fields = ['key', 'organization', 'name', 'description', 'schedule_class_group', 'usb_storage_device', 'cd_dvd',
                  'portable', 'wifi', 'bluetooth', 'webcam', 'serial_port', 'usb_port', 'local_printer',
                  'network_share', 'card_reader', 'unknown_device', 'custom']
