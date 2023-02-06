from rest_framework import serializers
from epsapp.models.Settings.Settings import Settings


class Settings(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = ['key', 'organization', 'config_fetch_timeout', 'super_user_password']
