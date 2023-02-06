from django.db import models
from epsapp.models.Organization import Organization
from epsapp.models.CommonFields import action_type, channel_type


class Reporting(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    key = models.AutoField(primary_key=True)
    incident_time = models.DateTimeField()
    source = models.CharField(max_length=100)
    endpoint = models.CharField(max_length=200, null=True)
    policy = models.CharField(max_length=100)
    channel = models.IntegerField(choices=channel_type, default=1)
    destination = models.CharField(max_length=100)
    transaction_size = models.CharField(max_length=50)
    action = models.IntegerField(choices=action_type, default=2)
    maximum_matches = models.IntegerField()
    status = models.CharField(max_length=50, default="new")
    severity = models.CharField(max_length=50, default="low")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    detected_by = models.CharField(max_length=50)
    files = models.CharField(max_length=100, null=True)
    application_name = models.CharField(max_length=100)
    direction = models.CharField(max_length=100, default="inbound")

    def __int__(self):
        return self.key

    class Meta:
        verbose_name_plural = "Reporting"
