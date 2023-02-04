from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from nividapp.src.models.Organization import Organization
from nividapp.src.managers.Manager import UserManager


class UserAuthentication(AbstractBaseUser):
    key = models.AutoField(primary_key=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    type = (
        (1, "Admin"),
        (2, "Users")
    )
    user_type = models.IntegerField(choices=type, default=1)
    joined_at = models.DateField(verbose_name="joined_at", auto_now_add=True)
    invalid_attempt = models.IntegerField(default=0)
    holding_datetime = models.DateTimeField(null=True)
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["password"]

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "User Authentication"
        unique_together = ('username', 'user_type')
        get_latest_by = 'key'

    def __int__(self):
        return self.key

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def is_staff(self):
        return self.is_active

    objects = UserManager()
