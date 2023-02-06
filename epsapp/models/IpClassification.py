from django.db import models
from epsapp.models.Organization import Organization
from epsapp.models.ClassificationSuperClass import ClassificationSuperClass
from epsapp.models.CommonFields import ip_type, custom_type


class IpClassification(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    class_super = models.ForeignKey(ClassificationSuperClass, on_delete=models.CASCADE)
    key = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    type = models.IntegerField(choices=ip_type, default=1)
    startIp = models.GenericIPAddressField(null=True, default="0.0.0.0")
    endIp = models.GenericIPAddressField(null=True, default="0.0.0.0")
    subnetMask = models.IntegerField(null=True, default=0)
    ipList = models.CharField(max_length=1000, null=True, default="0.0.0.0")
    custom = models.IntegerField(choices=custom_type, default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Ip FileClassification"
