from django.db import models
from epsapp.models.Organization import Organization
from epsapp.models.UserGroup.UserGroup import UserGroup
from epsapp.models.UserAuthentication import UserAuthentication


class Users(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    user_auth = models.ForeignKey(UserAuthentication, on_delete=models.CASCADE)
    key = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name="name")
    country_code = models.CharField(max_length=3)  # Including + symbol
    phone = models.IntegerField()
    email = models.EmailField()
    dob = models.CharField(max_length=100, null=True, verbose_name="dob")
    user_group = models.ForeignKey(UserGroup, on_delete=models.CASCADE)
    os = models.BigIntegerField(null=True, default=0)  # 0 defines all OS
    mac_address = models.TextField(null=True)

    def __int__(self):
        return self.key

    class Meta:
        verbose_name_plural = "User"
        get_latest_by = "key"


