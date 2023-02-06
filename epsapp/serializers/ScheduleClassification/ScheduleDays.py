from rest_framework import serializers
from epsapp.models.ScheduleClassification.ScheduleDays import ScheduleDays


class ScheduleDays(serializers.ModelSerializer):
    class Meta:
        model = ScheduleDays
        fields = ['schedule_class', 'key', 'days', 'time']
