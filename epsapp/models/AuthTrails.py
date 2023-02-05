from django.db import models
from epsapp.models.UserAuthentication import UserAuthentication


class AuthTrails(models.Model):
    key = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100, null=True)
    reason = models.CharField(max_length=100, null=True)
    user = models.ForeignKey(UserAuthentication, on_delete=models.CASCADE)
    user_login = models.DateTimeField(null=True)
    user_logout = models.CharField(max_length=255, null=True)
    user_agent = models.CharField(max_length=255, null=True)
    token = models.CharField(max_length=500, null=True)
    user_ip = models.CharField(max_length=100, null=True)
    user_os = models.CharField(max_length=100, null=True)

    def __int__(self):
        return self.key

    class Meta:
        verbose_name_plural = "Auth Trails"
        get_latest_by = 'key'
