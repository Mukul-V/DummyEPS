from django.db import models
from epsapp.models.Organization import Organization


class ClipboardDlp(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    key = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=1000)

    def __int__(self):
        return self.key

    class Meta:
        verbose_name_plural = "Clipboard Dlp"
        get_latest_by = 'key'
