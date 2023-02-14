from rest_framework import serializers
from epsapp.models.RuleUserMapping import RuleUserMapping


class RuleUserMapping(serializers.ModelSerializer):
    class Meta:
        model = RuleUserMapping
        fields = ['key', 'rule', 'user', 'user_group']
