from rest_framework import serializers
from epsapp.models.AppFileAccessDlp import AppFileAccessDlp


class AppFileAccessDlpSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppFileAccessDlp
        fields = ['organization', 'key', 'name', 'description', 'custom']
