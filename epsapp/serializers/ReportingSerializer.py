from rest_framework import serializers
from epsapp.models.Reporting import Reporting


class ReportingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporting
        fields = ['organization', 'key', 'incident_time', 'source', 'endpoint', 'policy', 'channel', 'destination',
                  'transaction_size', 'action', 'maximum_matches', 'status', 'severity', 'created_at', 'updated_at',
                  'detected_by', 'files', 'application_name', 'direction']
