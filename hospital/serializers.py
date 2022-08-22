from django.db.models import fields
from rest_framework import serializers
from .models import *


class HospitalAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'


class HospitalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'

    def create(self,validated_data):
        instance = Hospital.objects.create(**validated_data)
        instance.save()
        


