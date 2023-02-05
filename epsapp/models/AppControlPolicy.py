from django.db import models
from epsapp.models.Organization import Organization


class AppControlPolicy(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    key = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "App Control Policy"
        get_latest_by = 'key'
