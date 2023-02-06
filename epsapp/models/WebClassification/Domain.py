from django.db import models
from epsapp.models.WebClassification.WebClassification import WebClassification


class Domain(models.Model):
    key = models.AutoField(primary_key=True)
    web_classification = models.ForeignKey(WebClassification, on_delete=models.CASCADE)
    domain_name = models.CharField(max_length=200)

    def __int__(self):
        return self.key

    class Meta:
        verbose_name_plural = "Domain"
