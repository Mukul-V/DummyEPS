from rest_framework import serializers
from epsapp.models.KeysTable import KeysTable


class KeysTable(serializers.ModelSerializer):
    class Meta:
        model = KeysTable
        fields = ['organization', 'key', 'key_value', 'issue_date', 'tenure_type', 'activate_date', 'grace_period',
                  'tenure_value', 'expiry_date', 'status']
