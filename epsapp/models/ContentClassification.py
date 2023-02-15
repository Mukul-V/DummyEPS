from django.db import models
from epsapp.models.CommonFields import custom_type
from epsapp.models.Organization import Organization


class ContentClassification(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True)
    key = models.AutoField(primary_key=True)
    relation_of_data = models.CharField(max_length=5, null=True)
    keyword_regex = models.CharField(max_length=150)
    validation_type = models.CharField(max_length=15)
    old_name = models.CharField(max_length=150, null=True)
    validation_value = models.CharField(max_length=150, null=True)
    no_of_matches = models.IntegerField()
    custom = models.IntegerField(choices=custom_type, default=1)

    def __int__(self):
        return self.key

    class Meta:
        verbose_name_plural = "File Data"
        get_latest_by = 'key'
