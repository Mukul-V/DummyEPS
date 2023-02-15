from rest_framework import serializers
from epsapp.models.ClassificationSuperClass import ClassificationSuperClass


class ClassificationSuperClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassificationSuperClass
        fields = ['key']
