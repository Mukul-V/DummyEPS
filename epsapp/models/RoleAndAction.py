from django.db import models
from epsapp.models.Role import Role
from epsapp.models.FeatureTable import FeatureTable


class RoleAndAction(models.Model):
    key = models.AutoField(primary_key=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    feature_id = models.ForeignKey(FeatureTable, on_delete=models.CASCADE)
    permission = models.IntegerField()

    def __int__(self):
        return self.key

# 0 -> not show
# 1 -> Read (not possible create and update)
#


"""
{
    "key": 1,
    "device_class": 0,
    "app_class": 2,
    "device_policy": 1,
    "app_policy": 1,
    "rules": 2
}


{
    "Token":{},
    "msg":"",
    "feature":{
        "wijungle": {
            children:
        }
    }
}
"""
