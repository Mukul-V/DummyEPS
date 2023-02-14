from django.db import models
from epsapp.models.ScheduleClassification import ScheduleClassification


class ScheduleDays(models.Model):
    schedule_class = models.ForeignKey(ScheduleClassification, on_delete=models.CASCADE)
    key = models.AutoField(primary_key=True)
    days = models.CharField(max_length=50)
    time = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Schedule Days"
        get_latest_by = "key"
