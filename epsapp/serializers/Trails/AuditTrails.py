from rest_framework import serializers
from epsapp.models.Trails.AuditTrails import AuditTrails


class AuditTrails(serializers.ModelSerializer):
    class Meta:
        model = AuditTrails
        fields = ['key', 'auth_trail', 'type', 'date_time', 'action']
