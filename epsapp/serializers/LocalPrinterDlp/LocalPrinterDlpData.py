from rest_framework import serializers
from epsapp.models.LocalPrinterDlp.LocalPrinterDlpData import LocalPrinterDlpData


class LocalPrinterDlpData(serializers.ModelSerializer):
    class Meta:
        model = LocalPrinterDlpData
        fields = ['local_printer', 'key', 'device_class_group', 'file_class_group', 'schedule_class_group', 'action']
