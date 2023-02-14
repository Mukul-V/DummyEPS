from django.db import models
from epsapp.models import Organization
from epsapp.models.UserAuthentication import UserAuthentication
from epsapp.models.Hardware import Hardware


class UserHistory(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    key = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(UserAuthentication, on_delete=models.CASCADE)
    hardware_id = models.ForeignKey(Hardware, default=None, on_delete=models.CASCADE)
    login = models.DateTimeField(null=True)
    logout = models.DateTimeField(null=True)

    def __int__(self):
        return self.user_id

    class Meta:
        verbose_name_plural = "User History"

