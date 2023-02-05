from django.db import models
from epsapp.models.AppClassification import AppClassification


class AppClassData(models.Model):
    key = models.AutoField(primary_key=True)
    app_classification = models.ForeignKey(AppClassification, on_delete=models.CASCADE)
    column = models.CharField(max_length=20, null=True)
    value = models.CharField(max_length=100, null=True)

    def __int__(self):
        return self.key

    class Meta:
        verbose_name_plural = "App Classification Data"
