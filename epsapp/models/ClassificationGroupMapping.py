from django.db import models
from epsapp.models.BaseClassificationGroup import BaseClassificationGroup
from epsapp.models.ClassificationSuperClass import ClassificationSuperClass


class ClassificationGroupMapping(models.Model):
    key = models.AutoField(primary_key=True)
    class_group = models.ForeignKey(BaseClassificationGroup, on_delete=models.CASCADE, null=True)
    class_super = models.ForeignKey(ClassificationSuperClass, on_delete=models.CASCADE, null=True)
    types = models.IntegerField(default=1)  # Need to make enum for this

    def __int__(self):
        return self.key
