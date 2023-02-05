from django.db import models
from epsapp.models.Organization import Organization
from epsapp.models.CommonFields import custom_type, class_group_type


class BaseClassificationGroup(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, default=None)
    key = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=1000)
    custom = models.IntegerField(choices=custom_type, default=1)
    # 1 -> Device_Class
    # 2 -> App_Class
    # 3 -> Web_Class
    # 4 -> File_Class
    # 5 -> Ip Class
    # 6 -> Schedule_Class
    type = models.IntegerField(choices=class_group_type, default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Base Classification Group"
        get_latest_by = 'key'

