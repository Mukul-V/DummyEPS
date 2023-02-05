from django.db import models


class ContentClassification(models.Model):
    key = models.AutoField(primary_key=True)
    relation_of_data = models.CharField(max_length=5, null=True)
    keyword_regex = models.CharField(max_length=150)
    validation_type = models.CharField(max_length=15)
    old_name = models.CharField(max_length=150, null=True)
    validation_value = models.CharField(max_length=150, null=True)
    no_of_matches = models.IntegerField()

    def __int__(self):
        return self.key

    class Meta:
        verbose_name_plural = "File Data"
        get_latest_by = 'key'
