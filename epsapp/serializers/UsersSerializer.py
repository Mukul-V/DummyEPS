from rest_framework import serializers
from epsapp.models.Users import Users


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        models = Users
        fields = ['organization', 'user_auth', 'key', 'name', 'country_code', 'phone', 'email', 'dob', 'user_group',
                  'os', 'mac_address']
