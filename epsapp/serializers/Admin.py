from rest_framework import serializers
from epsapp.models.Admin import Admin


class Admin(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['organization', 'user_auth', 'key', 'name', 'phone', 'email', 'dob', 'role_id']
