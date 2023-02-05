from django.db import models
from epsapp.models.CommonFields import feature_type


class FeatureTable(models.Model):
    key = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, unique=True)
    self_type = models.IntegerField(choices=feature_type, default=2)
    id_grand_parent = models.IntegerField()
    id_parent = models.IntegerField()
    is_hide = models.IntegerField()
    position = models.IntegerField()
    possible_permission = models.IntegerField()

    def __int__(self):
        return self.key

    class Meta:
        verbose_name_plural = "Features Table"
        get_latest_by = "key"