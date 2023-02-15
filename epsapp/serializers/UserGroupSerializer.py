from rest_framework import serializers
from epsapp.models.UserGroup import UserGroup


class UserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroup
        fields = ['organization', 'key', 'name', 'description', 'factor_auth', 'session_in_activity',
                  'simultaneous_login']
