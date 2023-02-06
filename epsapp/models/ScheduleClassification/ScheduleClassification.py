from django.db import models
from epsapp.models.Organization import Organization
from epsapp.models.ClassificationSuperClass import ClassificationSuperClass
from epsapp.models.CommonFields import custom_type, schedule_duration


class ScheduleClassification(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, default=None, null=True)
    class_super = models.ForeignKey(ClassificationSuperClass, on_delete=models.DO_NOTHING, null=True)
    key = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    start_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    end_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    duration = models.IntegerField(choices=schedule_duration, default=1)
    custom = models.IntegerField(choices=custom_type, default=1)
    # days = models.CharField(max_length=500, null=True)
    # time_slot = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Schedule FileClassification"
        get_latest_by = "key"
