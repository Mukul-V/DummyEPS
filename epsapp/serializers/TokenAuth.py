from rest_framework import serializers
from epsapp.models.TokenAuth import TokenAuth


class TokenAuth(serializers.ModelSerializer):
    class Meta:
        model = TokenAuth
        fields = ['organization', 'key', 'access_token', 'refresh_token', 'admin_key', 'role', 'created_at', 'updated_at',
                  'status']
