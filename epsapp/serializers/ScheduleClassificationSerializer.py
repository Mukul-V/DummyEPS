from rest_framework import serializers
from epsapp.models.ScheduleClassification import ScheduleClassification


class ScheduleClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleClassification
        fields = ['organization', 'class_super', 'key', 'name', 'description', 'start_date', 'end_date', 'duration', 'custom']