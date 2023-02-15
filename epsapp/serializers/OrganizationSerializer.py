from rest_framework import serializers
from epsapp.models.Organization import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['key', 'name', 'email', 'phone', 'address', 'dob', 'created_at', 'updated_at']
