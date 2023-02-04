from django.db import models
from nividapp.src.models.Organization import Organization
from nividapp.src.models.UserAuthentication import UserAuthentication
from nividapp.src.models.Role import Role


class Admin(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    user_auth = models.ForeignKey(UserAuthentication, on_delete=models.CASCADE)
    key = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField()
    dob = models.CharField(max_length=50)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)