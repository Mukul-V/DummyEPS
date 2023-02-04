from django.db import models


class Organization(models.Model):
    key = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=150)
    dob = models.DateField()
    created_at = models.DateField(verbose_name="created_at", auto_now_add=True)
    updated_at = models.DateField(verbose_name='updated_at', auto_now=True)

    def __int__(self):
        return self.key

    class Meta:
        verbose_name_plural = "Organization"
