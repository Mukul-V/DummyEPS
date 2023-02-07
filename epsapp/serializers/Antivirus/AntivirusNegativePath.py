from rest_framework import serializers
from epsapp.models.Antivirus.AntivirusNegativePath import AntivirusNegativePathModel


class AntivirusNegativePathMode(serializers.ModelSerializer):
    class Meta:
        model = AntivirusNegativePathModel
        fields = ['key', 'antivirus', 'negative_path_model']