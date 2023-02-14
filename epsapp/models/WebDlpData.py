from django.db import models
from epsapp.models.BaseClassificationGroup import BaseClassificationGroup
from epsapp.models.WebDlp import WebDlp
from epsapp.models.CommonFields import action_type


class WebDlpData(models.Model):
    key = models.AutoField(primary_key=True)
    web_dlp = models.ForeignKey(WebDlp, on_delete=models.CASCADE)
    file_class_group = models.ForeignKey(BaseClassificationGroup, on_delete=models.CASCADE,
                                         related_name="file_class_group_web")
    web_class_group = models.ForeignKey(BaseClassificationGroup, on_delete=models.CASCADE,
                                        related_name="web_class_group_web")
    schedule_class_group = models.ForeignKey(BaseClassificationGroup, on_delete=models.CASCADE,
                                             related_name="schedule_class_group_web")
    action = models.IntegerField(choices=action_type, default=2)

    def __int__(self):
        return self.key

    class Meta:
        verbose_name_plural = "Web Dlp Data"
