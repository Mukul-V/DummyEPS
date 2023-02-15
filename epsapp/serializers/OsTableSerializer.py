from rest_framework import serializers
from epsapp.models.OsTable import OsTable


class OsTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = OsTable
        fields = ['key', 'name', 'value']
