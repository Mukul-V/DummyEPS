from django.db import models
from epsapp.models.CommonFields import action_type, custom_type
from epsapp.models.Organization import Organization


class WebFiltering(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    key = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    default_action = models.IntegerField(choices=action_type, default=2)
    custom = models.IntegerField(choices=custom_type, default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Web Filtering"
        get_latest_by = "key"
