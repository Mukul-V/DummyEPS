from django.db import models
from epsapp.models.ClassificationGroup.BaseClassificationGroup import BaseClassificationGroup
from epsapp.models.NetworkDlp.NetworkDlp import NetworkDlp
from epsapp.models.CommonFields import action_type


class NetworkDlpData(models.Model):
    key = models.AutoField(primary_key=True)
    network_dlp = models.ForeignKey(NetworkDlp, on_delete=models.CASCADE)
    file_class_group = models.ForeignKey(BaseClassificationGroup, on_delete=models.CASCADE,
                                         related_name="file_class_group_nwk")
    ip_class_group = models.ForeignKey(BaseClassificationGroup, on_delete=models.CASCADE,
                                       related_name="ip_class_group_nwk")
    schedule_class_group = models.ForeignKey(BaseClassificationGroup, on_delete=models.CASCADE,
                                             related_name="schedule_class_group_nwk")
    action = models.IntegerField(choices=action_type, default=2)

    def __int__(self):
        return self.key

    class Meta:
        verbose_name_plural = "Network Dlp Data"
