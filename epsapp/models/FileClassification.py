from django.db import models
from epsapp.models.Organization import Organization
from epsapp.models.ClassificationSuperClass import ClassificationSuperClass
from epsapp.models.CommonFields import custom_type, file_type


class FileClassification(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    class_super = models.ForeignKey(ClassificationSuperClass, on_delete=models.CASCADE)
    key = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)
    file_type = models.IntegerField(choices=file_type, default=1)
    file_title = models.CharField(max_length=200, null=True)
    file_desc = models.CharField(max_length=500, null=True)
    file_ext = models.CharField(max_length=100, null=True)
    subject = models.CharField(max_length=200, null=True)
    tags = models.CharField(max_length=200, null=True)
    author = models.CharField(max_length=150, null=True)
    program = models.CharField(max_length=200, null=True)
    company = models.CharField(max_length=150, null=True)
    content_created = models.CharField(max_length=200, null=True)
    date_last_saved = models.DateField(auto_now_add=False, null=True)
    size = models.CharField(max_length=100, null=True)
    date_created = models.DateField(auto_now=True)
    date_modified = models.DateField(auto_now_add=True)
    owner = models.CharField(max_length=150, null=True)
    folder_path = models.CharField(max_length=200, null=True)
    custom = models.IntegerField(choices=custom_type, default=1)

    def __int__(self):
        return self.key

    class Meta:
        verbose_name_plural = "File Classification"
        get_latest_by = "key"
