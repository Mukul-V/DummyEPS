from django.db import models
from epsapp.models.Organization import Organization
from epsapp.models.BaseClassificationGroup import BaseClassificationGroup
from epsapp.models.CommonFields import custom_type, action_type


class DeviceControlPolicy(models.Model):
    key = models.AutoField(primary_key=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=1000)
    schedule_class_group = models.ForeignKey(BaseClassificationGroup, on_delete=models.CASCADE)
    usb_storage_device = models.IntegerField(choices=action_type, default=1)
    cd_dvd = models.IntegerField(choices=action_type, default=1)
    portable = models.IntegerField(choices=action_type, default=1)
    wifi = models.IntegerField(choices=action_type, default=1)
    bluetooth = models.IntegerField(choices=action_type, default=1)
    webcam = models.IntegerField(choices=action_type, default=1)
    serial_port = models.IntegerField(choices=action_type, default=1)
    usb_port = models.IntegerField(choices=action_type, default=1)
    local_printer = models.IntegerField(choices=action_type, default=1)
    network_share = models.IntegerField(choices=action_type, default=1)
    card_reader = models.IntegerField(choices=action_type, default=1)
    unknown_device = models.IntegerField(choices=action_type, default=1)
    custom = models.IntegerField(choices=custom_type, default=1)

    def __int__(self):
        return self.key

    class Meta:
        verbose_name_plural = "DeviceControlPolicy"
