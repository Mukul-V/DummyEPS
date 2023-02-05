from django.db import models
from epsapp.models.Organization import Organization
from epsapp.models.CommonFields import key_state, tenure_type


class KeysTable(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    key = models.AutoField(primary_key=True)
    key_value = models.CharField(max_length=200)
    issue_date = models.DateField()
    tenure_type = models.IntegerField(choices=tenure_type, default=0)
    activate_date = models.DateField(null=True)
    grace_period = models.IntegerField(default=10)
    tenure_value = models.IntegerField(null=True)
    expiry_date = models.DateField(null=True)
    status = models.IntegerField(choices=key_state, default=0)

    def __str__(self):
        return self.key_value
