from django.db import models
from epsapp.models.BaseClassificationGroup import BaseClassificationGroup
from epsapp.models.ScreenshotDlp import ScreenshotDlp
from epsapp.models.CommonFields import action_type


class ScreenshotDlpData(models.Model):
    screenshot_dlp = models.ForeignKey(ScreenshotDlp, on_delete=models.CASCADE)
    key = models.AutoField(primary_key=True)
    app_class_group = models.ForeignKey(BaseClassificationGroup, on_delete=models.CASCADE,
                                        related_name="app_class_group_scr")
    schedule_class_group = models.ForeignKey(BaseClassificationGroup, on_delete=models.CASCADE,
                                             related_name="schedule_class_group_scr")
    action = models.IntegerField(choices=action_type, default=2)

    def __int__(self):
        return self.key

    class Meta:
        verbose_name_plural = "Screenshot Dlp Data"
