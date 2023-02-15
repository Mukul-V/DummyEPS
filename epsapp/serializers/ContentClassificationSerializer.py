from rest_framework import serializers
from epsapp.models.ContentClassification import ContentClassification


class ContentClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentClassification
        fields = ['key', 'relation_of_data', 'keyword_regex', 'validation_type', 'old_name', 'validation_value',
                  'no_of_matches', 'custom']
