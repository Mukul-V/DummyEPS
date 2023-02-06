from django.db import models
from epsapp.models.ClassificationGroup.BaseClassificationGroup import BaseClassificationGroup
from epsapp.models.AppControlPolicy.AppControlPolicy import AppControlPolicy
from epsapp.models.CommonFields import action_type


class AppControlPolicyData(models.Model):
    app_control_policy = models.ForeignKey(AppControlPolicy, on_delete=models.CASCADE)
    key = models.AutoField(primary_key=True)
    app_class_group = models.ForeignKey(BaseClassificationGroup, related_name="app_class_grp", on_delete=models.CASCADE)
    schedule_class_group = models.ForeignKey(BaseClassificationGroup, related_name="schedule_class_grp", on_delete=models.CASCADE)
    action = models.IntegerField(choices=action_type, default=2)

    def __int__(self):
        return self.key

    class Meta:
        verbose_name_plural = "App Control Policy Data"
