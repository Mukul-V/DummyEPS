from rest_framework import serializers
from epsapp.models.AuditTrails import AuditTrails


class AuditTrailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditTrails
        fields = ['key', 'auth_trail', 'type', 'date_time', 'action']
