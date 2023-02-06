from rest_framework import serializers
from epsapp.models.UserHardwareRestrict import UserHardwareRestrict


class UserHardware(serializers.ModelSerializer):
    class Meta:
        model = UserHardwareRestrict
        fields = ['key', 'user', 'hardware_value']
