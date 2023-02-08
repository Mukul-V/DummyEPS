from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from epsapp.managers.Manager import UserManager
from epsapp.models.Organization import Organization


class UserAuthentication(AbstractBaseUser):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True)
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, verbose_name="username")
    password = models.CharField(max_length=100, verbose_name="password")
    type = (
        (1, "Admin"),
        (2, "Users")
    )
    user_type = models.IntegerField(choices=type, default=1)
    joined_at = models.DateField(verbose_name="joined_at", auto_now_add=True)
    updated_at = models.DateField(verbose_name="updated_at", auto_now=True)
    jwt_issue_dt = models.CharField(max_length=100, null=True)
    invalid_attempt = models.IntegerField(default=0)
    holding_datetime = models.DateTimeField(null=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['password']

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "User Authentication"
        unique_together = ('username', 'user_type',)
        get_latest_by = 'key'

    def __int__(self):
        return self.key

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_active

    objects = UserManager()
