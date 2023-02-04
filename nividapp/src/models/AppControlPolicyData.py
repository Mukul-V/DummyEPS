from django.db import models


class AppControlPolicyData(models.Model):
    key = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField()
    issue = models.CharField(max_length=30)
    description = models.TextField()

    def __int__(self):
        return self.key

    class Meta:
        verbose_name_plural = "Contact Us"
