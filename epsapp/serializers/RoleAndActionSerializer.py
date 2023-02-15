from rest_framework import serializers
from epsapp.models.RoleAndAction import RoleAndAction


class RoleAndActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleAndAction
        fields = ['key', 'role', 'feature_id', 'permission']
