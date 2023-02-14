from rest_framework import serializers
from epsapp.models.UserAuthentication import UserAuthentication


class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100, required=False)
    password = serializers.CharField(required=False)

    class Meta:
        model = UserAuthentication
        fields = ['username', 'password']
