from rest_framework import serializers
from epsapp.models.LocalPrinterDlp import LocalPrinterDlp


class LocalPrinterDlpSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalPrinterDlp
        fields = ['organization', 'key', 'name', 'description', 'custom']
