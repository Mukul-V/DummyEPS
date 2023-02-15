from rest_framework import serializers
from epsapp.models.RuleUserMapping import RuleUserMapping


class RuleUserMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RuleUserMapping
        fields = ['key', 'rule', 'user', 'user_group']
