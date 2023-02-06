from rest_framework import serializers
from epsapp.models.LocalPrinterDlp.LocalPrinterDlp import LocalPrinterDlp


class LocalPrinterDlp(serializers.ModelSerializer):
    class Meta:
        model = LocalPrinterDlp
        fields = ['organization', 'key', 'name', 'description', 'custom']
