from rest_framework import serializers
from epsapp.models.AppFileAccessDlp.AppFileAccessDlp import AppFileAccessDlp


class AppFileAccessDlp(serializers.ModelSerializer):
    class Meta:
        model = AppFileAccessDlp
        fields = ['organization', 'key', 'name', 'description', 'custom']
