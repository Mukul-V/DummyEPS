from django.db import models
from epsapp.models.UserGroup import UserGroup
from epsapp.models.Users import Users


class Users_User_Group_Mapping(models.Model):
    key = models.AutoField(primary_key=True)
    user_group = models.ForeignKey(UserGroup, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __int__(self):
        return self.key

    class Meta:
        verbose_name_plural = "Users User Group Mapping"
