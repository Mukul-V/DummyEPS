from django.db import models
from epsapp.models.Organization import Organization


class Settings(models.Model):
    key = models.AutoField(primary_key=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    config_fetch_timeout = models.IntegerField()
    super_user_password = models.CharField(max_length=255)

    def __int__(self):
        return self.key

    class Meta:
        verbose_name_plural = "Settings"
        get_latest_by = "key"

