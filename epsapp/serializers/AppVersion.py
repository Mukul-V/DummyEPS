from rest_framework import serializers
from epsapp.models.AppVersion import AppVersion


class AppVersion(serializers.ModelSerializer):
    model = AppVersion
    fields = ['key', 'version', 'version_allowed', 'created_dt', 'url', 'custom']
