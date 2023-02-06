from rest_framework import serializers
from epsapp.models import UserAuthentication


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = UserAuthentication
        fields = ['organization', 'username', 'password', 'password2', 'user_type', 'joined_at']

        extra_kwargs = {
            'password': {'write_only': True},
        }

    # Validated the Password
    def validate(self, attrs):  # field Level validation (password level)
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password Does Not Match")
        return attrs

    def create(self, validated_data):
        return UserAuthentication.objects.create_user(**validated_data)

