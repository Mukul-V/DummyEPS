from rest_framework.serializers import ModelSerializer
from epsapp.models.Antivirus import Antivirus


class Antivirus(ModelSerializer):
    class Meta:
        model = Antivirus
        # fields = ['key ', 'organization', 'max_file_size_scan', 'extension', 'custom']
        fields = '__all__'
