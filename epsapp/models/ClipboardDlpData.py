from django.db import models
from epsapp.models.BaseClassificationGroup import BaseClassificationGroup
from epsapp.models.ClipboardDlp import ClipboardDlp


class ClipboardDlpData(models.Model):
    clipboard_dlp = models.ForeignKey(ClipboardDlp, on_delete=models.CASCADE)
    key = models.AutoField(primary_key=True)
    from_app_class_group = models.ForeignKey(BaseClassificationGroup, on_delete=models.CASCADE, related_name="from_app_class_clp")
    to_app_class_group = models.ForeignKey(BaseClassificationGroup, on_delete=models.CASCADE, related_name="to_app_class_clp")
    schedule_class_group = models.ForeignKey(BaseClassificationGroup, on_delete=models.CASCADE, related_name="schedule_class_clp")
    action = models.CharField(default="allow", max_length=10)

    def __int__(self):
        return self.key

    class Meta:
        verbose_name_plural = "Clipboard Dlp Data"
