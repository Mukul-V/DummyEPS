from django.db import models
from epsapp.models.Rules import Rules
from epsapp.models import Users, UserGroup


class RuleUserMapping(models.Model):
    key = models.AutoField(primary_key=True)
    rule = models.ForeignKey(Rules, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    user_group = models.ForeignKey(UserGroup, on_delete=models.CASCADE, null=True)

    def __int__(self):
        return self.key

    class Meta:
        verbose_name_plural = "Rules User Mapping"
