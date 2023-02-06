from django.db import models
from epsapp.models.ContentClassification import ContentClassification


class FileContent(models.Model):
    key = models.AutoField(primary_key=True)
    file_data = models.ForeignKey(ContentClassification, on_delete=models.CASCADE)
    file_row = models.CharField(max_length=150)

    def __int__(self):
        return self.key

    class Meta:
        verbose_name_plural = "File Content"
