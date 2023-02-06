from rest_framework import serializers
from epsapp.models.WebClassification.Domain import Domain


class Domain(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = ['key', 'web_classification', 'domain_name']
