from rest_framework import serializers
from epsapp.models.SettingsNegativePathModel import SettingsNegativePathModel


class SettingsNegativePathModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SettingsNegativePathModel
        fields = ['key', 'organization', 'settings', 'negative_path_model']
