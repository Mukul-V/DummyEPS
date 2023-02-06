from rest_framework import serializers
from epsapp.models.Settings.SettingsNegativePathModel import SettingsNegativePathModel


class SettingsNegativePathModel(serializers.ModelSerializer):
    class Meta:
        model = SettingsNegativePathModel
        fields = ['key', 'organization', 'settings', 'negative_path_model']
