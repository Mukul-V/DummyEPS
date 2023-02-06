from django.db import models
from epsapp.models.LocalPrinterDlp.LocalPrinterDlp import LocalPrinterDlp
from epsapp.models.ClassificationGroup.BaseClassificationGroup import BaseClassificationGroup
from epsapp.models.CommonFields import action_type


class LocalPrinterDlpData(models.Model):
    local_printer = models.ForeignKey(LocalPrinterDlp, on_delete=models.CASCADE)
    key = models.AutoField(primary_key=True)
    device_class_group = models.ForeignKey(BaseClassificationGroup, on_delete=models.CASCADE,
                                           related_name="device_class_group_print")
    file_class_group = models.ForeignKey(BaseClassificationGroup, on_delete=models.CASCADE,
                                         related_name="file_class_group_print")
    schedule_class_group = models.ForeignKey(BaseClassificationGroup, on_delete=models.CASCADE,
                                             related_name="schedule_class_group_print")
    action = models.IntegerField(choices=action_type, default=2)

    def __int__(self):
        return self.key

    class Meta:
        verbose_name_plural = "Local Printer Dlp Data"
