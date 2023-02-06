from django.db import models
from epsapp.models.Organization import Organization
from epsapp.models.ClassificationSuperClass import ClassificationSuperClass
from epsapp.models.CommonFields import custom_type, device_type


class DeviceClassification(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    class_super = models.ForeignKey(ClassificationSuperClass, on_delete=models.CASCADE)
    key = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=1000, default=None)
    device_type = models.IntegerField(choices=device_type, default=1)
    device_name_regex = models.CharField(max_length=100, null=True)
    vid = models.CharField(max_length=50, default=None, null=True)
    pid = models.CharField(max_length=50, default=None, null=True)
    serial_number = models.CharField(max_length=100)
    brand = models.CharField(max_length=25, default=None)
    custom = models.IntegerField(choices=custom_type, default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Device FileClassification"
