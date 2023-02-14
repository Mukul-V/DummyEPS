from django.db import models
from epsapp.models.WebFiltering import WebFiltering
from epsapp.models.WebClassification import WebClassification
from epsapp.models.CommonFields import action_type
from epsapp.models.BaseClassificationGroup import BaseClassificationGroup


class WebFilteringMapping(models.Model):
    key = models.AutoField(primary_key=True)
    web_filter = models.ForeignKey(WebFiltering, on_delete=models.CASCADE)
    web_class = models.ForeignKey(WebClassification, on_delete=models.CASCADE)
    schedule_class_group = models.ForeignKey(BaseClassificationGroup, on_delete=models.CASCADE, null=True)
    action = models.IntegerField(choices=action_type, default=2)

    def __int__(self):
        return self.key

    class Meta:
        verbose_name_plural = "Web Filtering Mapping"
