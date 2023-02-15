from rest_framework import serializers
from epsapp.models.UserHistory import UserHistory


class UserHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserHistory
        fields = ['organization', 'key', 'user_id', 'hardware_id', 'login', 'logout']
