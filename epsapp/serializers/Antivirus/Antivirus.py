from rest_framework import serializers
from epsapp.models.Antivirus import Antivirus


class Antivirus(serializers.ModelSerializer):
    class Meta:
        model = Antivirus
        fields = ['key ', 'organization', 'max_file_size_scan', 'extension', 'custom']
