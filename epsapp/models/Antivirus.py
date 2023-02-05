from django.db import models
from epsapp.models.Organization import Organization


class Antivirus(models.Model):
    key = models.AutoField(primary_key=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    max_file_size_scan = models.IntegerField()
    extension = models.CharField(max_length=255, null=True)

    def __int__(self):
        return self.key

    class Meta:
        verbose_name_plural = "Antivirus"
        get_latest_by = "key"
