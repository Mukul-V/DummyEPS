from rest_framework import serializers
from epsapp.models.AppControlPolicy import AppControlPolicy


class AppControlPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = AppControlPolicy
        fields = ['organization', 'key', 'name', 'description', 'custom']

