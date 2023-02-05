from django.db import models


class AppVersion(models.Model):
    key = models.AutoField(primary_key=True)
    version = models.CharField(max_length=50, null=True, unique=True)
    version_allowed = models.BooleanField(default=True)
    created_dt = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=100, null=True)

    def __int__(self):
        return self.key

    class Meta:
        verbose_name_plural = "App Version"
        get_latest_by = "key"
