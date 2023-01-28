from dataclasses import field, fields
from SMS.models import student
from rest_framework.serializers import ModelSerializer

class StudentSerializer(ModelSerializer):
    class Meta:
        model=student
        fields=['name','mobileno','address']
        