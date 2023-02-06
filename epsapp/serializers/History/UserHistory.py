from rest_framework import serializers
from epsapp.models.History.UserHistory import UserHistory


class UserHistory(serializers.ModelSerializer):
    class Meta:
        model = UserHistory
        fields = ['organization', 'key', 'user_id', 'hardware_id', 'login', 'logout']
