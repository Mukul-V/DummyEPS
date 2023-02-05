from django.db import models
from epsapp.models.Organization import Organization


class UserGroup(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    key = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200)
    factor_auth = models.CharField(max_length=10)
    session_in_activity = models.CharField(max_length=200)
    simultaneous_login = models.IntegerField()

    def __int__(self):
        return self.key

    class Meta:
        verbose_name_plural = "Users Group"
        get_latest_by = 'key'
