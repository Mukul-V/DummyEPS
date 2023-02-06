from rest_framework import serializers
from epsapp.models.Trails.AuthTrails import AuthTrails


class AuthTrails(serializers.ModelSerializer):
    class Meta:
        model = AuthTrails
        fields = ['key', 'type', 'reason', 'user', 'user_login', 'user_logout', 'user_agent', 'token', 'user_ip',
                  'user_os']
