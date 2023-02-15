from rest_framework import serializers
from epsapp.models.ScheduleDays import ScheduleDays


class ScheduleDaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleDays
        fields = ['schedule_class', 'key', 'days', 'time']
