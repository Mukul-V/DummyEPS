from rest_framework import serializers
from epsapp.models.Role import Role


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['organization', 'key', 'name', 'description', 'custom']
