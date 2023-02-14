from rest_framework import serializers
from epsapp.models.AppControlPolicyData import AppControlPolicyData


class AppControlPolicyData(serializers.ModelSerializer):
    class Meta:
        model = AppControlPolicyData
        fields = ['app_control_policy', 'key', 'app_class_group', 'schedule_class_group', 'action']
