from django.db import models
from epsapp.models.Admin import Admin
# from wijungleapp.src.models.Users import Users
from epsapp.models.Organization import Organization


class TokenAuth(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, verbose_name="organization_key")
    key = models.AutoField(primary_key=True)
    access_token = models.CharField(max_length=300, verbose_name="access_token")
    refresh_token = models.CharField(max_length=300, verbose_name="refresh_token")
    admin_key = models.ForeignKey(Admin, on_delete=models.CASCADE, verbose_name="admin_key", null=True)
    # user_key = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name="users_key", null=True)
    role = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    status = models.IntegerField()

    def __int__(self):
        return self.key

    class Meta:
        verbose_name_plural = "Token Authentication"
