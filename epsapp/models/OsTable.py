from django.db import models


class OsTable(models.Model):
    key = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    value = models.IntegerField(unique=True)

    def __int__(self):
        return self.key

    class Meta:
        verbose_name_plural = "Os Table"
        get_latest_by = "key"
