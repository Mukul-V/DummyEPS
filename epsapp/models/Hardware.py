from django.db import models
from epsapp.models.Organization import Organization
from epsapp.models.KeysTable import KeysTable
from epsapp.models.Users import Users


class Hardware(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    key = models.AutoField(primary_key=True)
    hardware_value = models.CharField(max_length=250)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    key_value = models.ForeignKey(KeysTable, on_delete=models.CASCADE, null=True)
    bandwidth = models.CharField(max_length=100, null=True)
    cpu = models.CharField(max_length=100, null=True)
    ram = models.CharField(max_length=100, null=True)
    hdd = models.CharField(max_length=100, null=True)
    current_wifi = models.CharField(max_length=100, null=True)
    current_ip = models.CharField(max_length=300, null=True)

    def __int__(self):
        return self.key

    class Meta:
        verbose_name_plural = "Hardware Table"
