from rest_framework import serializers
from epsapp.models.RoleAndAction import RoleAndAction


class RoleAndAction(serializers.ModelSerializer):
    class Meta:
        model = RoleAndAction
        fields = ['key', 'role', 'feature_id', 'permission']
