from rest_framework import serializers
from epsapp.models.FeatureTable import FeatureTable


class FeatureTable(serializers.ModelSerializer):
    class Meta:
        model = FeatureTable
        fields = ['key', 'name', 'self_type', 'id_grand_parent', 'id_parent', 'is_hide', 'position',
                  'possible_permission']
