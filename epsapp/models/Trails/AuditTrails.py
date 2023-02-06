from django.db import models
from epsapp.models.Trails.AuthTrails import AuthTrails


class AuditTrails(models.Model):
    key = models.AutoField(primary_key=True)
    auth_trail = models.ForeignKey(AuthTrails, on_delete=models.CASCADE)
    type = models.CharField(max_length=255, null=True)
    date_time = models.DateTimeField()
    action = models.CharField(max_length=255, null=True)

    def __int__(self):
        return self.key

    class Meta:
        verbose_name_plural = "Audit Trails"
