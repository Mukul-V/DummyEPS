from django.db import models
from epsapp.models.Antivirus.Antivirus import Antivirus


class AntivirusNegativePathModel(models.Model):
    key = models.AutoField(primary_key=True)
    antivirus = models.ForeignKey(Antivirus, on_delete=models.CASCADE)
    negative_path_model = models.CharField(max_length=200)

    def __int__(self):
        return self.key

    class Meta:
        verbose_name_plural = "Antivirus Negative Path Model"
