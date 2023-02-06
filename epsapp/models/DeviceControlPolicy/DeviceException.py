from django.db import models
from epsapp.models.ClassificationSuperClass import ClassificationSuperClass
from epsapp.models.DeviceControlPolicy.DeviceControlPolicy import DeviceControlPolicy
from epsapp.models.CommonFields import action_type


class DeviceException(models.Model):
    device_control_policy = models.ForeignKey(DeviceControlPolicy, on_delete=models.CASCADE)
    types = models.IntegerField()
    key = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=1000)
    classification = models.ForeignKey(ClassificationSuperClass, on_delete=models.CASCADE)
    action = models.IntegerField(choices=action_type, default=2)

    def __int__(self):
        return self.key

    class Meta:
        verbose_name_plural = "Device Exception"
        get_latest_by = "key"

