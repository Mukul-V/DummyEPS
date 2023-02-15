from rest_framework import serializers
from epsapp.models.Domain import Domain


class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = ['key', 'web_classification', 'domain_name']
