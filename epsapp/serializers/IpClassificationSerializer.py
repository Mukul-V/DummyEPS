from rest_framework import serializers
from epsapp.models.IpClassification import IpClassification


class IpClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = IpClassification
        fields = ['organization', 'class_super', 'key', 'name', 'description', 'type', 'startIp', 'endIp', 'subnetMask',
                  'ipList', 'custom']
