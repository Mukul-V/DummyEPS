from rest_framework import serializers
from epsapp.models.LocalPrinterDlpData import LocalPrinterDlpData


class LocalPrinterDlpDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalPrinterDlpData
        fields = ['local_printer', 'key', 'device_class_group', 'file_class_group', 'schedule_class_group', 'action']
