from rest_framework import serializers
from epsapp.models.UserAuthentication import UserAuthentication


class UserAuthentication(serializers.ModelSerializer):
    class Meta:
        model = UserAuthentication
        fields = ['organization', 'id', 'username', 'password', 'user_type', 'joined_at', 'updated_at', 'jwt_issue_dt',
                  'invalid_attempt', 'holding_datetime', 'is_active', 'is_admin']
