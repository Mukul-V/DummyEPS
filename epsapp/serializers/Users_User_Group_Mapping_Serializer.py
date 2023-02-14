from rest_framework import serializers
from epsapp.models.Users_User_Group_Mapping import Users_User_Group_Mapping


class Users_User_Group_Mapping(serializers.ModelSerializer):
    class Meta:
        model = Users_User_Group_Mapping
        fields = ['key', 'user_group', 'user']

