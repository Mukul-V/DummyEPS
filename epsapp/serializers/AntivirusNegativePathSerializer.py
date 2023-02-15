from rest_framework import serializers
from epsapp.models.AntivirusNegativePath import AntivirusNegativePathModel


class AntivirusNegativePathSerializer(serializers.ModelSerializer):
    class Meta:
        model = AntivirusNegativePathModel
        fields = ['key', 'antivirus', 'negative_path_model']
