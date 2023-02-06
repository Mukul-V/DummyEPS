from django.db import models
from epsapp.models.Organization import Organization
from epsapp.models.DeviceControlPolicy.DeviceControlPolicy import DeviceControlPolicy
from epsapp.models.AppControlPolicy.AppControlPolicy import AppControlPolicy
from epsapp.models.AppFileAccessDlp.AppFileAccessDlp import AppFileAccessDlp
from epsapp.models.ClipboardDlp.ClipboardDlp import ClipboardDlp
from epsapp.models.LocalPrinterDlp.LocalPrinterDlp import LocalPrinterDlp
from epsapp.models.NetworkDlp.NetworkDlp import NetworkDlp
from epsapp.models.ScreenshotDlp.ScreenshotDlp import ScreenshotDlp
from epsapp.models.WebDlp.WebDlp import WebDlp
from epsapp.models.WebFiltering.WebFiltering import WebFiltering
from epsapp.models.CommonFields import custom_type


class Rules(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    key = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    device_control_policy = models.ForeignKey(DeviceControlPolicy, on_delete=models.CASCADE, null=True)
    app_control_policy = models.ForeignKey(AppControlPolicy, on_delete=models.CASCADE, null=True)
    app_file_access_dlp = models.ForeignKey(AppFileAccessDlp, on_delete=models.CASCADE, null=True)
    clipboard_dlp = models.ForeignKey(ClipboardDlp, on_delete=models.CASCADE, null=True)
    local_printer_dlp = models.ForeignKey(LocalPrinterDlp, on_delete=models.CASCADE, null=True)
    network_dlp = models.ForeignKey(NetworkDlp, on_delete=models.CASCADE, null=True)
    screenshot_dlp = models.ForeignKey(ScreenshotDlp, on_delete=models.CASCADE, null=True)
    web_dlp = models.ForeignKey(WebDlp, on_delete=models.CASCADE, null=True)
    web_filter = models.ForeignKey(WebFiltering, on_delete=models.CASCADE, null=True)
    position = models.IntegerField(default=0)
    custom = models.IntegerField(choices=custom_type, default=1)

    def __int__(self):
        return self.key

    class Meta:
        verbose_name_plural = "Rules"
        get_latest_by = 'key'

