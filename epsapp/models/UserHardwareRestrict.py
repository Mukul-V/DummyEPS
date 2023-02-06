from django.db import models
from epsapp.models.Hardware import Hardware
from epsapp.models.Users import Users


class UserHardwareRestrict(models.Model):
    key = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    hardware_value = models.ForeignKey(Hardware, on_delete=models.CASCADE, verbose_name="hardware_value")

    def __int__(self):
        return self.key

    class Meta:
        verbose_name_plural = "User Hardware Restrict"
