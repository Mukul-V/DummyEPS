from rest_framework import serializers
from epsapp.models.ClipboardDlp.ClipboardDlp import ClipboardDlp


class ClipboardDlp(serializers.ModelSerializer):
    class Meta:
        model = ClipboardDlp
        fields = ['organization', 'key', 'name', 'description', 'custom']
