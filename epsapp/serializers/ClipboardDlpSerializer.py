from rest_framework import serializers
from epsapp.models.ClipboardDlp import ClipboardDlp


class ClipboardDlpSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClipboardDlp
        fields = ['organization', 'key', 'name', 'description', 'custom']
