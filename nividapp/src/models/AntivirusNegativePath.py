from django.db import models
from nividapp.src.models.Antivirus import Antivirus


class AntivirusNegativePath(models.Model):
    key = models.AutoField(primary_key=True)
    antivirus = models.ForeignKey(Antivirus, on_delete=models.CASCADE)
    negative_path = models.CharField(max_length=200)

    def __int__(self):
        return self.key

    class Meta:
        verbose_name_plural = "Antivirus Negative path Model"
