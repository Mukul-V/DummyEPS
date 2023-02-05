from django.db import models
from epsapp.models.Organization import Organization


class Role(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    key = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=300)

    def __int__(self):
        return self.key

    class Meta:
        verbose_name_plural = "Organization"
        get_latest_by = "key"
