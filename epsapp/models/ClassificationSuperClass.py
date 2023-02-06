from django.db import models


class ClassificationSuperClass(models.Model):
    key = models.AutoField(primary_key=True)

    def __int__(self):
        return self.key

    class Meta:
        verbose_name_plural = "FileClassification Super Class"
        get_latest_by = 'key'
