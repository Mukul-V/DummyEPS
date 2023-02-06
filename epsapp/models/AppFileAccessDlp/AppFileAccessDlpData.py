from django.db import models
from epsapp.models.ClassificationGroup.BaseClassificationGroup import BaseClassificationGroup
from epsapp.models.AppFileAccessDlp.AppFileAccessDlp import AppFileAccessDlp
from epsapp.models.CommonFields import action_type


class AppFileAccessDlpData(models.Model):
    key = models.AutoField(primary_key=True)
    app_file_access_dlp = models.ForeignKey(AppFileAccessDlp, on_delete=models.CASCADE)
    app_class_group = models.ForeignKey(BaseClassificationGroup, on_delete=models.CASCADE, related_name="app_class_group_afa")
    file_class_group = models.ForeignKey(BaseClassificationGroup, on_delete=models.CASCADE, related_name="file_class_group_afa")
    schedule_class_group = models.ForeignKey(BaseClassificationGroup, on_delete=models.CASCADE, related_name="schedule_class_group_afa")
    action = models.IntegerField(choices=action_type, default=2)

    def __int__(self):
        return self.key

    class Meta:
        verbose_name_plural = "App File Access Dlp Data"
