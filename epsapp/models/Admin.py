from django.db import models
from epsapp.models.UserAuthentication import UserAuthentication
from epsapp.models.Organization import Organization
from epsapp.models.Role.Role import Role


class Admin(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    user_auth = models.ForeignKey(UserAuthentication, on_delete=models.CASCADE)
    key = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name="name")
    country_code = models.CharField(max_length=3, default="+00")  # Including + symbol
    phone = models.IntegerField(default=None)
    email = models.EmailField(default=None)
    dob = models.CharField(max_length=100, verbose_name="dob")
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Admin"
