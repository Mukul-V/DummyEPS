from django.db import models
from nividapp.src.models.Organization import Organization
from nividapp.src.models.Classification_SuperClass import ClassificationSuperClass


class AppClassification(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    class_super = models.ForeignKey(ClassificationSuperClass, on_delete=models.CASCADE)
    key = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    custom = models.IntegerField(default=1)

    def __int__(self):
        return self.key

    class Meta:
        verbose_name_plural = "App Classification"
        get_latest_by = "key"
