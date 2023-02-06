from django.db import models
from epsapp.models.Organization import Organization
from epsapp.models.ClassificationSuperClass import ClassificationSuperClass
from epsapp.models.CommonFields import custom_type


class WebClassification(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    class_base = models.ForeignKey(ClassificationSuperClass, on_delete=models.CASCADE)
    key = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=1000)
    custom = models.IntegerField(choices=custom_type, default=1)

    def __int__(self):
        return self.key

    class Meta:
        verbose_name_plural = "Web FileClassification"
        get_latest_by = "key"
