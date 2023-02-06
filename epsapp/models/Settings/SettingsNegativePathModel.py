from django.db import models
from epsapp.models.Organization import Organization
from epsapp.models.Settings.Settings import Settings


class SettingsNegativePathModel(models.Model):
    key = models.AutoField(primary_key=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    settings = models.ForeignKey(Settings, on_delete=models.CASCADE, null=True)
    negative_path_model = models.CharField(max_length=200, null=True)

    def __int__(self):
        return self.key

    class Meta:
        verbose_name_plural = "Settings Negative Path Model"
