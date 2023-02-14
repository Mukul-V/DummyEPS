from django.db import models


class FileDetail(models.Model):
    key = models.AutoField(primary_key=True)
    old_name = models.CharField(max_length=200)
    new_name = models.CharField(max_length=200)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.new_name

    class Meta:
        verbose_name_plural = 'File Details'

